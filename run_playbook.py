import ansible_runner
import os

# Set the ANSIBLE_CONFIG environment variable
ansible_config_path = os.path.abspath('ansible.cfg')
os.environ['ANSIBLE_CONFIG'] = ansible_config_path

r = ansible_runner.run(private_data_dir='secrets', playbook='/workspaces/ensf400-lab5-ansible/hello.yml')
print("{}: {}".format(r.status, r.rc))
# successful: 0
for each_host_event in r.events:
    print(each_host_event['event'])
print("Final status:")
print(r.stats)