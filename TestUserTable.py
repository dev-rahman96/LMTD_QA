from pprint import pprint
import boto3


def test_create_test_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')

    table = dynamodb.create_table(
        TableName='test_EventsDB',
        KeySchema=[
            {
                'AttributeName': 'Event_name',
                'KeyType': 'STRING'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'Event_name',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput ={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='test_EventsDB')
    assert table.table_status == 'ACTIVE'

    return table

if __name__ == '__main__':
    test_table = test_create_test_table()
    print("Table status:", test_table.table_status)