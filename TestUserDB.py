from pprint import pprint
import unittest
import boto3
from botocore.exceptions import ClientError
from moto import mock_dynamodb2

@mock_dynamodb2
class TestDatabaseFunctions(unittest.TestCase):
    
    def setUp(self):
        """Create the mock database and table"""
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        
        from TestUserTable import test_create_test_table
        self.table = test_create_test_table(self.dynamodb)
        
    def tearDown(self):
        """Delete mock database and table after test is run"""
        self.table.delete()
        self.dynamodb=None 
        
    def testTable(self):
        self.assertTrue(self.table) # check if we got a result
        self.assertIn('test_userdevbops', self.table.name) # check table name
        pprint(self.table.name)
        
        

if __name__ == '__main__':
    unittest.main()