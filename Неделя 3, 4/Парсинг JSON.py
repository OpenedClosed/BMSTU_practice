import json


def mean_age(json_string):
    py_obj = json.loads(json_string)
    ages = list(map(lambda x: x['age'], py_obj))
    sum_age = sum(ages)
    amount_of_people = len(py_obj)
    return json.dumps({'mean_age': sum_age/amount_of_people})


if __name__ == "__main__":
    json_string = '''[
        {
            "name": "Петр",
            "surname": "Петров",
            "patronymic": "Васильевич",
            "age": 23,
            "occupation": "ойтишнек"
        },
        {
            "name": "Василий",
            "surname": "Васильев",
            "patronymic": "Петрович",
            "age": 24,
            "occupation": "дворник"
        }
    ]'''

    print(mean_age(json_string))