import socket

def send_messages_to_server(messages, host='localhost', port=65432):
    received_messages = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        for message in messages:
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Sent: {message}, Received: {data.decode()}")
            if data.decode() == message:
                received_messages.append(message)
                
    return received_messages

if __name__ == "__main__":
    test_messages = ["Hello, Server!", "This is a test.", "Message 3", "Final message", 
                     "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", # EICAR
                    "XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X" # GTUBE
                    ]
    successfully_received = send_messages_to_server(test_messages)
    print(f"Successfully received messages: {successfully_received}")
# To do, add emulation of PII, PHI, CC, etc to test whether these messages go through.
