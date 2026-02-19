#!/usr/bin/python3
"""Task 3: Simple API using Python http.server module"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API.
    
    This handler implements:
    - GET requests for / (root), /data, /status, /info endpoints
    - Proper JSON responses with correct headers
    - 404 error handling for undefined endpoints
    """

    def do_GET(self):
        """
        Handle GET requests to different endpoints.
        """
        # Define routes
        if self.path == "/":
            # Root endpoint - simple text response
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode("utf-8"))

        elif self.path == "/data":
            # Data endpoint - returns JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Status endpoint - returns OK
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))

        elif self.path == "/info":
            # Info endpoint - returns API info
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # Undefined endpoint - 404 Not Found
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error).encode("utf-8"))

    def log_message(self, format, *args):
        """
        Override to customize logging format.
        """
        print(f"[{self.client_address[0]}] {format % args}")


def run_server(host="127.0.0.1", port=8000):
    """
    Start the HTTP server on specified host and port.
    
    Args:
        host (str): The hostname to bind to (default: 127.0.0.1)
        port (int): The port number to bind to (default: 8000)
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Server running at http://{host}:{port}")
    print("Press Ctrl+C to stop the server")
    print("\nAvailable endpoints:")
    print(f"  GET http://{host}:{port}/          - Simple text response")
    print(f"  GET http://{host}:{port}/data      - JSON data")
    print(f"  GET http://{host}:{port}/status    - Status check")
    print(f"  GET http://{host}:{port}/info      - API information")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)


if __name__ == "__main__":
    run_server()
