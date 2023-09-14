#!/bin/bash

python backend/resources/setup.py

if [ $? -ne 0 ]; then
  echo "Błąd w setup.py"
  exit 1
fi

python backend/python/main.py &

echo $! > server_pid.txt &

npm --prefix ./frontend run start

echo "Serwer został uruchomiony."

exit 0