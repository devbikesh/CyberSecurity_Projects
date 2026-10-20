import socket

host = "127.0.0.1"
ports = [21, 22, 80, 443, 3306, 8080]

for port in ports:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    result = client.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is OPEN")
    else:
        print("Port", port, "is CLOSED or NOT ACCESSIBLE")

    client.close()