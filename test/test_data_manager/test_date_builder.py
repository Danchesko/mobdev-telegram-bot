import unittest 
from src.data_manager import date_builder
from unittest.mock import patch 


class TestDateBuilder(unittest.TestCase):
    
    def test_get_current_date(self):
        self.assertIsNotNone(date_builder.get_current_date())
        
    def test_get_file_date_name(self):
        self.assertIsNotNone(date_builder.get_file_date_name("1-1-2018.xlsx"))
        with self.assertRaises(ValueError):
           date_builder.get_file_date_name("tester")
        
    def test_current_date_for_xlsx(self):
        self.assertIsNotNone(date_builder.get_current_date_for_xlsx())
            
            
if __name__ == '__main__':
    unittest.main()