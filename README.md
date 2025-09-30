# Demo Simple To Do List

This is a simple to-do list web app built with Flask. The app serves a single-page HTML UI and provides a REST API for managing tasks. All data is stored in memory (not persistent).

## How to Run

1. **Build the Docker image:**
   ```sh
   docker build -t demo-simple-to-do-list .
   ```
2. **Run the container:**
   ```sh
   docker run -p 5000:5000 demo-simple-to-do-list
   ```
3. Open your browser and go to [http://localhost:5000](http://localhost:5000)

## Files

- `app.py`: Flask web application (serves both backend and frontend)
- `Dockerfile`: Containerizes the app using Python
- `requirements.txt`: Python dependencies (Flask, Gunicorn)

## API Endpoints

- `GET /tasks` — Get all tasks (JSON array)
- `POST /tasks` — Add a new task (JSON: `{ "task": "..." }`)
- `DELETE /tasks/<idx>` — Delete a task by index

## Notes

- All tasks are stored in memory and will be lost when the server restarts.
- The UI is rendered directly from the Flask app (no separate HTML file).
