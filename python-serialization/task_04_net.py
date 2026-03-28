#!/usr/bin/python3
"""
Module for simple client-server dictionary transmission using JSON and sockets.
"""
import socket
import json


def start_server():
    """
    Starts a server that listens for a connection, receives serialized JSON data,
    deserializes it, and prints the resulting dictionary.
    """
    host = '127.0.0.1'  # Localhost
    port = 65432        # İstifadə olunmayan ixtiyari port

    try:
        # TCP/IP soketi yaradırıq
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Portu bağlayırıq və qulaq asmağa başlayırıq
            s.bind((host, port))
            s.listen()
            # print("Server is listening on {}:{}".format(host, port))

            conn, addr = s.accept()
            with conn:
                # Məlumatı qəbul edirik (maksimum 1024 bayt)
                data = conn.recv(1024)
                if data:
                    # Baytları deşifrə edib JSON-dan lüğətə çeviririk
                    received_dict = json.loads(data.decode('utf-8'))
                    print("Received Dictionary from Client:")
                    print(received_dict)
    except Exception as e:
        print("Server error: {}".format(e))


def send_data(dictionary):
    """
    Acts as a client that connects to the server and sends a serialized dictionary.

    Args:
        dictionary (dict): The Python dictionary to be sent.
    """
    host = '127.0.0.1'
    port = 65432

    try:
        # Lüğəti JSON sətirinə, sonra isə baytlara çeviririk
        serialized_data = json.dumps(dictionary).encode('utf-8')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(serialized_data)
    except ConnectionRefusedError:
        print("Connection failed: Is the server running?")
    except Exception as e:
        print("Client error: {}".format(e))
