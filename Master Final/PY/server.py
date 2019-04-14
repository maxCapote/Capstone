#!/usr/bin/env python3

# Credit for this piece goes to GitHub user 'mildred'
# Source: https://gist.github.com/mildred/67d22d7289ae8f16cae7

import http.server
import os
import argparse

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_PUT(self):
        filename = self.translate_path(self.path)
        if filename.endswith('/'):
            self.send_response(405, "Method Not Allowed")
            self.end_headers()
            self.wfile.write("PUT not allowed on a directory\n".encode())
            return
        else:
            length = int(self.headers['Content-Length'])
            with open(filename, 'wb') as outfile:
                outfile.write(self.rfile.read(length))
            self.send_response(201, "Created")
            self.end_headers()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()

    http.server.test(HandlerClass=HTTPRequestHandler, port=args.port, bind=args.bind)
