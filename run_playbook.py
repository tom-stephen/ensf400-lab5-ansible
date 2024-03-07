#!/usr/bin/env python
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase

# Custom callback to capture playbook results
class ResultCallback(CallbackBase):
    def v2_playbook_on_stats(self, stats):
        for host, result in stats.summarize().get('ok', {}).items():
            print(f"{host} | SUCCESS => {result}")

def run_playbook(inventory_manager, variable_manager):
    play_source = {
        'name': 'Run hello.yml playbook',
        'hosts': 'app',  # Replace 'app' with your target group
        'gather_facts': 'no',
        'tasks': []
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
    run_playbook(inventory_manager, variable_manager)

