def lists_sum(*args, unique=False):
    if unique == False:
        result_collection = [*map(lambda x: sum(x), args)]
    else:
        result_collection = set([*map(lambda x: sum(set(x)), args)])
    return sum(result_collection)

if __name__ == "__main__":
    print(lists_sum([1, 1], [1], [1, 2, 3]))
    print(lists_sum([1, 1, 1], [1, 1], unique=True))
