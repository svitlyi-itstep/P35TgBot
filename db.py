import boto3


class DataBase:
    def __init__(self, table_name, region):
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=region)
        self.table = self.dynamodb.Table(table_name)

    def __str__(self):
        return str(self.table)

    def put_item(self, item: dict):
        self.table.put_item(
            Item=item
        )