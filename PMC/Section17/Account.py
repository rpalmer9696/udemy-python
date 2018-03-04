class Account:
    def __init__(self, file_path):
        self.file_handler = FileHandler(file_path)
        self._balance = self.file_handler.read()

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        self._balance = float(self._balance) - amount
        self.commit()

    def deposit(self, amount):
        self._balance = float(self._balance) + amount
        self.commit()

    def commit(self):
        self.file_handler.write(str(self._balance))


class Checking(Account):
    def __init__(self, file_path, fee):
        super().__init__(file_path)
        self.fee = fee

    def transfer(self, amount):
        self._balance = float(self._balance) - (amount + self.fee)
        self.commit()


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def write(self, value):
        with open(self.file_path, 'w') as file:
            file.write(value)
