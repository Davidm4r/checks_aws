from checks.check import Check
import boto3
import datetime
from colorama import Fore, Style
'''
iam-administrator-access-with-mfa
iam-assume-role-no-mfa
iam-assume-role-policy-allows-all-principals
iam-avoid-root-usage
iam-check-saml-providers-sts
iam-customer-managed-policy-least-privilege
iam-customer-managed-policy-not-allow-decrypt-reencrypt
iam-disable-30-days-credentials
iam-disable-90-days-credentials
iam-enable-access-analyzer
iam-external-role-with-mfa-external-id
iam-group-inline-policy-least-privilege
iam-group-not-empty
iam-inline-policy-allows-non-sts-action
iam-inline-policy-allows-NotActions
iam-inline-policy-least-privilege
iam-instance-profile-attached
iam-log-metric-filter-authentication-failures
iam-log-metric-filter-policy-changes
iam-log-metric-filter-root-usage
iam-log-metric-filter-sign-in-without-mfa
iam-log-metric-filter-unauthorized-api-calls
iam-managed-policy-allows-full-privileges
iam-managed-policy-allows-non-sts-action
iam-managed-policy-allows-NotActions
iam-no-custom-policy-permissive-role-assumption
iam-no-root-access-key
iam-no-root-certificates
iam-no-server-certificates-stored
iam-no-service-user-with-password
iam-password-policy-expires-90-days
iam-password-policy-lowercase
iam-password-policy-minimum-length-14
iam-password-policy-number
iam-password-policy-reuse-24
iam-password-policy-symbol
iam-password-policy-uppercase
iam-policy-attached-only-to-group-or-roles
iam-policy-no-administrative-privileges
iam-principals-not-allow-decrypt-reencrypt
iam-role-inline-policy-least-privilege
iam-role-with-inline-policy
iam-root-hardware-mfa-enabled
iam-root-mfa-enabled
iam-rotate-access-key-90-days
iam-support-role-created
iam-user-mfa-enabled
iam-user-mfa-enabled-console-access
iam-user-no-inline-policy
iam-user-no-managed-policy
iam-user-no-setup-initial-access-key
iam-user-not-in-group
iam-user-two-active-access-key
iam-user-with-password-and-key
iam-policy-allows-privilege-escalation
'''

class CheckClient():
    def __init__(self, region=""):
        if region:
            self.client = boto3.client('iam')
        else:
            self.client = boto3.client('iam', region=region)
        self.available_checks = self.available_checks()


    @staticmethod
    def available_checks():
        return ["IamDisable90DaysCredentials", "IamDisable30DaysCredentials"]


class IamDisable90DaysCredentials(Check):

    def title(self):
        return "iam-disable-90-days-credentials"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        response = self.client.list_users()
        for user in response['Users']:
            try:
                time_since_insertion = datetime.datetime.now(datetime.timezone.utc) - user['PasswordLastUsed']
                if time_since_insertion.days > 90:
                    print(
                        f"{Fore.RED}FAIL!{Style.RESET_ALL} User {user['UserName']} has not logged into the console in the past 90 days")
                else:
                    print(
                        f"{Fore.GREEN}PASS!{Style.RESET_ALL} User {user['UserName']} has logged into the console in the past 90 days")
            except KeyError:
                pass


class IamDisable30DaysCredentials(Check):
    def title(self):
        return "iam-disable-30-days-credentials"

    def description(self):
        return "Ensure credentials unused for 30 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        print(self.client)
        response = self.client.list_users()
        for user in response['Users']:
            try:
                time_since_insertion = datetime.datetime.now(datetime.timezone.utc) - user['PasswordLastUsed']
                if time_since_insertion.days > 30:
                    print(
                        f"{Fore.RED}FAIL!{Style.RESET_ALL} User {user['UserName']} has not logged into the console in the past 90 days")
                else:
                    print(
                        f"{Fore.GREEN}PASS!{Style.RESET_ALL} User {user['UserName']} has logged into the console in the past 90 days")
            except KeyError:
                pass

