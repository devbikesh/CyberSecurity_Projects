
import socket

domain_name = input("Enter Domain Name: ")

if not domain_name.strip():
    print("Domain name cannot be empty.")

else:
    try:
        ip_addresses = socket.gethostbyname_ex(domain_name)[2]

        print("Domain Name:", domain_name)
        print("IP Addresses:")

        for ip_address in ip_addresses:
            print(ip_address)

        # Create the DNS lookup report
        report = "===== DNS LOOKUP REPORT =====\n"
        report += f"Domain Name: {domain_name}\n"
        report += "IP Addresses:\n"

        for ip_address in ip_addresses:
            report += f"{ip_address}\n"

        # Save the report to a file
        with open("dns_report.txt", "w") as file:
            file.write(report)

        print("DNS report saved to dns_report.txt")

    except socket.gaierror:
        print("Could not find the IP addresses for this domain.")
