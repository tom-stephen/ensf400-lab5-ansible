#!/usr/bin/env python
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

# Custom callback to capture ping results
class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        print(f"{host.name} | SUCCESS => {result._result['ping']}")

def load_inventory():
    loader = DataLoader()
    inventory_manager = InventoryManager(loader=loader, sources=['/path/to/your/inventory.ini'])
    variable_manager = VariableManager(loader=loader, inventory=inventory_manager)

    # Print names, IP addresses, and group names of all hosts
    for host in inventory_manager.get_hosts():
        print(f"Name: {host.name}, IP Address: {host.vars['ansible_host']}, Groups: {host.groups}")

    return inventory_manager, variable_manager

def ping_hosts(inventory_manager, variable_manager):
    play_source = {
        'name': 'Ping all hosts',
        'hosts': 'all',
        'gather_facts': 'no',
        'tasks': [
            {'name': 'Ping', 'ping': {}}
        ]
    }

    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    tqm = TaskQueueManager(
        inventory=inventory_manager,
        variable_manager=variable_manager,
        loader=loader,
        passwords={},
        stdout_callback=ResultCallback()
    )
    result = tqm.run(play)

if __name__ == "__main__":
    loader = DataLoader()
    inventory_manager, variable_manager = load_inventory()
    ping_hosts(inventory_manager, variable_manager)
