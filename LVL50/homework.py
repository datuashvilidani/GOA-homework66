# კომენტარების სახით ახსენით მოცემული კოდი
def sort_array(source_array):
    odd_numbers = [] #აქ არი ცარიელი კენტი რიცხვების სია      
    result = [] #აქ არის საბოლოო ჯამში დაგროვებული სია
    index = 0 #ეს არის index count
    
    for num in source_array:  #აქ ვატრიალებთ for loop-ს და if-ის საშუალებით ვიგებთ ეს რიცხვი ლუწია თუ კენტი,თუ კენტია მაშინ ავიტანოთ odd_numbers-ში
        if num % 2 != 0:
            odd_numbers.append(num)
    
    odd_numbers.sort(); # აქ odd_numbers ზრდადობის მიხედვით ვალაგებთ
    
    for num in source_array: #აქ გადმოვდივართ საბოლოო ჯამში დათვლაზე ანალოგიური ხერხის საშუალებით მაგრამ ამჯერად index ემატება 1 
        if num % 2 != 0:
            result.append(odd_numbers[index])
            index += 1
        else:
            result.append(num)
    
    return result #გამოვიტანოთ საბოლოო ჯამი


print(sort_array(1235))
