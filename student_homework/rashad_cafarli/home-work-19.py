def find_even_numbers(input_list):
    even_numbers = []
    for num in input_list:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

example_list = [1, 2, 3, 4, 5, 6, 7, 8]
netice = find_even_numbers(example_list)
print(netice)