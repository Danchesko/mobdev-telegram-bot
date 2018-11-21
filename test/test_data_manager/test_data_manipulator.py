import os
import shutil
import unittest
import datetime
import pandas as pd
from unittest.mock import patch
from src.data_manager import data_manipulator

class TestDataManipulator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        first_df = pd.DataFrame({'Название телефона' : ["Apple 5", "Samsung Galaxy S6", "OnePlus 6t"], 
                               'Цена' : [10000, 12000, 8000],
                               "Магазин":["kivano","svetofor","mostovoy"],
                               'Index':['apple5','samsung-galaxy-s6','oneplus6t']
                               }).set_index('Index')
        second_df = pd.DataFrame({'Название телефона' : ["Apple 8", "Samsung Galaxy S6", "OnePlus 6t"], 
                               'Цена' : [30000, 14000, 8000],
                               "Магазин":["kivano","svetofor","mostovoy"],
                               'Index':['apple8','samsung-galaxy-s6','oneplus6t']}).set_index('Index')
    
        os.mkdir('test')
        
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        day_before = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%d-%m-%Y")
        
        writer = pd.ExcelWriter('test/' + current_date +".xlsx")
        first_df.to_excel(writer, sheet_name = "Sheet1")
        writer.save()
        
        writer2 = pd.ExcelWriter('test/' + day_before +".xlsx")
        second_df.to_excel(writer, sheet_name = "Sheet1")
        writer2.save()
        
        
        
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('test')
    
#    
#    def setUp(self):#starts with every test
#        pass
#    
#    def tearDown(self):
#        pass

    
    def test_show_archive(self):
        self.assertEqual(sorted(data_manipulator.show_archive(data_folder="test/")), 
                         sorted([datetime.datetime.now().strftime("%d-%m-%Y")+'.xlsx',
                                 (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%d-%m-%Y")+'.xlsx']))
    
        self.assertNotEqual(sorted(data_manipulator.show_archive(data_folder="test/")), 
                         sorted([datetime.datetime.now().strftime("%d-%m-%Y") + '.xlsx', 
                          (datetime.datetime.now() - datetime.timedelta(days = 5)).strftime("%d-%m-%Y")+'.xlsx']))  
    
        with patch('os.listdir') as mocked_list_dir:
            mocked_list_dir.return_value = ["21-11-2018.xlsx", "20-11-2018.xlsx"]
            self.assertEqual(data_manipulator.show_archive(),  ["21-11-2018.xlsx", "20-11-2018.xlsx"])
        
        
        
    
#    def test_compare_data(self):
#        self.assertEqual(data_manipulator.compare_data('))
#        
        
        
if __name__ == "__main__":
        unittest.main()