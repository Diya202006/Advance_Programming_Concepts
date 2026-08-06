# Web Server Configuration System
 
server_ip = ("192", "168", "1", "10")
 
allowed_ips = [
    "192.168.1.100",
    "192.168.1.101"
]
 
def update_allowed_ips(ip):
    allowed_ips.append(ip)
    print("IP address added successfully.")
 
def update_server_ip(new_ip):
    print("Error: Server IP cannot be changed because it is stored as a tuple.")
 
def display_configuration():
    print("\n--- Server Configuration ---")
    print("Server IP:", ".".join(server_ip))
    print("Allowed IPs:")
    for ip in allowed_ips:
        print(ip)
 
display_configuration()
 
new_ip = input("\nEnter a new allowed IP address: ")
update_allowed_ips(new_ip)
 
choice = input("\nDo you want to change the server IP? (yes/no): ")

if choice.lower() == "yes":
    new_server_ip = input("Enter new server IP: ")
    update_server_ip(new_server_ip)
 
display_configuration()