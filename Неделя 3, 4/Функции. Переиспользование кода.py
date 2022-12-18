def get_balance(name, transactions) -> int:
    current_balance = [
        (x["amount"]) for x in transactions if x["name"] == name
    ]
    return sum(current_balance)


def count_debts(names, amount, transactions) -> dict:
    debt_dict = dict(
        (name, (lambda x: 0 if x > 0 else abs(x))(
            get_balance(name, transactions) - amount
        )) for name in names
    )
    return debt_dict
    

if __name__ == "__main__":
    transactions = [
        {"name": "Василий", "amount": 500},
        {"name": "Петя", "amount": 100},
        {"name": "Василий", "amount": -300},
    ]
    print(get_balance("Василий", transactions))
    print(count_debts(["Василий", "Петя", "Вова"], 150, transactions))

