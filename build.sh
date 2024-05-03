#!/bin/zsh

pid=$(lsof -ti :7070)
current_date=$(date "+%Y-%m-%d")
current_time=$(date "+%H-%M-%S")

kill -9 $pid
sleep 3
SCRIPT_DIR=$(dirname "$0")
cd $SCRIPT_DIR

git checkout main
git pull
sleep 3
git checkout $1
sleep 3
nohup python main.py > log_${current_date}_${current_time}.log 2>&1 &

