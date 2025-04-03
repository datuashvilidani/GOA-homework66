#ფუნქციები გვჭირდება დროის დაზოგვაში,კოდის გამარტივებისთვის და არ გვიწევს ერთი და იგივეს წერა ბევრჯერ

# def double_values(input_list):
#     result=[]
#     for i in input_list:
#         result.append(i*2)
#     return result
# print(double_values([1,5,6,8,2,4]))


# შექმენით ფუნქცია, რომელსაც არგუმენტად გადასცემთ სიას (ჩათვალეთ, რომ სიაში ინახება Integer-ი რიცხვები). ამ ფუნქციამ საბოლოოდ უნდა დააბრუნოს სიიდან მხოლოდ ლუწი რიცხვები.

# def even(num):
#     result=[]
#     for i in num:
#         if i % 2 ==0:
#             result.append(i)
#     return(result)
    


# print(even([1,5,6,8,2,7]))


# შექმენით ფუნქცია და გადაეცით არგუმენტად სია. ფუნქციამ უნდა დააბრუნოს ახალი სია, რომლის თითოეული ელემენტიც უნდა იყოს კვადრატში აყვანილი.

# def multiply(numbers):
#     result=[]
#     for i in numbers:
#         result.append(i**2)
#     return result

# print(multiply([2,6,7,9,10]))

# შექმენით ფუნქცია და არგუმენტად გადაეცით String-ი. ფუნქციამ ეგრედწოდებულად უნდა "გაფილტროს" ეს სტრინგი თანხმოვანი ასოებისგან და მხოლოდ დააბრუნოს ის ხმოვანი ასოები, რომლებსაც ეს სტრინგი შეიცავს.

# def strings(words):
#     just=""
#     for i in words:
#         if i in "aeiou":
#             just+=i
#     return(just)

# print(strings("adamiani"))

# def numbers(numlist):
#     result=[]
#     for i in numlist:
#         if i <0:
#             result.append(i)
#     return result

# print(numbers([1,5,6,8,-1,-6,-8]))



# def numbers(numlist):
#     result=[]
#     for i in numlist:
#         if i >0:
#             result.append(i)
#     return result

# print(numbers([1,5,6,8,-1,-6,-8]))

# def multiply(numbers):
#     return numbers **2 * 10

    
# print(multiply(5))

# def two_nums(x,y):
#     return x **y

# print(two_nums(2,3))