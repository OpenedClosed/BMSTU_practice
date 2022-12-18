import re

pattern = re.compile(r'^(\d+[a-z])$|^([a-z]\d+)$')


class Field(dict):
    def check_the_key(self, key):
        if not pattern.match(key):
            raise ValueError('Неверный тип')

    def __getitem__(self, key):
        key = ''.join(sorted(list(str(x) for x in key))).lower()
        self.check_the_key(key)
        return super(Field, self).__getitem__(key)

    def __setitem__(self, key, value):
        key = ''.join(sorted(list(str(x) for x in key))).lower()
        self.check_the_key(key)
        super(Field, self).__setitem__(key, value)

    def __delitem__(self, key):
        key = ''.join(sorted(list(str(x) for x in key))).lower()
        super(Field, self).__delitem__(key)

    def __missing__(self, key):
        return None

    def __contains__(self, item):
        return self[item] != self.__missing__(1)

    def __iter__(self):
        return iter(self.values())

if __name__ == "__main__":
    field = Field()
    field[1, 'A'] = 5
    field['b25'] = 6
    field['b28'] = 7
    print(field)
    print(field["1A"] is None)
    print((1, 'a') in field)
    print("A1" in field)
    print(('D', '4') in field)
    for i in field:
        print(i)
