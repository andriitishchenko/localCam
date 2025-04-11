# import http.server
# import ssl

# port = 8000
# httpd = http.server.HTTPServer(('0.0.0.0', port), http.server.SimpleHTTPRequestHandler)

# httpd.socket = ssl.wrap_socket(httpd.socket,
#                                keyfile="key.pem",
#                                certfile="cert.pem",
#                                server_side=True)

# print(f"Serving HTTPS on port {port}")
# httpd.serve_forever()


import http.server
import ssl

port = 8000
server_address = ('0.0.0.0', port)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Создаём SSL контекст
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

# Оборачиваем сокет
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on https://localhost:{port}")
httpd.serve_forever()