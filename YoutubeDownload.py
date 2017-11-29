import os

def download(youtube_link):
    os.system(r'e: && cd E:\Books (Audio and eBooks)\youtube-dl && youtube-dl -f "bestaudio[ext=m4a]/best[ext=mp4]/best" "' + youtube_link + '"')

text_file = open("E:\Books (Audio and eBooks)\youtube-dl\Youtube links.txt", "r")
links = text_file.readlines()
links = [l.replace('\n', '') for l in links]
print(links)
text_file.close()

for link in links:
    download(link)
    print(link + " downloaded.")