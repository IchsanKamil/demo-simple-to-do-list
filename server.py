from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 80
WEB_DIR = os.path.dirname(os.path.abspath(__file__))

class TaskHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

if __name__ == "__main__":
    with HTTPServer(("0.0.0.0", PORT), TaskHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
