import socket
import requests

HOST = "127.0.0.1"
PORT = 65001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data)     
            #decoded = data.decode()   
            credentials = str(data).split(',')
            username = credentials[0]
            password = credentials[1]

            jsonCreds = {"username": username, "password":password}

            request = requests.post()
            print(username)
            print(credentials)
            #store data in another object
            #convert data to json
            # create post request 
            # send post request to oauth provider 
            # receive response from oauth provider
            # encrypt using client password hash 
            # send back to client
