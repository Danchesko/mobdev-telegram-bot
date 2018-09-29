from src.data_manager import data_processor
from src.db_guard import db_manager
import sqlite3

 
def get_mobile_data(send_message, chat_id):
    parser = data_processor.DataProcessor()
    if(not parser.check_data_exist()):
        for messages in parser.scrape(): 
            send_message(chat_id, messages)
    return parser.load_data()


def create_db_conn(name):
    db_conn = sqlite3.connect(name)
    db_manager.create_table(db_conn)
    