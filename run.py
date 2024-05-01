import paramiko
import time

from datetime import date

client = paramiko.SSHClient()


def ssh_command(command) -> str:
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode("utf-8")


while True:
    ssh_command(f'pg_dump -U denis family_finances > /home/denis/db/dump_db_family_finances_{date.today()}.sql')
    time.sleep(28800)
