<<<<<<< HEAD
pid=$(lsof -ti :7070)

kill -9 $pid

SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

git pull

git checkout $1

python main.py
=======

sh stop.sh
>>>>>>> de516b154019a056a5beb4498d62ac40a9b2b348
