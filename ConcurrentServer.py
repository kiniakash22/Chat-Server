import threading
import socket

print("Welcom to Concurent Server!!!")
count = 1
client_list = []
class Conversation(threading.Thread):
    def __init__(self, nis):
        global count, client_list
        threading.Thread.__init__(self)
        self.nis = nis
        self.client_id = count
        count += 1

    def run(self):
        global client_list
        client_list.append(self.nis)
        data = ""
        while data != 'q':
            data = self.nis.recv(1024).decode()
            print("Client {} sent -> {}".format(self.client_id, data))
            for c in client_list: 
                c.send(str("Client "+str(self.client_id)+" > "+data).encode(encoding='utf_8', errors='strict'))
        print    
        self.nis.close()

soc = socket.socket()
soc.bind(("localhost", 9898))
soc.listen(3)
while True: 
    print("Waiting for Client")
    client, add = soc.accept()
    print("Connected with client: ", add)
    Conversation(client).start()
soc.close()
print("Server closed")
