from classes.Email import Email
from classes.Name import Name
from classes.Phone import Phone
from helpers.error import PhoneValueError


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

        self.birthdays = None
        self.address = None
        self.email = None

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def remove_phone(self, phone):
        phone = Phone(phone)
        if phone in self.phones:
            self.phones.remove(phone)

    def find_phone(self, phone_number):
        phone = None
        for p in self.phones:
            if p.value == phone_number:
                phone = p
                break
        return phone

    def edit_phone(self, old_phone, new_phone):
        if len(new_phone) != 10 or not new_phone.isdigit():
            raise PhoneValueError("New number must contain 10 digits.")

        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone
        else:
            raise PhoneValueError("Phone is not in the address book.")

    def add_email(self, email):
        self.email = Email(email)

    def __str__(self):
        result = f"Contact name: {self.name.value}, phones: {', '.join(p.value for p in self.phones)}"

        if self.email:
            result += f", email: {str(self.email)}"

        return result
