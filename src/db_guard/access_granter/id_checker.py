from src.data_manager.date_builder import get_current_date
from src.db_guard import db_manager

def check_id(user_id):
    user = db_manager.search_id(user_id)
    print(user, end = " ")
    print(get_current_date())
    return user is not None
    