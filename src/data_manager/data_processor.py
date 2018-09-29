from src import constants
from src.data_manager import data_constants
from src.data_manager import date_builder
import pandas as pd
import os
import re

class DataProcessor:
        
    def __init__(self, pars_args = data_constants.PARSERS, data_folder = data_constants.DATA_FOLDER):
        self.file_name = data_folder + date_builder.get_current_date_for_xlsx()+".xlsx"
        self.pars_args = pars_args
        self.phones = []   
        
    def check_data_exist(self):
        return os.path.exists(self.file_name)
    
    def load_data(self):
        return open(self.file_name, 'rb')
    
    def scrape(self):
        for parser, page_name in self.pars_args.items():
            try:
                yield(constants.PARSING_MESSAGE%parser)
                site_phones = pd.DataFrame(page_name.get_phones()).transpose()
                yield(constants.PARSE_FINISHED_MESSAGE % str(site_phones.shape[0]))
                site_phones[constants.Phone.SHOP] = parser
                self.phones.append(site_phones) 
            except Exception:
                yield(constants.ERROR_MESSAGE)
        self.save_data()
            
    def save_data(self):
        writer = pd.ExcelWriter(self.file_name)
        self.clean_data(pd.concat(self.phones)).to_excel(writer, 'Sheet1')
        writer.save()
        
    def clean_data(self, data):
        data = data.copy()
        data = data[data[constants.Phone.PRICE]!="\xa0"]
        for index, row in data.iterrows():
            try:
                matcher = re.match('[0-9, ]+',row[constants.Phone.PRICE])
                row[constants.Phone.PRICE]=matcher.group(0).replace(" ", "").replace(",", "")
            except Exception:
                continue
        return data