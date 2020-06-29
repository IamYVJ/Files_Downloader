import requests 
from time import sleep
import os

def create_directory():
    if not os.path.exists('Downloads'):
        os.mkdir('Downloads')

def download(url):
    r = requests.get(url)
    filename = url[url.rindex('/')+1:]
    with open('Downloads\\' + filename,'wb') as f: 
        f.write(r.content) 

def main():

    create_directory()

    urls = []

    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    count = 0
    curr = 1

    for url in urls:
        print(str(curr) + ' | ' + str(len(urls)))
        curr += 1
        if len(url)==0:
            continue
        try:
            if url[-1]=='\n':
                download(url[:-1])
            else:
                download(url)
            count += 1
            sleep(0.5)
        except Exception as e:
            print('Error: ' + str(e))

    print('Successful: ' + str(count))
    print('Total: ' + str(len(urls)))
    print('Success Rate: ' + str((count/len(urls))*100))

if __name__ == "__main__":
    main()