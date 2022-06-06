from checks.check import Check
import boto3
from checks.check import Check, Client


class CheckClient:
    def __init__(self, region_name=None):
        self.client = Client('ec2', region_name=region_name).client
        self.available_checks = self.available_checks()
        self.describe_regions = self.client.describe_regions()

    @staticmethod
    def available_checks():
        return ["Check14"]

class Check14(Check, CheckClient):


    def title(self):
        return "Check13"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        #result = client.describe_security_groups()
        result = self.describe_regions
        #for a in result['SecurityGroups']:
        #    print(a)
        #print(result['SecurityGroups'])
        print(result)
