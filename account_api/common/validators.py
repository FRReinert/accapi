import datetime
import re


class InvalidEmail(ValueError):
    pass


class InvalidPhone(ValueError):
    pass


class EmailAlreadyEnrolled(ValueError):
    pass


class InvalidBirthday(ValueError):
    pass


class InvalidDocument(ValueError):
    pass


def validate_personal_id(func) -> bool:
    '''Validate Personal ID'''

    def wrap(value: str):
        # clear masks
        if value.isdigit() == False:
            raise InvalidDocument('Apenas numeros sao aceitos')

        # Validate document length
        if len(value) != 11:
            raise InvalidDocument('Documento deve ter 11 caracteres')

        # reverse doc and compare with original
        # If its equal, means its not valid
        if value == value[::-1]:
            raise InvalidDocument('Documento nao pode conter todos os digitos iguais')

        # validat 1st digit
        sum_result = 0
        for i in range(1, 10):
            idx = i-1
            sum_result += int(value[idx]) * i
        mod_result = sum_result % 11
        print(mod_result)
        expected_digit_one = 0 if mod_result == 10 else mod_result
        if int(value[9]) != expected_digit_one:
            raise InvalidDocument('Digito verificador incorreto')

        # validat 2st digit
        sum_result = 0
        for i in range(1, 11):
            idx = i-1
            sum_result += int(value[idx]) * idx
        mod_result = sum_result % 11
        expected_digit_two = 0 if mod_result == 10 else mod_result
        if int(value[10]) != expected_digit_two:
            raise InvalidDocument('Digito verificador incorreto')

        return value

    return wrap


def is_user_older_then_eighteen(func):
    '''Is user older then eighteen'''

    def wrap(value: str):
        today = datetime.date.today()
        eighteen_years = datetime.timedelta(days=(365.24 * 18))
        
        mininum_date_accepted = today - eighteen_years
        informed_date = datetime.datetime.strptime(value, '%d/%m/%Y').date()

        if informed_date > mininum_date_accepted:
            raise InvalidBirthday('Idade nao autorizada')

        return value

    return wrap


def is_email_valid(func):
    '''Validate email'''

    def wrap(value: str) -> str:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        re.search(regex, value)

        if not re.search(regex, value):
            raise InvalidEmail('E-mail invalido')
        return value

    return wrap


def is_phone_valid(func):
    '''Validate Phone'''

    def wrap(value: str) -> str:

        if ' ' in value:
            raise InvalidPhone('Informar telefone sem espacos')

        if value.isdigit() == False:
            raise InvalidPhone('Informar apenas numeros')

        regex = r"^[0-9]{2,3}[0-9]{2}[0-9]{9}$"
        re.search(regex, value)

        if not re.search(regex, value):
            raise InvalidPhone('Telefone invalido, utilize o  padrao "xxxyyyzzzzzzzz"')
        return value

    return wrap
