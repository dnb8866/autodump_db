import paramiko
import time

from datetime import date

client = paramiko.SSHClient()


def ssh_connect(func):
    def wrapper(*args, **kwargs):
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=,
                       username=,
                       password=,
                       port=)
        data = func(*args, **kwargs)
        client.close()
        return data
    return wrapper


@ssh_connect
def ssh_command(command) -> str:
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode("utf-8")


while True:
    ssh_command(f'pg_dump -U denis family_finances > /home/denis/db/dump_db_family_finances_{date.today()}.sql')
    time.sleep(28800)
