import boto3

class DataBase:
    def __init__(self, table_name, region):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=region)
        self.table = self.dynamodb.Table('users')

    def __str__(self):
        return str(self.table)