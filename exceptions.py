class UserEmailAlreadyRegistered(Exception):
    "Email já utilizado em alguma outra conta registrada no banco de dados de usuários"
    pass

class IncorrectEmailOrPassword(Exception):
    "O email recebido não está registrado ou a senha não foi encontrada no banco de usuários"
    pass

class InvalidPasswordError(Exception):
    "Senha inválida, não atende a pelo menos um dos requisitos mínimos (tamanho, caracter especial, caracter alfabetico ou caracter numerico)"
    pass