import string


def str_to_bool(strToConvert: string):
    if str(strToConvert).capitalize() == 'True':
        return True
    else:
        return False
