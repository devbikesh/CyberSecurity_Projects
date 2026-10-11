import ipaddress
print("===== IP ADDRESS INFORMATION TOOL =====")
ip_address=input("Enter an IP address:")

try:

    address=ipaddress.ip_address(ip_address)
    print("Valid Ip Address:",address)
    print("IP Version:",address.version)
    if address.is_private:
        print("Address Type: Private")
    else:
        print("Address Type: Public")
    if address.is_loopback:
        print("Address Type: Loopback")
    elif address.is_link_local:
        print("Address Type: Link-Local")
    elif address.is_reserved:
        print("Address Type: Reserved")
    
except ValueError:
    print("Invalid IP address")
