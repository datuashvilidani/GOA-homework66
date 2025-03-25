#Control flow-ს აქვს სამი FLOW:1:Sequence კოდს მიყვება რიგრიგობით-2:iteration-აბრუნებს კოდს სანამ კოდის მოთხოვნებს არ დააკმაყოფილებს-3:Selection:მაგ if else-შეუძლია მიიღოს გადაწყვეტილებები

#iteration-აბრუნებს კოდს სანამ მოთხოვნა არ დაკმაყოფილდება. for და while ციკლი განსხვავდება იმით რომ როცა for ვიყენებთ იტერაციის რიცხვი ცნობილია ხოლო while ციკლის დროს იტერაციის რიცხვი უცნობია

# sum=0
# for i in range(1,10):
#     sum+=i
#     print(sum)

# i=0
# sum=0
# while i<=9:
#     i+=1
#     sum+=i
#     print(sum)

# for i in range(2,21):
#     if i%2==0:
#         print(i)


# sum=30
# while sum<70:
#     sum+=1
#     if sum%2==1:
#         print(sum)

#index არის მასივი,სია ხოლო indexing ნიშნავს სიაში კონკრეტული ასოს ადგილმდებარეობით მიგნებას


# user=int(input("enter a prime number"))
# for i in range(2,user):
#     if user%i==0:
#         print("your number is not prime")
#         break
# else:
#     print("your number is prime")


# sum=0
# num=int(input("enter a number"))
# for i in range(1,num + 1):
#     sum+=i
#     print(sum)


is_student=input("are you a student?")
age=14
if age<18:
    is_student=="no"    
    print("10% discount")


else:
    print("regular price")


#ეს flow chart მუშაობს ასე:თუ მომხმარებელი არ არის 18 წელზე ზემოთ და არ არის სტუდენტი მას 10% ფასდაკლება აქვს ხოლო თუ სტუდენტია 20% ფასდაკლება და სხვა შემთხვევაში თუ მომხმარებელი 18 წელზე ზემოთ არის მაშინ ჩვეულ ფასში იყიდის