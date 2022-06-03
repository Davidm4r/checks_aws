from checks.check import Check
import boto3


class CheckClient(object):
    def __init__(self, region=""):
        if region:
            self.client = boto3.client('ec2')
        else:
            self.client = boto3.client('ec2', region=region)
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
        #result = client.describe_security_groups()
        result = client.describe_regions()
        #for a in result['SecurityGroups']:
        #    print(a)
        #print(result['SecurityGroups'])
        print(result)
