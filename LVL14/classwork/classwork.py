# numbers = []

# for i in range(5):
#     number = int(input("Please enter a number: "))
#     numbers.append(number)

# for number in numbers:
#     if number % 2 == 0:
#         print(number, "is even")
#     else:
#         print(number, "is odd")


# names = []

# for i in range(5):
#     name = input("Please enter a number: ")
#     names.append(name)


# for name in names:
#     if len(name) > 5:
#         print(name)




# healthy_products = ["Tomato", "Apple", "Orange", "Alucha", "Cucumber"]

# healthy_products.pop(0)
# healthy_products.pop()

# print(healthy_products)




num=[1,2,'elementi',3,4]

nums=[]
string=[]

for i in num:
    if type(i)==int:
        nums.append(i)
    else:
        string.append(i)
print(nums)
print(string)

