file = open('list_of_numbers.txt')

#View the number list
numbers = []
for number_line in file:
    number_line = number_line.strip()
    if number_line != '':
        number = int(number_line)
        numbers.append(number)

#Function to find the result
def two_numbers(number_list):
    seen = set()
    for number in number_list:
        target = 2020 - number
        if target in seen:
            return number * target
        seen.add(number) 

#Show result
result = two_numbers(numbers)
print("Product:", result)