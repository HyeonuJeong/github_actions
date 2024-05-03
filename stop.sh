pid=$(lsof -ti :7070)

if [ -z "$pid" ]; then
    echo "포트 7070을 사용하는 프로세스가 없습니다."
else
    echo "포트 7070을 사용하는 프로세스 (PID: $pid)를 종료합니다."
    kill -9 $pid

    # 종료 후 프로세스 상태 확인
    if [ $? -eq 0 ]; then
        echo "프로세스 종료가 성공적으로 이루어졌습니다."
    else
        echo "프로세스 종료 중 오류가 발생했습니다."
    fi
fi
