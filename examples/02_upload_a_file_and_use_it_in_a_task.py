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
password = getpass("Please Enter Catalyst password: ") or "<not set>"

URL=f"{base_url}/api"

jm_client = JinjamatorClient(URL, ssl_verify=False)
print("login to jinjamator with username and password using the local aaa povider")
jm_client.login(username, password, "local")
api = jm_client.api

jm_filename=jm_client.upload("/tmp/test.xlsx")

print("start job and get id")

job_id=jm_client.run("/tasks/jinjamator101/some_task_that_needs_a_file",file=jm_filename)

print("poll job status and wait for success or failure (default timeout is 300s, default pollrate=10s) ")
jm_client.wait_for_job(job_id)

