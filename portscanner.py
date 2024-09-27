import nmap
import pyfiglet

def scanner(target_name, target_port):
    nm = nmap.PortScanner()

    print("\nScanning the target...")
    if target_port:
        nm.scan(target_name, target_port, arguments='-nP')
    else:
        nm.scan(target_name)

    for host in nm.all_hosts():
        print("-------------------------------------------\n")
        print(f"Host: {host}\n")
        print(f"Host name: {nm[host].hostname()}\n")
        print(f"State of Host: {nm[host].state()}\n")
        print("---------------------\n")
        for proto in nm[host].all_protocols():
            print("PORT\t\tSTATE\t\tSERVICE\n")
            for port in nm[host][proto].keys():
                supports = "tcp" if nm[host].has_tcp(port) else "udp"
                print(f"{port}/{supports}\t\t{nm[host][proto][port]['state']}\t\t{nm[host][proto][port]['name']}\n")



if __name__ == "__main__":
    print(pyfiglet.figlet_format("PORT", font="ansi_shadow", justify="center"))
    print(pyfiglet.figlet_format("SCANNER", font="ansi_shadow", justify="center"))

    target_name = str(input("Enter the target domain name or IP address: "))
    target_port = str(input("\nEnter a port or range of ports to scan (optional): "))

    scanner(target_name, target_port)
