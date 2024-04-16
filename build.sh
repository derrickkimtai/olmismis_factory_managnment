#!/usr/bin/env bash

# Build the project
echo "Building the project..."
mvn clean install

# Run the project
echo "Running the project..."
 pip install -r requirements.txt

 python3 manage.py migrate

 kim



 