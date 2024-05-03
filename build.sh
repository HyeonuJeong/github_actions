pid=$(lsof -ti :7070)

kill -9 $pid

SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

git pull

git checkout $1

python main.py
