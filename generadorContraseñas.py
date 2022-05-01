import random
size_password = int(input("de cuantos digitos nesecitas tu contraseña"))
list_password = [] 

turns_password = int(size_password // 5 + 2)
cont_password = 0

while turns_password - cont_password > 0 :
    cont_password += 1  
    list_password.append(random.randint(41,59))
    list_password.append(random.randint(61,79))
    list_password.append(random.randint(30, 39))
    list_password.append(random.randint(21,27))
            
list_ascii = []

for password in range(1, (size_password+1)):
    list_ascii.append(chr(list_password[random.randint(0, size_password)]))

passwordPass = "".join(list_ascii)

print(f"su contraseña es: {passwordPass}")