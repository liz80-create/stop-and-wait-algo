import socket
import time
HOST = "25.69.150.115"  #hostname of the server
PORT = 12345 #Non-priviliged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connecting to the server
    while s:
      datatosend=input("Message-")#input message
      st=' '.join(format(ord(x), '08b') for x in datatosend) #converting to bits
      if datatosend == "Exit":
        s.close()
        break
      else:
        s.sendall(st.encode())
        ack = s.recv(1024)
        print(f"Received {ack.decode()}")
        if ack.decode()=='NAK':
          s.sendall(st.encode())
          print("Frame resent")

      
