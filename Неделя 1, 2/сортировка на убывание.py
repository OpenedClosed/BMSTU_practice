list_of_numbers = []
while len(list_of_numbers) < 5:
    number = int(input())
    list_of_numbers.append(number)
sort_rev_list = sorted(list_of_numbers, reverse=True)
str_sort_rev_list = list(map(str, sort_rev_list))
print('\n'.join(str_sort_rev_list))