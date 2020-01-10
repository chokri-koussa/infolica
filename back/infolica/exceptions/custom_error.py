class CustomError(Exception):
    # General constants
    GENERAL_EXCEPTION = 'An error occured while executing the query'
    ID_NOT_FOUND_EXCEPTION = 'Id not found'
    USER_NOT_FOUND_EXCEPTION = 'User not found'
    NOT_AUTHORIZED_EXCEPTION = 'Not authorized'
    RECORD_WITH_ID_NOT_FOUND = '{} with id {} not found'

    pass