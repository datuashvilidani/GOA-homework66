# name="Danieli"
# print(name[1]);print(name[3]);print(name[4])

#False Strings are immutable and lists are mutable

#იმიტომ რომ სტრინგს არ შეუძლია შეიცვალოს ხოლო ლისტებს შეგვიძლია "მოდიფიკაცია" გავუკეთოთ 


empty=[]

for i in range(8):
    userinput=input("Enter your name,surname,age,birthday,height,haircolor,eyecolor,birthplace ")
    empty.append(userinput)
print(empty)