user_list=[]
for i in range(11):
    a=input()
    user_list.append(a)

print(user_list)

m_list = ["gela", "zviadi ","dato"]
user_input=input()
for i in m_list:
    if i == user_input:
        
        m_list.remove(user_input)

        print(m_list)