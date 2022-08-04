import sys
import os
import json
import time
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from types import SimpleNamespace
sys.path.insert(0, './bin')
# import bin.open_master_product as omp
import bin._cmd as cmd


while True:
    os.system('cls')
    cmd.header()
    cmd.option_command()
    comm = input("Silahkan pilih perintah : ")
    if comm not in ['1','2','3']:
        input("Apakah anda tidak bisa membaca...???")
    else:
        comm = int(comm) 
        break

cmd.option_url()
url = input("Silahkan pilih perintah : ")
if url not in ['1','2','3']:
    input("Apakah anda tidak bisa membaca...???")
else:
    url = int(url) 

with open('./bin/data.json') as f:
    dt = json.load(f,object_hook=lambda d: SimpleNamespace(**d))
dt = dt.urls

if comm == 1:
    print(dt[0].url)
cmd.footer()