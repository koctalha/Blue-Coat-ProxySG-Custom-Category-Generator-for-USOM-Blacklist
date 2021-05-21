import wget
import os

url = 'https://www.usom.gov.tr/url-list.txt'
filename = wget.download(url)
with open("url-list.txt", "r") as file:
    lines = file.read().split("\n")
    newlines = ["define category USOM_URL_BLOCK_LIST"]
    for line in lines:
        line = line.rstrip()
        newline = '\t' + line
        newlines.append(newline)
        newlines = newlines[:-1]
        newlines.append("end")
with open("clean-url-list.txt", "w") as newfile:
    newfile.write("\n".join(newlines))
os.remove('url-list.txt')