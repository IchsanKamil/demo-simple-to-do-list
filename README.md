# Simple Web App Task Manager

This is a simple HTML-based task manager web app that runs in a Docker container using Flask (Python web application).

## How to Run

1. **Build the Docker image:**
   ```sh
   docker build -t simple-task-manager .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8080:80 simple-task-manager
   ```
3. Open your browser and go to [http://localhost:8080](http://localhost:8080)

## Files
- `index.html`: The main web app UI
- `app.py`: Flask web application
- `Dockerfile`: Containerizes the app using Python
