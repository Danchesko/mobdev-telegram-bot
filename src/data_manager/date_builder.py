import datetime

DATE_FORMAT = "%d-%m-%Y"

def get_current_date():
    return datetime.datetime.now()

def get_file_date_name(file):
    return datetime.datetime.strptime(file[:-5], DATE_FORMAT)
    
def get_current_date_for_xlsx():
    """ Create a name as a current date for saving scraped data """
    return datetime.datetime.now().strftime(DATE_FORMAT)
