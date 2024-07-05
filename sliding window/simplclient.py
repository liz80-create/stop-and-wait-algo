import socket

HOST = "25.69.150.115"  #hostname of the server
PORT = 15200 #Non-priviliged port
    
stream= ['1','2','3','4','5','6','7','8','9','10','11','12']
window_size = 3
window_start = 0
window_end = window_size
window = stream[window_start:window_end]
num_iter = int(len(stream)/window_size)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT)) #connecting to the server
    print("connected")
    while s:
  
        for i in range(num_iter):
            temp_frame = stream[window_start:window_end]
            print(stream[window_start:window_end])
            print(len(temp_frame))
            print("=========================================================")
            #Moving sender's pointer in frame
            for  x in temp_frame:
                s.send(x.encode())        
                print(x + " Sent!")
            resp = s.recv(1024)
            print(resp.decode())
        
            window_start+=3
            window_end+=3
        break
        s.close()
        # print(window)