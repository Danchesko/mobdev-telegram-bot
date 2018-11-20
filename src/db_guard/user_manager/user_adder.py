from src import constants
from src.db_guard import db_manager

def sign_in(message):
    arguments = message.text.split(" ")[1:]
    if len(arguments)!=1:
        return constants.INVALID_ARGUMENT_MESSAGE % " ".join(arguments)
    if arguments[0]==constants.BOT_PASS:
        db_manager.insert_id(message)
        return constants.LOGIN_SUCCESS
    else:
        return constants.LOGIN_FAILURE
