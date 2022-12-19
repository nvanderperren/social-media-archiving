import requests
from csv import DictReader
from sys import argv
from uuid import uuid4
import os
from time import sleep
from random import randint

csv = argv[1]
folder = argv[2]

filename = 'qid'
linkedin_key = 'LinkedIn_ID'
QID_key = 'QID'


def linkedin_scrape(linkedin_id, output):
    #output folder
    uuid = str(uuid4())
    path = output + '/' + uuid + '.jpg'

    # get the json of the person
    # requirement `nmp start @ linkedin-profile-scraper`
    response = requests.get("http://localhost:3000/?url=https://linkedin.com/in/" + linkedin_id)

    # scrape the profile pic url
    image_url = response.json()['userProfile']['photo']
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


def start(metadata, output_dir):
    print("hello! starting!")
    with open(metadata, 'r') as input_file:
        reader = DictReader(input_file)
        os.chdir(output_dir)
        for row in reader:
            linkedin = row[linkedin_key]
            if not linkedin == '':
                folder = row[QID_key]
                create_folder(folder)
                linkedin_scrape(linkedin, folder)
                
        input_file.close()

start(csv, folder)