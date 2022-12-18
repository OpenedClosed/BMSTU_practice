sentence = input().split(', ')
dict_of_words = {}
for word in sentence:
    dict_of_words[word] = dict_of_words.get(word, 0) + 1
sorted_tuple_3_elem = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)[:3]
answer_dict = dict(sorted_tuple_3_elem)
for key, value in answer_dict.items():
    print(f'{key}: {value}')
