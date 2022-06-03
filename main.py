from checks.iam import checks
import importlib
import argparse

available_groups = ['iam', 'security_groups']

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups", nargs='+', help="Select group")

    args = parser.parse_args()

    if args.groups:
        groups = args.groups
    else:
        groups = available_groups

    for group in groups:
        lib = importlib.import_module(f'checks.{group}.checks')
        client = lib.CheckClient()
        for check in client.available_checks:
            method_to_call = getattr(lib, check)
            print(method_to_call(client.client).title())
            print(method_to_call(client.client).description())
            method_to_call(client.client).execute()

