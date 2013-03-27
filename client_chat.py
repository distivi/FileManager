import sys
from tkinter import *
from socket import *
from threading import *

HOST = ''#'localhost'
PORT = 7000
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
try:
	tcpCliSock.connect(ADDR)
	print("Client Connected to server")
except:
	print("connection failed")
	sys.exit(0)

class Application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()
		self.socket()

	def callback(self, event):
		message = self.entry_field.get()
		tcpCliSock.send(bytes(message,'utf-8'))

	def create_widgets(self):
		self.messaging_field = Text(self, width = 110, height = 20, wrap = WORD)
		self.messaging_field.grid(row = 0, column = 0, columnspan = 2, sticky = W)

		self.entry_field = Entry(self, width = 92)
		self.entry_field.grid(row = 1, column = 0, sticky = W)
		self.entry_field.bind('<Return>', self.callback)

	def add(self, data):
		self.messaging_field.insert(END, data)

	def socket(self):
		def loop0():
			while 1:
				data = tcpCliSock.recv(BUFSIZE)
				if data: self.add(data)

		#thread.start_new_thread(loop0, ())
		t = Thread(target=loop0)		
		t.daemon = True
		t.start()



root = Tk()
root.title("Chat client")
root.geometry("550x260")

app = Application(root)

root.mainloop()