user_year = int(input('year'))

if user_year % 4 == 0 and user_year % 100 != 0 or user_year % 400 == 0:
    print("ეს არის ნაკიანი წელი")

else:
    print("ეს წელი არ არის ნაკიანი")








