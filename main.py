from checks.iam import checks
import importlib

groups = ['iam', 'security_groups']

for group in groups:
    lib = importlib.import_module(f'checks.{group}.checks')
    client = lib.CheckClient()
    for check in client.available_checks:
        method_to_call = getattr(lib, check)
        print(method_to_call(client.client).title())
        print(method_to_call(client.client).description())
        print("\n")
        method_to_call(client.client).execute()

