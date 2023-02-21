import wget
import os
import shutil

url1 = 'https://www.usom.gov.tr/url-list.txt'

dosya1_adi = "url-list.txt"
baslangic_verisi1 = "define category USOM_URL_BLOCK_LIST\n"
bitis_verisi = "\nend\n"

# Dosya1'i okuyun
try:
    filename = wget.download(url1)
    with open(dosya1_adi, "r") as dosya1:
        icerik1 = dosya1.readlines()
        with open("proxysgdbtmp.txt", "a") as writeFile:
            writeFile.write(baslangic_verisi1)
            for icerik in icerik1:
                icerik = icerik.split('/')
                cleanicerik = icerik[0]
                #print(cleanicerik)
                if ":" in cleanicerik:
                    continue
                else:
                    if len(cleanicerik)>128:
                        print(cleanicerik)
                        cleanicerik = cleanicerik.split('.')
                        i = len(cleanicerik)
                        cleanicerik = str(cleanicerik[i-3])+"."+str(cleanicerik[i-2])+"."+str(cleanicerik[i-1])
                        print(cleanicerik)
                    cleanicerik = cleanicerik+"\r"
                    writeFile.write(cleanicerik)

            writeFile.write(bitis_verisi)
except:
    pass

shutil.copyfile("proxysgdbtmp.txt","proxysgdb.txt")

os.remove("url-list.txt")
os.remove("proxysgdbtmp.txt")