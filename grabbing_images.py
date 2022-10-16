import datetime
import os
import time
import threading
import requests
from bs4 import BeautifulSoup

img_url = []

def get_urls(URL):
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.content, 'html.parser')
    anchor_tag = soup.findAll("a", {"title" : "Download photo"})

    for i in anchor_tag:
        get_link = i["href"]
        img_url.append(get_link)

def download_images(URL, TIMESTAMP):

    file_name = TIMESTAMP+"/"+URL.split('/')[4]+".jpg"
    resp = requests.get(URL)
    
    file = open(file_name, "wb")
    file.write(resp.content)
    file.close()

def main():
    start = time.perf_counter() 

    URL = input('Enter the URL - ')
    print(f"Grabbing the URLs...")
    # get_urls('https://unsplash.com/t/nature')
    
    get_urls(URL)
        # DIRECTORY = "Images"
    now = datetime.datetime.now()
    TIMESTAMP = now.strftime("%d_%m_%Y_%H_%M_%s")
    if os.path.exists(TIMESTAMP):
        print("Directory Exists!\n Downloading the Images")
    else:
        print("Directory Does not exist!\n Creating a directory")
        os.mkdir(TIMESTAMP)

    print("Downloading the Images")

    threads = []

    for link in img_url:
        t = threading.Thread(target=download_images, args=[link, TIMESTAMP])
        t.start()
        threads.append(t)
    
    for thread in threads:
        thread.join()
    
    finish = time.perf_counter()
    print(f"{len(img_url)} Images Downloaded in {round(finish - start, 2)} second(s)")

if __name__ == '__main__':
    main()