import os
import shutil
import unittest
import datetime
import pandas as pd
from src.data_manager import data_manipulator
from pandas.util.testing import assert_frame_equal

class TestDataManipulator(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.first_df = pd.DataFrame({'Название телефона' : ["Apple 5", "Samsung Galaxy S6", "OnePlus 6t"], 
                               'Цена' : [10000, 12000, 8000],
                               "Магазин":["kivano","svetofor","mostovoy"],
                               'Index':['apple5','samsung-galaxy-s6','oneplus6t']
                               }).set_index('Index')
        cls.second_df = pd.DataFrame({'Название телефона' : ["Apple 8", "Samsung Galaxy S6", "OnePlus 6t"], 
                               'Цена' : [30000, 14000, 8000],
                               "Магазин":["kivano","svetofor","mostovoy"],
                               'Index':['apple8','samsung-galaxy-s6','oneplus6t']}).set_index('Index')
    
        os.mkdir('testfolder')
        
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        day_before = (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%d-%m-%Y")
        
        writer = pd.ExcelWriter('testfolder/' + current_date +".xlsx")
        cls.first_df.to_excel(writer, sheet_name = "Sheet1")
        writer.save()
        
        writer2 = pd.ExcelWriter('testfolder/' + day_before +".xlsx")
        cls.second_df.to_excel(writer, sheet_name = "Sheet1")
        writer2.save()
        
         
    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('testfolder')
    
    
    def test_show_archive(self):
        self.assertEqual(sorted(data_manipulator.show_archive(data_folder="testfolder/")), 
                         sorted([datetime.datetime.now().strftime("%d-%m-%Y")+'.xlsx',
                                 (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%d-%m-%Y")+'.xlsx']))
    
        self.assertNotEqual(sorted(data_manipulator.show_archive(data_folder="testfolder/")), 
                         sorted([datetime.datetime.now().strftime("%d-%m-%Y") + '.xlsx', 
                          (datetime.datetime.now() - datetime.timedelta(days = 5)).strftime("%d-%m-%Y")+'.xlsx']))  
    
        
        
    def test_check_arguments(self):
        test_arguments = ["test","test2","test3"]
        self.assertEqual(data_manipulator.check_arguments(test_arguments, "testfolder/"),
                         'Invalid arguments: "%s"' % (" ".join(test_arguments)))
        
        self.assertEqual(data_manipulator.check_arguments(test_arguments[1:], "testfolder/"),
                         r"Unable to find given documents in /archive, please check your arguments on validity")
        
        self.assertIsNone(data_manipulator.check_arguments(sorted([datetime.datetime.now().strftime("%d-%m-%Y"),
                                 (datetime.datetime.now() - datetime.timedelta(days = 1)).strftime("%d-%m-%Y")]),"testfolder/"))
    
    
    def test_analyze_datasets(self):
        test_new = pd.DataFrame({'Название телефона' : ["Apple 5"], 'Цена' : [10000],"Магазин":["kivano"],'Index':['apple5']}).set_index('Index')
        test_old = pd.DataFrame({'Название телефона' : ["Apple 8"], 'Цена' : [30000],"Магазин":["kivano"],'Index':['apple8']}).set_index('Index')
        test_price_changed = pd.DataFrame({'Название телефона' : ["Samsung Galaxy S6"], 'Цена' : [12000],'Измененная цена':[14000],
                                           "Магазин":["svetofor"],'Index':['samsung-galaxy-s6']}).set_index('Index')
        analyzed_datasets = data_manipulator.analyze_datasets(self.first_df, self.second_df)
        assert_frame_equal(analyzed_datasets[0], test_new)
        assert_frame_equal(analyzed_datasets[1], test_old)
        assert_frame_equal(analyzed_datasets[2], test_price_changed)


        
if __name__ == "__main__":
        unittest.main()