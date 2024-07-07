# Get Ipaddress and Hostname of Website
This Python script retrieves the IP address and hostname of a given website URL using the socket library.

## Description
The script prompts the user to enter a website address (URL). It then attempts to fetch and display the corresponding hostname and IP address using the socket.gethostbyname() function. If the hostname is invalid or cannot be resolved, it catches and prints a socket.gaierror.

## Required Modules
No additional modules are required beyond the standard Python library.

## How to Install Required Modules
No installation of additional modules is needed

## How to Run the Script
1. Clone the Repository:
```bash 
         git clone https://github.com/yourusername/get-website-ip.git
         cd get-website-ip
```
2. Run the Script:
```bash 
        python3 get_website_ip.py
```