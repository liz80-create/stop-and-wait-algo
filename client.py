import socket

HOST = "25.69.150.115"  #hostname of the server
PORT = 12345 #Non-priviliged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connecting to the server
    while s:
      datatosend=input("Message-")#input message
      st=' '.join(format(ord(x), '08b') for x in datatosend) #converting to bits
      #kachra=st+'1' #damaged
      if datatosend == "Exit":
        s.close()
        break
      else:
        s.sendall(st.encode())
        data = s.recv(1024)
        print(f"Received {data.decode()}")
      