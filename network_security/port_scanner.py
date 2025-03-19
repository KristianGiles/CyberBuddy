import nmap

def scanner(target):
    scanner = nmap.PortScanner()

    scanner.scan(target, arguments='-pN -sS -sV')

    return scanner.all_hosts()

results = scanner('172.31.96.1')

print(results)