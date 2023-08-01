#!/bin/bash
 
DIR_TO_WATCH=${1}
COMMAND=${2}
 
trap "echo Exited!; exit;" SIGINT SIGTERM
${COMMAND} &
while [[ 1=1 ]]
do
  watch --chgexit -n 1 "ls -l ${DIR_TO_WATCH} | sha256sum"
  pkill -P $$
  ${COMMAND} &
  sleep 1
done