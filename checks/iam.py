from checks.check import Check

class Check13(Check):
    def title(self):
        return "Check13"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        import boto3
        import datetime
        from colorama import Fore, Style

        client = boto3.client('iam')
        response = client.list_users()
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

