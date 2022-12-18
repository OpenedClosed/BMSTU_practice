def get_popular_name_from_file(filename):
    counter = {}
    with open(filename) as f:
        for line in f:
            line_list = line.split()
            counter[line_list[0]] = counter.get(line_list[0], 0) + 1
    max_value = max(counter.values())
    answer_list = [name for name in counter if counter[name] == max_value]
    answer = ', '.join(answer_list)
    return answer

if __name__ == "__main__":
    print(get_popular_name_from_file('file.txt'))