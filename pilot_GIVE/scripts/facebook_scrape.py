from csv import DictReader
import os
from random import randint
from sys import argv
from time import sleep
from uuid import uuid4

from dotenv import load_dotenv
from facebook_scraper import get_profile
import requests

csv = argv[1]
output_dir = argv[2]

load_dotenv()
cookies = os.getenv('COOKIES')
QID_key = 'QID'
facebook_key = 'Facebook_ID'

def facebook_scrape(facebook_id, output):
    #output folder
    uuid = str(uuid4())
    path = output + '/' + uuid + '.jpg'

    json = get_profile(facebook_id, cookies=cookies)
    image_url = json['profile_picture']

    if image_url.startswith('http'):
        image_data = requests.get(image_url).content

        # downlaod image
        with open(path, "wb") as handler:
            handler.write(image_data)

        ## let it sleep, let it sleep, let it sleep
    pause = randint(0, 300)
    print("sleeping for " + str(pause) + ' seconds')
    sleep(pause)


def create_folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def start():
    with open(csv, 'r') as input_file:
        reader = DictReader(input_file)
        os.chdir(output_dir)
        for row in reader:
            facebook = row[facebook_key]
            if not facebook == '':
                folder = row[QID_key]
                create_folder(folder)
                facebook_scrape(facebook, folder)
                
        input_file.close()

start()