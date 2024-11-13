# 10-ელემენტიანი სია
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# პირველი და ბოლო ელემენტის სხვაობა
გამოკლება = my_list[-1] - my_list[0]
print("ბოლო და პირველი ელემენტის სხვაობა არის" + " " + str(გამოკლება))

# სია
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

# სიის ელემენტები მე-2-დან მე-5 ინდექსამდე
sliced_list = my_list[2:6]
print("მე-2-დან მე-5 ინდექსი ჩათვლით:" + " " + str(sliced_list))

# თქვენი სახელი
name = "Nodo"

# სახელი ხუთჯერ
for i in range(5):
    print(name)


word = input("Enter a word: ")


for letter in word:
    print(letter)
