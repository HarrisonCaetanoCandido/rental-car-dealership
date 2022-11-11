from exceptions import UserEmailAlreadyRegistered, InvalidPasswordError
from hashservice import HashService
from user import User

class SignUp:
    def __init__(self, user_repo):
        self.user_repo = user_repo
        # instancia o objeto hash_service sem nenhum método acionado além do __init__(self)
        self.hash_service = HashService()

    def perform(self, user_name, user_email, user_password):
        # checar se o email ja esta cadastrado
        if self.user_repo.find_by_email(user_email) != None:
            raise UserEmailAlreadyRegistered

        if invalid_password(user_password) == True:
            raise InvalidPasswordError

        # criar o hashing da senha
        hash_now = HashService()
        hashed_password = hash_now.hash_password(user_password)

        # adicionar usuario no repositorio de usuarios (banco de dados de usuarios)
        new_user = User(user_name, user_email, hashed_password)
        self.user_repo.add_user(new_user)

def invalid_password(user_password):
    # verificacao de tamanho da senha
    password_length = len(user_password)
    if password_length < 6 or password_length > 12:
        return True

    # verificacao de ao menos um caracter alfabetico maiusculo
    has_upper_letter = [c for c in user_password if c.isupper()]

    if not has_upper_letter:
        return True

    # verificacao de ao menos um caracter alfabetico minusculo
    has_lower_letter = [c for c in user_password if c.islower()]

    if not has_lower_letter:
        return True

    # verificacao de ao menos um caracter numerico
    has_numeric_character = [c for c in user_password if c.isnumeric()]

    if not has_numeric_character:
        return True

    # verificacao de ao menos um caracter especial
    has_special_character = [c for c in user_password if not c.isalnum()]

    if not has_special_character:
        return True

    return False