#ping atmak istediiniz ip numara aralığını girerek girdiğiniz aralıktaki ip numaralarının olup olmadığını kontrol ediyor.
import os
start_ip = input("ilk ip giriniz.")
end_ip = input("son ip gir")

start_ip_split = start_ip.split(".")
end_ip_split = end_ip.split(".")


for ip in range(int(start_ip_split[3]),int(end_ip_split[3])+1):
    current_ip = start_ip_split[0]+"."+start_ip_split[1]+"."+start_ip_split[2]+"."+str(ip)
    response = os.system("ping -c 1 "+ current_ip)

    if response == 0:
        print(current_ip," var")
    else: 
        print(current_ip," yok")
