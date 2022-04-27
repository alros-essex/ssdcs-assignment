'''Exceptions raised in the application'''

class AuthorizationException(Exception):
    '''The user is not authorized'''

    def __str__(self) -> str:
        return 'AuthorizationException'

class DbIntegrityError(Exception):
    '''Integrity violation on db'''

    def __str__(self) -> str:
        return 'DbIntegrityError'

class InvalidArgument(Exception):
    '''The input is invalid'''

    def __str__(self) -> str:
        return 'InvalidArgument'