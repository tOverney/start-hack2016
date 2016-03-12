import os

import sys

try:
    from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
    from SocketServer import TCPServer as Server
except ImportError:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carousel.settings")

from django.core.management import execute_from_command_line

args = ['runserver', PORT]
args.append(sys.argv)
execute_from_command_line(args)
