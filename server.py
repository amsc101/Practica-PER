import web
import socketserver

##
# WEB SERVER
##

PORT = 9090
#Handler = http.server.SimpleHTTPRequestHandler --> handler de la biblioteca python
Handler = web.testHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
