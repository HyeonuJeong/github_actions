import asyncio
import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    print(f"Received request for item_id: {item_id}")
    return {"item_id": item_id}


async def execute_build_script(version):
    # 빌드 스크립트 실행
    root = os.path.dirname(__file__)
    build_file = os.path.join(root, "build.sh")

    # 외부 명령 비동기 실행
    process = await asyncio.create_subprocess_shell(f"sh {build_file} {version}")
    await process.wait()
    return "build finish"


@app.get("/build/{version}")
async def update_version(version):
    print(f"Received request for version: {version}")

    asyncio.create_task(execute_build_script(version))

    return "build finish"


if __name__ == "__main__":
    root = os.path.dirname(__file__)
    print(root)
    uvicorn.run(app, host="0.0.0.0", port=7070)
