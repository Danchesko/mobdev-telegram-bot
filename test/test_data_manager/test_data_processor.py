import pandas as pd
import unittest
from unittest.mock import patch 

from src.data_manager import data_processor
from pandas.util.testing import assert_frame_equal


class TestDataProcessor(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_class = data_processor.DataProcessor(pars_args=['test_args'], data_folder='testfolder/')
        
    
    def test_clean_data(self):
        test_df = pd.DataFrame({'Название телефона' : ["Apple 5"], 'Цена' : ['10,000$'],"Магазин":["kivano"],'Index':['apple5']}).set_index('Index')
        assert_frame_equal(pd.DataFrame({'Название телефона' : ["Apple 5"], 'Цена' : ['10000'],
                                       "Магазин":["kivano"],'Index':['apple5']}).set_index('Index'), self.test_class.clean_data(test_df))
    
        test_df = pd.DataFrame({'Название телефона' : ["Apple 5"], 'Цена' : ['test_price'],"Магазин":["kivano"],'Index':['apple5']}).set_index('Index')
        assert_frame_equal(pd.DataFrame({'Название телефона' : ["Apple 5"], 'Цена' : ['test_price'],
                                       "Магазин":["kivano"],'Index':['apple5']}).set_index('Index'), self.test_class.clean_data(test_df))


    def test_scrape(self):
        with patch('src.data_manager.data_processor.DataProcessor.scrape') as mock_scrape:
            mock_scrape.return_value = True
        self.assertTrue(self.test_class.scrape())


if __name__ == "__main__":
    unittest.main()