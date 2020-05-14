import socket
import re
import sys
import os


def content_type(ext):
    if ext == '.html':
        return 'text/html'
    elif ext == '.txt':
        return 'text/plain'
    elif ext == '.pdf':
        return 'application/pdf'
    elif ext == '.png':
        return 'image/png'
    elif ext == '.jpg' or ext == '.jpeg':
        return 'image/jpeg'
    else:
        return 'none'


HOST = ''
PORT = int(sys.argv[1])

# build redirect mapping from redirect.defs
file = open('www/redirect.defs', 'r')
mapping = file.read()
file.close()
row = mapping.split('\n')
map = {}
for urls in row:
    tmp = urls.split(' ')
    if len(tmp) == 2:
        map.update({tmp[0]: tmp[1]})

# Configure socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(100)

while True:

    conn, addr = sock.accept()
    request = conn.recv(1024)

    if(len(request.split(' ')) < 2):
        content = 'HTTP/1.1 400 Bad Request\r\n'
        conn.sendall(content)
        conn.close()
        continue

    method = request.split(' ')[0]
    src = request.split(' ')[1]
    root_src = 'www' + src
    extentison = os.path.splitext(src)[1]

    # GET method
    if method == 'GET':
        # process redirects
        if src in map.keys():
            redirect_response = 'HTTP/1.1 301 Moved Permanently\r\nLocation: ' + \
                map[src] + '\r\n\r\n'
            content = redirect_response
        # validate resources
        elif os.path.isfile(root_src):
            if src == '/redirect.defs':
                error_response = 'HTTP/1.1 404 NOT FOUND\r\n'
                content = error_response
            else:
                con_type = content_type(extentison)
                con_len = os.path.getsize(root_src)
                index_content = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: ' + \
                    con_type + '\r\n' + 'Content-Length: ' + \
                    str(con_len) + '\r\n\r\n'
                file = open(root_src, 'r')
                index_content += file.read()
                file.close()
                content = index_content
        else:
            error_response = 'HTTP/1.1 404 NOT FOUND\r\n'
            content = error_response

    # HEAD method
    elif method == 'HEAD':
        # process redirects
        if src in map.keys():
            redirect_response = 'HTTP/1.1 301 Moved Permanently\r\nLocation: ' + \
                map[src] + '\r\n\r\n'
            content = redirect_response
        # validate resources
        elif os.path.isfile(root_src):
            if src == '/redirect.defs':
                error_response = 'HTTP/1.1 404 NOT FOUND\r\n'
                content = error_response
            else:
                con_type = content_type(extentison)
                con_len = os.path.getsize(root_src)
                index_content = 'HTTP/1.1 200 OK\r\nConnection: close\r\nContent-Type: ' + \
                    con_type + '\r\n' + 'Content-Length: ' + \
                    str(con_len) + '\r\n\r\n'
                content = index_content
        else:
            error_response = 'HTTP/1.1 404 NOT FOUND\r\n'
            content = error_response

    # Methods not supported
    else:
        other_methods_response = 'HTTP/1.1 405 Method Not Allowed\r\n'
        content = other_methods_response

    # send content
    conn.sendall(content)
    conn.close()
