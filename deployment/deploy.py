
#we can run the ansible playbook manually through the following command or we can use the following python automation code
#command for running the ansible playbook(the Gunicorn method) manually
#ansible-playbook -i /path/to/src/projectinventory /path/to/src/projectdeploy.yml


import paramiko
# SSH connection information for the target VMs
hosts = ['target_vm1_ip', 'target_vm2_ip']

username = 'ssh_username'
password = 'ssh_password'


# Define commands to execute on the target VMs
commands = [
    f'cd /path/tosrc/project && pip install -r /path/to/src/projectrequirements.txt',
    f'cd /path/tosrc/project && gunicorn main:app -b 0.0.0.0:5000 --daemon'
]


# SSH connection and execution of commands
for host in hosts:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host, username=username, password=password)

        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(f'Result for {host} - {command}: {stdout.read().decode()}')
            print(f'Error for {host} - {command}: {stderr.read().decode()}')

    except paramiko.AuthenticationException as e:
        print(f'Authentication failed for {host}: {e}')
    except paramiko.SSHException as e:
        print(f'SSH error for {host}: {e}')
    except paramiko.BadHostKeyException as e:
        print(f'Bad host key for {host}: {e}')
    finally:
        client.close()