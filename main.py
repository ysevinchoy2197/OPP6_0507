# 6
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.__password = password

    def login(self, pw):
        print(f"password: {self.__password}")

    def change_password(self, old, new):
        self.__password = old
        self.__password = new

    def info(self):
        print(f"username: {self.username}, email: {self._email}, password: {self.__password}")


u1 = User("@jemfur.", "jemfur696@gamil.com", "IUM-2797")

u1.username("@jemfur.")
u1.change_password("IUM-2797", "POH-7354")
u1.info()
