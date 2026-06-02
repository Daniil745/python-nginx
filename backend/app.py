from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == "/":
      self.send_response(200)
      self.send_header('Content-type', 'text/plain; charset=utf-8')
      self.end_headers()
      self.wfile.write(b"Hello from Effective Mobile!")
    else:
      self.send_error(404, "Not_found")

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8080):
  server_address=('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Server is starting on port {port}')
  httpd.serve_forever()

if __name__ == "__main__":
  run()

