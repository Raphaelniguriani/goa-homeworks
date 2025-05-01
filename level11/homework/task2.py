age = int(input('age'))

if age >= 1 and age < 12:
    print('child')

elif age > 12 and age < 18:
    print("teenager")

elif age > 18 and age < 30:
    print("adult")

else:
    print("senior")
