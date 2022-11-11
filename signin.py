from exceptions import IncorrectEmailOrPassword
from hashservice import HashService

class SignIn:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def perform(self, user_email, user_password):
        user_found = self.user_repo.find_by_email(user_email)

        if user_found == None:
            raise IncorrectEmailOrPassword

        hash_service = HashService()
        check_password = hash_service.check_password(user_found.password, user_password)

        if check_password == True:
            return user_found
        else:
            raise IncorrectEmailOrPassword
