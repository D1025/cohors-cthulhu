#!/bin/bash

python backend/resources/setup.py

if [ $? -ne 0 ]; then
  echo "Błąd w setup.py"
  exit 1
fi

python backend/python/main.py &

npm --prefix ./frontend run start &

cd frontend &

npm i &

cd .. &

echo $! > server_pid.txt

echo "Serwer został uruchomiony."

exit 0