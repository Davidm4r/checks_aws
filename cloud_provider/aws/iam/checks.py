from cloud_provider.aws.client import Check, Service, Client

class CheckServices(Service):

    def available_methods(self):
        return ["IamDisable90DaysCredentials", "IamDisable30DaysCredentials"]

    def available_services(self):
        return ["iam"]

class IamDisable90DaysCredentials(Check):

    def title(self):
        print(f"Cliente 12345 {self.client}")
        return "iam-disable-90-days-credentials"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        print(f"Execute {self.title()}")

class IamDisable30DaysCredentials(Check, Client):

    def title(self):
        print(f"Cliente 12345 {self.client}")
        return "iam-disable-30-days-credentials"

    def description(self):
        return "Ensure credentials unused for 90 days or greater are disabled"

    def severity(self):
        return "High"

    def execute(self):
        import datetime
        from colorama import Fore, Style

        print(f"Execute {self.title()}")
        response = self.client.iam.list_users()
        for user in response['Users']:
            try:
                time_since_insertion = datetime.datetime.now(datetime.timezone.utc) - user['PasswordLastUsed']
                if time_since_insertion.days > 30:
                    print(
                        f"{Fore.RED}FAIL!{Style.RESET_ALL} User {user['UserName']} has not logged into the console in the past 30 days")
                else:
                    print(
                        f"{Fore.GREEN}PASS!{Style.RESET_ALL} User {user['UserName']} has logged into the console in the past 30 days")
            except KeyError:
                pass
