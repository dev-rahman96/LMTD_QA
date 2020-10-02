import os
import unittest



class BasicTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    def api_test(self):
        pass
    
    def test_login(self, username, password):
        """Login helper function."""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

# self.assertEqual(response.data, b'Hello, World!')    
 
test1 = BasicTestCase()
# test1.test_index()
test1.test_login()

    
if __name__ == '__main__':
    unittest.main()