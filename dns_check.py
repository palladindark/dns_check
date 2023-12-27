import subprocess

def check_dns_resolution(domain, dns_servers, output_file):
    with open(output_file, 'w') as output:
        output.write(f"Checking DNS resolution for {domain} using different DNS servers:\n\n")
        for dns_server in dns_servers:
            try:
                result = subprocess.check_output(['nslookup', domain, dns_server], universal_newlines=True)
                output.write(f"DNS Server: {dns_server}\n{result}\n\n")
            except subprocess.CalledProcessError as e:
                output.write(f"DNS Server: {dns_server}\nError: {e.output}\n\n")

if __name__ == "__main__":
    domain_to_check = "github.com"
    dns_servers_file = "dns_ru.txt"
    output_file = "dns_resolution_results.txt"

    with open(dns_servers_file, 'r') as file:
        dns_servers_to_check = [line.strip() for line in file]

    check_dns_resolution(domain_to_check, dns_servers_to_check, output_file)
