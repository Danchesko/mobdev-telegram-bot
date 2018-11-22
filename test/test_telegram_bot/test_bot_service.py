import unittest
from src.telegram_bot import bot_service
from unittest.mock import patch 



class TestBotService(unittest.TestCase):
    
    def test_get_mobile_data(self):
         with patch('src.telegram_bot.bot_service.get_mobile_data') as mock_scrape:
            mock_scrape.return_value = True
            self.assertTrue(bot_service.get_mobile_data)
            
            
if __name__ == '__main__':
    unittest.main()