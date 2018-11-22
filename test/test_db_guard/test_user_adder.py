import unittest 
from src.db_guard.user_manager import user_adder


class TestUserAdder(unittest.TestCase):
    
    def test_sign_in(self):
        class TestMessage():
            text = ''
        message = TestMessage()
        message.text = '\login wrong_password'
        self.assertEqual(user_adder.sign_in(message), 'Password is incorrect')
        message.text = '\login wrong input'
        self.assertEqual(user_adder.sign_in(message), 'Invalid arguments: "wrong input"')
        

            
if __name__ == '__main__':
    unittest.main()