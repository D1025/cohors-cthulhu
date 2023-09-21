#!/bin/bash

# Set the current directory as the base directory
BASE_DIR=$(dirname "$0")

# Run setup.py
python "$BASE_DIR/backend/resources/setup.py"

# Check the exit code of the previous command
if [ $? -ne 0 ]; then
  echo "Błąd w setup.py"
  exit 1
fi

# Change directory to frontend
cd "$BASE_DIR/frontend"

# Install npm dependencies
npm i

# Check the exit code of the previous command
if [ $? -ne 0 ]; then
  echo "Błąd w instalacji zależności npm"
  exit 1
fi

# Go back to the base directory
cd "$BASE_DIR"

# Run main.py in the background
python "$BASE_DIR/backend/python/main.py" &

# Check the exit code of the previous command
if [ $? -ne 0 ]; then
  echo "Błąd w uruchamianiu main.py"
  exit 1
fi

# Run the frontend server in the background
npm --prefix "$BASE_DIR/frontend" run start &

# Check the exit code of the previous command
if [ $? -ne 0 ]; then
  echo "Błąd w uruchamianiu serwera frontendowego"
  exit 1
fi

# Save the process ID of the server
echo $! > "$BASE_DIR/server_pid.txt"

echo "Serwer został uruchomiony."

exit 0