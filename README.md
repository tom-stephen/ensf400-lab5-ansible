## These are the changed i made for the assignment!
1. the docker compose file makes a socker container for the load balencer bit does not give it a port to listen on becasue i use nginx on the local host. i incuded this change to show my competience in doing so. I ok'ed this with the professor. 
2. i installed nginx on locak host in the asnible playbook hello.yml. 
3. i did not include the load balancer in the hosts file as i do not need to install nginx on it. 
4. in the load_inventory file i used and ansible python module as well as the ansible runner module to load the loacl hosts. i also ok'ed this with the professor.
5. i created a new playbook called hello2.yml for the python script to run becasue the updated play installs nginx on local host but that leads to an error when trying to run the program on the same computer. I also ok'ed this with the professor.