import subprocess
# local ağdaki ip numaralarının listesini oluşturuyor...
output = subprocess.check_output(['nmap', '-sn', '192.168.1.0/24'])
output = output.decode('latin-1')

print("Ağdaki tüm cihazların IP adresleri:")
lines = output.splitlines()
for line in lines:
    if 'Nmap scan report for' in line:
        ip_address = line.split()[-1]
        print(ip_address)
