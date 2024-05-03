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
    build_file = os.path.join(os.path.dirname(__file__), "build.sh")
    process = await asyncio.create_subprocess_shell(f"sh {build_file} {version}")
    await process.wait()
    

@app.get("/build/{version}")
async def update_version(version):
    asyncio.create_task(execute_build_script(version))
    return f"Received request for version:{version}"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7070)
