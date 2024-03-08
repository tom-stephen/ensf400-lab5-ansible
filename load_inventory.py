from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

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
    print(f"Info for host {host}:",info.vars)
    # print(info.vars)
