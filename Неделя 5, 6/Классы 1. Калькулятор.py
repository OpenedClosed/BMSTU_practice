class Calculator:

    last = None
    def __init__(self):
        self.log = []
    
    def sum(self, a, b):
        res = a + b
        log_record = f'sum({a}, {b}) == {res}'
        self.log.append(log_record)
        Calculator.last = log_record
        return res

    def sub(self, a, b):
        res = a - b
        log_record = f'sub({a}, {b}) == {res}'
        self.log.append(log_record)
        Calculator.last = log_record
        return res

    def mul(self, a, b):
        res = a * b
        log_record = f'mul({a}, {b}) == {res}'
        self.log.append(log_record)
        Calculator.last = log_record
        return res

    def div(self, a, b, mod=False):
        if mod:
            res = a % b
        else:
            res = a / b
        if type(res) is float:
            log_record = f'div({a}, {b}) == {res:.1f}'
        else:
            log_record = f'div({a}, {b}) == {res}'
        self.log.append(log_record)
        Calculator.last = log_record
        return res

    def history(self, n):
        if n <= len(self.log):
            return self.log[(len(self.log) - n)]
        return None

    @classmethod
    def clear(cls):
        cls.last = None

if __name__ == "__main__":
    a = Calculator()
    b = Calculator()
    a.sum(8, 9)
    a.sum(100, 41)
    a.div(20, 9)
    a.mul(6, 7)
    b.div(7, 3)
    print(a.last)
    print(b.last)
    print(Calculator.last)