user_input = input("შეიყვანეთ რიცხვები: ") 
user_num = 0

current_number = ""  
for char in user_input:  
    if char == ",":  
        user_num += int(current_number)  
        current_number = ""  
    else:
        current_number += char  


if current_number:
    user_num += int(current_number)

print("შეყვანილი რიცხვების ჯამი არის: ", user_num)



