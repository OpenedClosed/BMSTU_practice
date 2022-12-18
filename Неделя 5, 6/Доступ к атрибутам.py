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

    def __getattr__(self, attr):
        attr = ''.join(sorted(list(str(x) for x in attr))).lower()
        return self[attr]

    def __setattr__(self, name, value):
        new_name = ''.join(sorted(list(str(x) for x in name))).lower()
        if pattern.match(new_name):
            self[new_name] = value
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        new_name = ''.join(sorted(list(str(x) for x in name))).lower()
        if pattern.match(new_name):
            self[new_name] = None
        else:
            del self.__dict__[name]

if __name__ == "__main__":
    field = Field()
    field.B2 = 26
    print(field)
    print(field['b', 2])
