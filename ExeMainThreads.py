# partie validation threads, pool et multiprocessing

#import
import time
import threading
import sys
import multiprocessing
import concurrent.futures
import requests
import statistics

#lien image
img_urls = [
    'https://pixabay.com/get/ge36da8e79b014449b480ffe562b1806e9535f65be56f56a8c5605c9888ebda22da49b5008a721f28dbf8b0d2ad9886b1d8b343ea7011387f8d29904969f607e090d0d26b2f8a41bd2d135665a858b30b_1920.jpg',
    'https://pixabay.com/get/gb00c9d30215223e75255ce8b304c17be148341ea3098d45eac460f8b83e226cb12decbfc596f66d521eeee905803dcfb8a3267d04d54008b58d5433cf877b46319b99d60376505256b2a21c4ee338374_1920.jpg',
    'https://pixabay.com/get/g9c60a8778795014208aecd888625ad2593d7fdca6eb40d82c2f3028c1117b7ef72e279fdf39bff3d4decfb76d7725ec65bb647ae6a4730953aaec39380d7dd96ff71a55674441880804128c01569cc68_1920.jpg'
    ]

#fonction download permet nommer et de récuprer les image
def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
#        print(f"{img_name} was downloaded")

def Threads():
    T = []

    for i in range(3):
        T.append(threading.Thread(target=download_image, args=(img_urls[i],)))

    for i in range(len(T)):
        T[i].start()

    for i in range(len(T)):
        T[i].join()



def poolThreads():

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)


def Multiprocessing():
    P = []
    for i in range(3):
        P.append(multiprocessing.Process(target=download_image, args=(img_urls[i],)))

    for i in range(len(P)):
        P[i].start()

    for i in range(len(P)):
        P[i].join()

def TestDownload(nb):
    Th = []
    Thp = []
    Mp = []
    for i in range (nb):
        start = time.perf_counter()
        Threads()
        end = time.perf_counter()
        Th.append(round(end - start, 2))
        print(f"Thread {i}/{nb}")

    for z in range(nb):
        start = time.perf_counter()
        poolThreads()
        end = time.perf_counter()
        Thp.append(round(end - start, 2))
        print(f"pool {z}/{nb}")

    for x in range(nb):
        start = time.perf_counter()
        Multiprocessing()
        end = time.perf_counter()
        Mp.append(round(end - start, 2))
        print(f"Multiprocessing {x}/{nb}")

    moyenneTH = statistics.fmean(Th)
    moyenneTHP = statistics.fmean(Thp)
    moyenneMP = statistics.fmean(Mp)

    print(f"Vitesse moyenne pour 10 Multiprocessing {moyenneMP:.2f}s. Vitesse moyenne pour 10 poolThreads {moyenneTHP:.2f}s. Vitesse moyenne pour 10 Threads {moyenneTH:.2f}s. ")


if __name__ == '__main__':

    if sys.argv[1] == "--nb":
        nb = int(sys.argv[2])
        sys.exit(TestDownload(nb))

# .\ExeMainThreads.py --nb 10 <- "valeur de nb"