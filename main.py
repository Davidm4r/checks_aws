from checks.iam import checks
import importlib
import argparse

available_groups = ['iam', 'security_groups']

regions = ['eu-north-1', 'ap-south-1', 'eu-west-3', 'eu-west-2', 'eu-west-1', 'ap-northeast-3', 'ap-northeast-2',
           'ap-northeast-1', 'sa-east-1', 'ca-central-1', 'ap-southeast-2', 'eu-central-1', 'us-east-1', 'us-east-2',
           'us-west-1', 'us-west-2']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups", nargs='+', help="Select group")
    parser.add_argument("--regions", nargs='+', help="Select regions")

    args = parser.parse_args()

    if args.groups:
        groups = args.groups
    else:
        groups = available_groups

    if args.regions:
        regions = args.regions
    else:
        regions = ['eu-west-1'] # TODO ADD REGION DEFAULT FROM FILE
    for group in groups:
        lib = importlib.import_module(f'checks.{group}.checks')
        for region in regions:
            client = lib.CheckClient(region)
            for check in client.available_checks:
                method_to_call = getattr(lib, check)
                print(method_to_call(client.client).title())
                print(method_to_call(client.client).description())
                method_to_call(client.client).execute()

