import ansible_runner
import os
import pprint

# Set the ANSIBLE_CONFIG environment variable
ansible_config_path = os.path.abspath('ansible.cfg')
os.environ['ANSIBLE_CONFIG'] = ansible_config_path

r = ansible_runner.run(private_data_dir='secrets', playbook='/workspaces/ensf400-lab5-ansible/hello2.yml')
print("{}: {}".format(r.status, r.rc))
# successful: 0
print("Final status:")
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(r.stats)