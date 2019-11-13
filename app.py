from http.server import HTTPServer, BaseHTTPRequestHandler

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text-html')
        self.end_headers()
        greeting = "Hello Emerging Tech Valencia!!\n"
        self.wfile.write(greeting.encode())
        return

try:
    server = HTTPServer(('0.0.0.0', 8080), GetHandler)
    server.serve_forever()

except KeyboardInterrupt:
    print("Shutting down web server")
    server.socket.close()