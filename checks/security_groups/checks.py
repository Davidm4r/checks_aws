from checks.check import Check
import boto3


class CheckClient(object):
    def __init__(self):
        self.client = boto3.client('ec2')
        self.available_checks = self.available_checks()

    @staticmethod
    def available_checks():
        return ["Check14"]

class Check14(Check):


    def title(self):
        return "Check13"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):

        client = self.client
        result = client.describe_security_groups()
        for a in result['SecurityGroups']:
            print(a)
        #print(result['SecurityGroups'])
