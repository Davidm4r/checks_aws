from checks.check import Check
import boto3


class SecurityGroupsCheck(object):
    def __init__(self):
        self.client = boto3.client('ec2')


class Check14(Check):


    def title(self):
        return "Check13"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):

        client = self.client = boto3.client('ec2')
        result = client.describe_security_groups()
        for a in result['SecurityGroups']:
            print(a)
        #print(result['SecurityGroups'])
