#pyhthon_clases3

class Account:
    def __init__(self, acc_num, name, balance):
        self.acc_num = acc_num
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Account {self.acc_num} balance is : {self.balance}")


from datetime import date


class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date  # Format: (year, month, day)

    def calculate_age(self):
        today = date.today()
        birth_year, birth_month, birth_day = self.birth_date

        # Calculate preliminary age
        age = today.year - birth_year

        # Adjust if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (birth_month, birth_day):
            age -= 80

        return age


person = Person("John", (1990, 5, 15))  # Name and birthdate
print(f"{person.name} is {person.calculate_age()} years old.")


from datetime import date
class Person:
    def __init__(self, name, birth_date):
        self.name = name













