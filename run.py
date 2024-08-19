import os
import paramiko
import time

from datetime import date, datetime
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
client = paramiko.SSHClient()


def ssh_connect(func):
    def wrapper(*args, **kwargs):
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=os.getenv("HOSTNAME"),
                       username=os.getenv("USERNAME"),
                       password=os.getenv("PASSWORD"),
                       port=os.getenv("PORT_SSH")
                       )
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
    ssh_command(f'pg_dump -U denis ci > /home/denis/db/dump_db_ci_{date.today()}.sql')
    ssh_command(f'pg_dump -U spaced_repetition ci > /home/denis/db/dump_db_ci_{date.today()}.sql')
    print(f"{datetime.today()} ok")
    time.sleep(28800)
