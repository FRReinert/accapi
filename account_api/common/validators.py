import datetime
import re


class InvalidEmail(ValueError):
    pass


class InvalidPhone(ValueError):
    pass


class DuplicatedValue(ValueError):
    pass


class InvalidBirthday(ValueError):
    pass


class InvalidDocument(ValueError):
    pass


def is_document_valid(value: str) -> bool:
    '''Validate Personal ID'''

    # clear masks
    if value.isdigit() == False:
        raise InvalidDocument('Apenas numeros sao aceitos')

    # Validate document length
    if len(value) != 11:
        raise InvalidDocument('Deve ter 11 caracteres')

    # reverse doc and compare with original
    # If its equal, means its not valid
    if value == value[::-1]:
        raise InvalidDocument('Nao pode conter todos os digitos iguais')

    # validat 1st digit
    sum_result = 0
    for i in range(1, 10):
        idx = i-1
        sum_result += int(value[idx]) * i
    mod_result = sum_result % 11
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

    return True

def is_user_older_then_eighteen(value: str) -> bool:
    '''Is user older then eighteen'''

    today = datetime.date.today()
    eighteen_years = datetime.timedelta(days=(365.24 * 18))
    
    mininum_date_accepted = today - eighteen_years
    
    try:
        informed_date = datetime.datetime.strptime(value, '%d/%m/%Y').date()
    except Exception:
        raise InvalidBirthday('Utilize o formato DD/MM/YYYY')

    if informed_date > mininum_date_accepted:
        raise InvalidBirthday('Idade nao autorizada')

    return True

def is_email_valid(value: str) -> bool:
    '''Validate email'''

    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    re.search(regex, value)

    if not re.search(regex, value):
        raise InvalidEmail('Formato invalido')

    return True

def is_phone_valid(value: str) -> bool:
    '''Validate Phone'''

    if ' ' in value:
        raise InvalidPhone('Informar telefone sem espacos')

    if value.isdigit() == False:
        raise InvalidPhone('Informar apenas numeros')

    regex = r"^[0-9]{2,3}[0-9]{2,3}[0-9]{8,9}$"
    re.search(regex, value)

    if not re.search(regex, value):
        raise InvalidPhone('utilize o  padrao "xxxyyyzzzzzzzz"')
    
    return True

def unique_field_valid(model_manager, field_name: str, value: str, *extra_args) -> bool:
    '''Verify if value already exist in a specifc collection'''

    model_doc: list = model_manager.filter(field_name,'==', value)
    if len(model_doc) > 0:
        raise DuplicatedValue(f'{field_name} ja cadastrado')
    
    return True
