from django.http import HttpResponse
import socket

# Code for the greet web application.
# Simply return a string "Hello from <docker host>"

def greet(request):
 return HttpResponse("Hello from ” + socket.gethostname() + “")