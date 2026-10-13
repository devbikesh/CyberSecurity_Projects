import socket
domain_name=input("Enter Domain Name:")
try:
    ip_address=socket.gethostbyname(domain_name)
    print("Domain Name:",domain_name)
    print("Ip Address:",ip_address)
except socket.gaierror:
    print("Could Not Find The IP Address for this Domain.")
    