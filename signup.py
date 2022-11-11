from exceptions import UserEmailAlreadyRegistered
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

        # criar o hashing da senha
        hash_now = HashService()
        hashed_password = hash_now.hash_password(user_password)

        # adicionar usuario no repositorio de usuarios (banco de dados de usuarios)
        new_user = User(user_name, user_email, hashed_password)
        self.user_repo.add_user(new_user)