import socket

def get_domain_name(ip_address):
    try:
        # Use gethostbyaddr to get the domain name associated with the IP address
        domain_name, _, _ = socket.gethostbyaddr(ip_address)
        return domain_name
    except socket.herror:
        return "Unable to resolve domain name for the given IP address"

if __name__ == "__main__":
    # Input the IP address you want to look up
    ip_address = input("Enter the IP address: ")

    # Call the function and print the result
    domain_name = get_domain_name(ip_address)
    print(f"Domain name for {ip_address}: {domain_name}")
