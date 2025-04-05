#clear(),extend(),count(),pop(),remove()

# randomlist=[1,25,6,7,7,8]
# randomlist.clear()
# print(randomlist)
#ეს ფუნქცია აშორებს ლისტიდან ყველაფერს

# numlist1=[1,2,6,7,4,9]
# numlist2=[3,5,10,11]
# numlist1.extend(numlist2)
# print(numlist1)
#ეს ფუნქცია აერთიანებს ლისტებს

# numberlist=[3,5,6,8,9,6,5]
# print(numberlist.count(5))
#ეს ფუნქცია აბრუნებს იმას თუ რამნდერჯერ არის რიცხვი ლისტში

# lists=["adamiani","frinveli","ragaca","msxali"]
# lists.pop(3)
# print(lists)
#ეს ფუნქცია აშორებს ლისტიდან ელემენტს ინდექსინგის საშუალებით

# lists=["adamiani","frinveli","ragaca","msxali"]
# lists.remove("msxali")
# print(lists)
#ეს ფუნქცია აშორებს ლისტიდან ელემენტს დასახელების საშუალებით




# n = int(input("შემოიტანე ციფრი"))
# a = []
# for i in range(n):
#     a.append(int(input("შემოიტანე ციფრი")))
# for i in range(n):
#     if a[i] not in a[:i]:
#         if a.count(a[i]) > 1:
#             print("ციფრი", a[i], "მეორდება", a.count(a[i]), "ჯერ")



# someoneslist=[2,5,6,7,4,3]
# someone=input("would you like to clear all list?")
# if someone=="yes":
#     someoneslist.clear()
#     print("list cleared")
# else:
#     print(someoneslist)




# fruits=["msxali","vashli","marwyvi","sazamtro","yurdzeni"]
# user=int(input("enter a index to remove a fruit from fruits list"))
# fruits.pop(user)
# print(fruits)



