from pprint import pprint
import boto3

def create_test_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    table = dynamodb.create_table(
        TableName='Events',
        KeySchema=[
            {
                'AttributeName': 'Event_name',
                'KeyType': 'STRING'
            },
            {
                'AttributeName': 'Event_date',
                'KeyType': 'STRING'
            },
            {
                'AttributeName': 'Event_time',
                'KeyType': 'STRING'
            },
             {
                'AttributeName': 'User',
                'KeyType': 'STRING'
            },
             {
                'AttributeName': 'Event_desc',
                'KeyType': 'STRING'
            },
             {
                'AttributeName': 'Event_image',
                'KeyType': 'STRING'
            },
             {
                'AttributeName': 'Event_location',
                'KeyType': 'STRING'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Event_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Event_date',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Event_time',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'User',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Event_desc',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Event_image',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'Event_location',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput ={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='Events')
    assert table.table_status == 'ACTIVE'

    return table

if __name__ == '__main__':
    test_table = create_test_table()
    print("Table status:", test_table.table_status)