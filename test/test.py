#1)შექმენი ორი ცვლადი სადაც შეინახავ შენს სახელს გვარს და ასაკს და გამოიტანე ეს სამი მნიშვნელობა ერთ წინადადებად,გამოყავი ეს სიტყვები სფეისებით

# name="Daniel"
# surname="Datuashvili"
# age=16
# print(name,surname,age)


#2)მომხმარებელს შემოატანინე სახელი,გვარი და ასაკი,და გამოიტანე ეს სამი მნიშვნელობა ერთ წინადადებაში,გამოყავი ეს სამი სიტყვა სფეისებით

# user=input("enter your name and surname")
# user2=int(input("enter your age now"))
# print(user + " " +user2)


#3)შექმენი ორი ცვლადი num1 და num2 თუ num1 მეტია num2 ზე მაშინ ტერმინალში გამოიტანე "first is greater" და სცვა შემთვევაში გამოიტანე "second is greater"

# num1=14
# num2=16
# if num1>num2:
#     print("first is greater")
# else:
#     print("second is greater")



#4)მომხმარებელს შემოაყვანინე სახელი  და ასაკი,თუ მომხმარებლის შემოყვანილი ასაკი მეტია 18 ზე და ასევე მისი სახელი ემთხვევა შენს სახელს მაშინ დაუბეჭდე "same",თუ მომხმარებლის შემოყვბანული ასაკი ნაკლებია 18 ზე და ამავდროულად მისი სახელი ემთხევა შენს სახელს მაშინ დაუბეჭდე რომ "smaller than me",იმ შემთვევაში თუ მისი სახელი არ ემთვევა შენს სახელს დაუბეჭდე "not same"



# user=input("enter your name")
# age=int(input("enter your age"))
# if user.capitalize()=="Daniel" and age>=18:
#     print("same")
# elif user.capitalize()=="Daniel" and age<18:
#     print("smaller than me")
# elif user.capitalize()!="Daniel":
#     print("not same")




#5)შექმენი ორი ცვლადი სადაც შეინახავ განსხვავებულ რიცხვებს,შენი დავალებაა გაიგო ნაშთი როდესაც პირველ რიცხვს გავყობთ მეორე რიცხვზე

# num1=15
# num2=19

# print(num1%num2)



#6)მომხმარებელს შემოატანინე  3 რიცხვი,შენი დავალებაა იპოვო ამ სამი რიცხვის საშუალო არითმეტიკული

# num1=15
# num2=10
# num3=20
# sum=num1+num2+num3
# print(sum/3)

#7)რა იქნება საბოლოო პასუხი False and False or True or True and False
#True



#8)შექმენი ორი ცვლადი სადაც შეინახავ რიცხვებს,შენი დავალებაა  შეამოწმო თუ პირველი რიცხვი მეტია მეორე რიცხვზე და ასევე არის ლუწი,მაშინ ტერმინალში გამოიტანე greater than second number and even,შემდეგ შეამოწმე თუ პირველი რიცხვი მეტია მეორეზე და არის კენტი დაუბეჭდე greater than second number and odd,დანარჩენ სხვა შემთხვევაშ დაუპრინტე other


# num1=20
# num2=10

# if num1>num2 and num1%2==0:
#     print("greater than second number and even")

# elif num1>num2 and num1%2==1:
#     print("greater than second number and odd")
# else:
#     print("other")



#9)მომხმარებელს შემოატანინე წონა და ასაკი,შენი დავალებაა შეამოწმო თუ ასაკი მეტია ან უდრის 18  და წონა მეტია ან ტოლია 90,დაუპრინტე you can join and train in adult team,შემდეგ შეამოემე თუ ასაკი ნაკლებია ან ტოლია 18ზე და წონა ნაკლებია 90 დაუპრინტე you can join and train in young team



# age=int(input("enter your age"))
# weight=int(input("enter your weight"))

# if age>=18 and weight>=90:
#     print("you can join adult and train in the team")
# elif age<18 and weight<90:
#     print("you are in young team")


#10)შექმენი სამი ცვლადი სადაც შეინახავ შენს ასაკს,სახელს და აკადემიის სახელს, f სტრინგის გამოყენებით ტერმინალში გამოიტანე შემდეგი წინადადება --> გამარჯობათ,ჩემი სახელია name და მე ვარ age წლის,ასევე ვსწავლობ academy ში


# age=16
# name="Daniel"
# academy="GOA"

# print(f"გამარჯობათ,ჩემი სახელია {name} და მე ვარ {age} ასევე ვსწავლობ {academy}-ში")


#11)შექმენი ფუნქცია სახელად sum,სადაც გადასცემ პარამეტრად გადასცემ ორ ცვლადს num1 და num2,და არგუმენტად გადასცემ ორ რიცხვს,ანუ რაც გინდა რომ შეინახო ამ ორ ცვლადშ გამოძახების დროს,შენი დავალებაა უბრალოდ შეკრიბო ეს ორი რიცხვი და დააბრუნო მათი ჯამი


# def sum(num1,num2):
#     return(num1+num2)

# print(sum(15,20))


#12)შექმენი ფუნქცია დაარქვი სასურველი სახელი,ამ სიას პარამეტრად გადაეცი ცვლადი სახელად listt და არგუმენტად გადაეცი სია სადაც გექნება მოთავსებული რიცხვები,შენი დავალებაა იპოვო ამ სიაში მყოფი ყველა ლუწი რიცხვის ჯამი


# def lists(list):
#     sum=0
#     for i in list:
#         if i % 2==0:
#             sum+=i
#     return sum
            
            


# print(lists([15,5,7,9,6,2,4]))


#13)შექმენი ფუნქცია დაარქვი სასურველი სახელი,ამ სიას პარამეტრად გადაეცი ცვლადი სახელად listt და არგუმენტად გადაეცი სია სადაც გექნება მოთავსებული რიცხვები ათზე მეტი და ათზე ნაკლები,შენი დავალებაა იპოვო ამ სიაში მყოფი ყველა ათზე ნაკლები რიცხვების ჯამი

# def lists(list):
#     sum=0
#     for i in list:
#         if i < 10:
#             sum+=i
#     return sum

# print(lists([2,5,6,8,10]))




#14)შექმენი ფუნქცია და დაარქვი სასურველი სახელი,გადაეცი პარამეტრად ცვლადი და არგუმენტად გამოძახების დროს სია,შენი დავალებაა სიიდან ამოშალო ყველა ლუწი რიცხვი და დააბრუნო განახლებული სია ლუწი რიცხვების გარეშე


# def remove(num):
#     list=[]
#     for i in num:
#         if i%2==1:
#             list.append(i)
#     return list
# print(remove([2,5,76,8,11]))



#15)შექმენი ფუნქცია და დაარქვი სასურველი სახელი,გადაეცი პარამეტრად ცვლადი და არგუმენტად გამოძახების დროს ეს სია --> [10,11,13,14,16],შენი დავალებაა ამ სიაში დაამატო შესაბამის ინდექსზე ის რიცხვები რომელიც აკლია ამ სიას

# def add(list):
#     list.insert(2,12)
#     list.insert(5,15)
#     return list


# print(add([10,11,13,14,16]))



#16)შექმენი ფუნქცია და დაარქვი სასურველი სახელი,გადაეცი პარამეტრად ცვლადი და არგუმენტად გამოძახების დროს ეს სია --> [20,21,22,22,23,24,24,25],შენი დავალებაა ამოშალო ყველა ის რიცხვი ამ სიიდან რომელიც არღვევს თანმიმდევრობას


# def remove(num):
#     num.remove(22)
#     num.remove(24)
#     return num


# print(remove([20,21,22,22,23,24,24,25]))


#17)შექმენი ფუნქცია და დაარქვი სასურველი სხელი,გადაეცი პარამეტრად ცვლადი და არგუმენტად გამოძახების დროს ეს სია --> ["giorgi","lasha","beqa","danieli","ioane"],შენი დავალებაა ამ სიიდან ამოშალო შენი სახელი და დააბრუონო განახლებული სიან შენი სახელის გარეშე,



# def name(list):
#     list.pop(3)
#     return list



# print(name(["giorgi","lasha","beqa","danieli","ioane"]))


#18)შექმენი ფუნქცია და გადაეცი პარამეტრად ცვლადი და არგუმენტად გადაეცი სია,შენი დავალებაა გამოიტანო ლუწ ინდექსზე მდგომი რიცხვების კვადრატების ჯამი


# def something(list):
#     sum=0
#     for i in range(len(list)):
#         if i % 2==0:
#             sum+=list[i]
#             sum2=sum**2
#     return sum2



# print(something([5,6,4,2,7,8]))




#19)შექმენი ფუნქცია ,პარამეტრად გადაეცი ცვლადი და არგუმენტად გადაეცი სტრინგი --> "paparaci",შენი დავალებაა ამოშალო ამ სტრინგიდან ყველა ხმოვანი ასო და დააბრუნო ეს სსტრინგი ხმოვნების გარეშე,დაგჭირდება ცარიელი სტრინგი სადაც ჩაამატებ ასოებს ,რომლებიც არ არიან ხმოვნები


# def something(word):
#     new=""
#     for i in word:
#         if i not in "aeiou":
#             new+=i
#     return new

# print(something("paparaci"))



# list1=[1,2,4,5,7]
# list1.pop()
# print(list1)










# name=int(input)



# def most_common_type(lst):
#     ints = 0
#     strs = 0
#     floats = 0

#     for item in lst:
#         if type(item) == int:
#             ints += 1
#         elif type(item) == str:
#             strs += 1
#         elif type(item) == float:
#             floats += 1

#     if ints >= strs and ints >= floats:
#         return int
#     elif strs >= ints and strs >= floats:
#         return str
#     else:
#         return float




password=1234
trypass=int(input("Enter a number password"))
while trypass!=password:
    print("wrong,try again")
    trypass=input("enter a mumber password")
 
        






# def adding_num(a,b):
#     return a+b

# result=adding_num(5,3)
# print(result)