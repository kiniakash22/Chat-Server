import socket
from threading import Thread
from tkinter import *

def send_on_click(event):
    global text_area, client_input, connection_socket
    data = client_input.get()
    connection_socket.send(data.encode())
    client_input.delete(0, END)

def Receive():
    global text_area, client_input, connection_socket
    data = ""
    while data != 'q':
        data = connection_socket.recv(1024).decode()
        text_area.insert(END, data+"\n")
        

connection_socket = socket.socket()

root = Tk()
root.geometry("600x550")
text_area = Text(root)

client_input = Entry(root)
send_button = Button(root, text="Send")

send_button.bind("<Button>", send_on_click)

text_area.pack(side="top")
client_input.pack()
send_button.pack()

print("Initializing Client...")
connection_socket.connect(("localhost", 9898))
print("Connected to Server")

receiver = Thread(target=Receive)
receiver.start()

root.mainloop()


receiver.join()
connection_socket.close()
print("Closed")
