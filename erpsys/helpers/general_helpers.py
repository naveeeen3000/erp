"""General helper functions."""
from erpsys.helpers.custom_exceptions import InvalidBooleanStringException

def to_bool(value):
    bools = ['true','false']
    val = str(value)
    if val in bools:
        if val.lower() == 'true':
            return True
        else:
            return False
        
    else:
        raise InvalidBooleanStringException("Invalid Boolean String")