import os
import sys
try:
    from simple_jinjamator import JinjamatorClient
except ImportError:
    sys.path.insert(0,os.path.sep.join(__file__.split(os.path.sep)[:-2]))
    from simple_jinjamator import JinjamatorClient


import logging
from getpass import getpass
import string
from pprint import pprint

base_url = input("Please Enter Jinjamator URL: ") or "http://localhost:5000"
username = input("Please Enter Jinjamator username: ") or "root"
password = getpass("Please Enter Jinjamator password: ") or "<not set>"

URL=f"{base_url}/api"

jm_client = JinjamatorClient(URL, ssl_verify=False)
print("login to jinjamator with username and password using the local aaa povider")
jm_client.login(username, password, "local")
api = jm_client.api

print("start job in environment some/env with the parameter command and get the job id")

job_id=jm_client.run("/tasks/jinjamator101/discover_cisco_device",environment="some/env",command="show interface status")

print("poll job status and wait for success or failure (default timeout is 300s, default pollrate=10s) ")
jm_client.wait_for_job(job_id)

print("download all generated files to /tmp")
jm_client.download_job_files(job_id,"/tmp")

