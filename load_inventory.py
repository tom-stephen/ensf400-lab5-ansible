class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# load the inventory 
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
import pprint

dl = DataLoader()
im = InventoryManager(loader=dl, sources=['hosts.yml'])

# Use list_groups_dict() to get a dictionary of groups and their hosts
groups_dict = im.get_groups_dict()
groups = groups_dict.keys()
print("Groups: ", groups)

# Access specific group, e.g., 'app_group'
all_hosts = groups_dict.get('all', [])

for host in all_hosts:
    # Access specific host
    info = im.get_host(host)
    print(f"{Color.GREEN}Info for host {host}:{Color.RESET}",)
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(info.vars)

# Ping the host 
import os
import subprocess

print("\nPinging Hosts")

# Set the ANSIBLE_CONFIG environment variable
ansible_config_path = os.path.abspath('ansible.cfg')
os.environ['ANSIBLE_CONFIG'] = ansible_config_path

# Define the Ansible command
ansible_command = ['ansible', '-i', 'hosts.yml', '-m', 'ping', 'all']

# Run the command
try:
    result = subprocess.run(ansible_command, check=True, text=True, capture_output=True)
    print("Command output:")
    print(f"{Color.GREEN}{result.stdout}{Color.RESET}")
except subprocess.CalledProcessError as e:
    print(f"{Color.RED}Error: {e}")
    print("Command output:")
    print(f"{e.output}{Color.RESET}")


## VVVV this does not work VVV
# import ansible_runner

# action = 'graph'
# inventories = ['hosts.yml']
# r = ansible_runner.interface.get_inventory(action, inventories, response_format=None, host=None, playbook_dir=None, vault_ids=None, vault_password_file=None, output_file=None, export=None)
# # print("{}: {}".format(r.status, r.rc))
# print(r)

# # Define the inventory path
# inventory_path = 'hosts.yml'

# # Run the ping command
# r = ansible_runner.interface.run_command('ping', cmdline_args=['-m', 'all:localhost'])
# print(r)