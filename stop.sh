#!/bin/bash

if [ -f "server_pid.txt" ]; then
  server_pid=$(cat server_pid.txt)

  kill $server_pid

  rm server_pid.txt

  echo "Serwer został zatrzymany."
else
  echo "Plik z PID serwera nie istnieje. Serwer nie jest uruchomiony."
fi

exit 0