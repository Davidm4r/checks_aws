from checks.iam import checks
import importlib
import argparse
from colorama import Fore, Style
import time
from checks.check import Check, Client



available_groups = ['iam', 'security_groups']

regions = ['eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2',
           'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2',
           'us-west-1', 'us-west-2']

if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups", nargs='+', help="Select group")
    parser.add_argument("--regions", nargs='+', help="Select regions")
    parser.add_argument("--provider", help="Select provider")

    args = parser.parse_args()

    if args.groups:
        groups = args.groups
    else:
        groups = available_groups

    if args.provider:
        provider = args.provider
    else:
        provider = "aws"

    if args.regions:
        regions = args.regions
    else:
        regions = ['eu-west-1']  # TODO ADD REGION DEFAULT FROM FILE

    for group in groups:
        check_library = importlib.import_module(f'cloud_provider.{provider}.{group}.checks')
        lib_client = importlib.import_module(f'cloud_provider.{provider}.client')
        services = check_library.CheckServices()
        client = lib_client.Client(services.available_services())
        for method in services.available_methods():
            m = getattr(check_library, method)
            m(client).execute()
            print(client)
        print("AAA")
'''
    for group in groups:
        check_library = importlib.import_module(f'checks.{group}.checks')  #check.py inside each service.
        check_client = check_library.CheckClient()
        available_checks = check_client.available_checks
        for check in available_checks:
            method_to_call = getattr(check_library, check)
            print(f"{Fore.YELLOW} {method_to_call().title()} {Style.RESET_ALL}")
            print(f"{Fore.BLUE} {method_to_call().description()} {Style.RESET_ALL}")
            method_to_call.execute(check_client)
            print(method_to_call().client)
    print("--- %s seconds ---" % (time.time() - start_time))
'''
'''
    for group in groups:
        lib = importlib.import_module(f'checks.{group}.checks')
        for region in regions:
            client = lib.CheckClient(region)
            for check in client.available_checks:
                method_to_call = getattr(lib, check)
                print(f"{Fore.YELLOW} {method_to_call().title()} {Style.RESET_ALL}")
                print(f"{Fore.BLUE} {method_to_call().description()} {Style.RESET_ALL}")
                method_to_call().execute()

    print("--- %s seconds ---" % (time.time() - start_time))

'''