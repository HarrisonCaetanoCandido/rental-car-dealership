class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.rent_list = None
    
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def reset_password(self, password):
        self.password = password

    def set_rent_list(self, rent_list):
        self.rent_list = rent_list