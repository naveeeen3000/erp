"""Custom exceptions."""
class PasswordsDontMatchException(Exception):
    
    def __init__(self,message):
        super().__init__(message)


class InvalidBooleanStringException(Exception):
    
    def __init__(self,message):
        super().__init__(message)
