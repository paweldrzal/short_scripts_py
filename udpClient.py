import socket

def Main():
	host = "127.0.0.1"
	port = 5000

	server= ("127.0.0.1", 5000)

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))
	
	message = raw_input("->")
	while message != "q":
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print "Recieved from server: " +str(data)
		message = raw_input("->")
	s.close()
	
if __name__ == '__main__':
	Main()
