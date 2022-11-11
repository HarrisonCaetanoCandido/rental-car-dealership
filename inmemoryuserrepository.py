# a intenção é simular um banco de usuários
class InMemoryUserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, email):
        pass

    def find_by_email(self, email):
        for item in self.users:
            if item.email == email:
                return item