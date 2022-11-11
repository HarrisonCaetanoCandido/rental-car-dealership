from user import User
from vehicle import Vehicle
from rent import Rent
import datetime
from signup import SignUp
from signin import SignIn
from inmemoryuserrepository import InMemoryUserRepository
from exceptions import UserEmailAlreadyRegistered, IncorrectEmailOrPassword, InvalidPasswordError
import pytest

def test_user_getters_setters():
    user = User('Harrison', 'h.candido20@unifesp.br', 'Aa12345&7')

    assert user.get_name() == 'Harrison'
    assert user.get_email() == 'h.candido20@unifesp.br'
    assert user.get_password() == 'Aa12345&7'

    user.reset_password('1234577')

    assert user.get_password() == '1234577'

def test_vehicle_getters_setters():
    car = Vehicle('Dodge', 'Challenger SRT Hellcat', 'xlsx4267', 10.75, 2019)

    assert car.get_brand() == 'Dodge'
    assert car.get_model() == 'Challenger SRT Hellcat'
    assert car.get_plate() == 'xlsx4267'
    assert car.get_daily_rate() == 10.75
    assert car.get_rental_date() == ['It is avaiable', 'It is avaiable', 'It is avaiable']
    assert car.get_factory_year() == 2019

    car.set_rental_date('2022-11-05', '2022-11-08')
    assert car.get_rental_date() == [datetime.date.fromisoformat('2022-11-05'), datetime.date.fromisoformat('2022-11-08'), 3]
    assert car.get_total_value() == 37.0875

def test_rent_getters_setters():
    user = User('Harrison', 'h.candido20@unifesp.br', 'Aa12345&7')
    rent_list = Rent(user)
    car = Vehicle('Dodge', 'Challenger SRT Hellcat', 'xlsx4267', 10.75, 2019)
    rent_list.add_vehicle(car, '2022-11-05', '2022-11-08')

    assert rent_list.get_rented_vehicles() == [[car], 1]

    rent_list.remove_vehicle(car.plate)

    assert rent_list.get_rented_vehicles() == [[], 0]

def test_sign_up_password_length_verification():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)

    # less than 6 characters
    with pytest.raises(InvalidPasswordError):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'A13&7')

    # more than 12 characters
    with pytest.raises(InvalidPasswordError):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', '0000000A013&7')

def test_sign_up_password_alfabetic_verification():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)

    # upper_letters
    with pytest.raises(InvalidPasswordError):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', '0aa13&7')

    # lower_letters
    with pytest.raises(InvalidPasswordError):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', '0AA13&7')

def test_sign_up_password_special_character_verification():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)

    with pytest.raises(InvalidPasswordError):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', '0Aa13777')

def test_sign_up_user():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)
    sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'Aa12345&7')

    assert user_repo.find_by_email('h.candido20@unifesp.br') != None

def test_sign_up_user_email_already_registered():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)
    sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'Aa12345&7')

    with pytest.raises(UserEmailAlreadyRegistered):
        sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'Aa12345&7')

def test_sign_in_user():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)
    sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'Aa12345&7')

    sign_in = SignIn(user_repo)

    # aqui ele deve retornar o objeto usuário logado
    assert sign_in.perform('h.candido20@unifesp.br', 'Aa12345&7') != False

def test_sign_in_wrong_password():
    user_repo = InMemoryUserRepository()
    sign_up = SignUp(user_repo)
    sign_up.perform('Harrison Caetano Cândido', 'h.candido20@unifesp.br', 'Aa12345&7')

    sign_in = SignIn(user_repo)

    # aqui deve ser lancada uma excessao para email nao encontrado
    with pytest.raises(IncorrectEmailOrPassword):
        sign_in.perform('h.candido27@unifesp.br', 'Aa12345&7')

    # aqui deve ser lancada uma excessao para senha nao encontrada
    with pytest.raises(IncorrectEmailOrPassword):
        sign_in.perform('h.candido20@unifesp.br', '121345&7')