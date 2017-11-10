import os

def download(youtube_link):
    os.system('e: && cd E:\Books (Audio and eBooks)\youtube-dl && youtube-dl -f bestaudio "' + youtube_link + '"')

text_file = open("E:\Books (Audio and eBooks)\youtube-dl\Youtube links.txt", "r")
links = text_file.readlines()
links = [l.replace('\n', '') for l in links]
print(links)
text_file.close()

for link in links:
    download(link)
    print(link + " downloaded.")