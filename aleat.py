import webapp
import socket
import random


class server (webapp.webApp):
	def process(self, parsedrequest):
		numrandom = str(int(random.random() * 1000 * 1000))
		return ("200 OK", "<html><body><h1>"
				+ str(numrandom)
				+ "</h1></body></html>")

if __name__ == "__main__":
		new_serv = server (socket.gethostname(), 1234)