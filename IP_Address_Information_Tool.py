import ipaddress
print("===== IP ADDRESS INFORMATION TOOL =====")
ip_address=input("Enter an IP address:")

try:

    address=ipaddress.ip_address(ip_address)
    print("Valid Ip Address:",address)
    print("IP Version:",address.version)

    if address.is_loopback:
        address_type = "Loopback"
        print("Address Type:", address_type)
    elif address.is_link_local:
        address_type = "Link-local"
        print("Address Type:", address_type)
    elif address.is_reserved:
        address_type = "Reserved"
        print("Address Type:", address_type)
    elif address.is_private:
        address_type = "Private"
        print("Address Type:", address_type)
    else:
        address_type = "Public"
        print("Address Type:", address_type)
    report = f"""===== IP ADDRESS REPORT =====
     IP Address: {address}
     IP Version: {address.version}
     Address Type: {address_type}
     """  
    with open("ip_report.txt","w") as file:
        file.write(report)
    print("Report saved to ip_report.txt")
    
except ValueError:
    print("Invalid IP address")
