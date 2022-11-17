# partie test tp

#import
import time
import threading
import sys
import multiprocessing
import concurrent.futures
import requests

#lien image
img_urls = [
    'https://pixabay.com/get/gcdbacfd56b42152d4823af278675b00aa41ce3d337867e827a36354bec3fa477def3938b2081319dd9a9b975853cc7c185592974712adb3def090cc55a46ecc8396e47e720183d7e87d35dd5e07fe26d_640.jpg',
    'https://pixabay.com/get/gebf87d632e3b539e9d99c4033c327a3cded6b4f45809d21c718bf0d88066e0451c6234f399ce1cd973e362c800df538c8711b8f2077c2164ad09da0e024497d2241b93a23babc50eb3e1c982a9a0066f_640.jpg',
    'https://pixabay.com/get/gc80d12b47489c9a82cacc0e08f52603c1fa56c4e1989fd3dc4649c361d2d9f5539b6868085a050d1cac4706000a4ecd1fa3aa71401d1a9a28a4b56d451fcf884f7bd73ba554a75111aff697850a78a04_640.jpg'
    ]

def task(i):
    print(f"Task {i} starts for {i+1} second(s)")
    time.sleep(i+1)
    print(f"Task {i} ends")

def tache(i):
    print(f"Task {i} starts")
    time.sleep(1)
    print(f"Task {i} ends")

def main100Thread():
    start = time.perf_counter()

    T = []
    for i in range(100):
        T.append(threading.Thread(target=tache, args=[i]))
    for i in range(len(T)):
        T[i].start()
    for i in range(len(T)):
        T[i].join()

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")

def mainThread():
    start = time.perf_counter()
    T = []
    for i in range(10):
        T.append(threading.Thread(target=task, args=[i]))

    for i in range(len(T)):
        T[i].start()

    for i in range(len(T)):
        T[i].join()

    end = time.perf_counter()

    print(f"Tasks ended in {round(end - start, 2)} second(s)")

def mainSuite():
    start = time.perf_counter()

    for i in range(10):
        task(i)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

def mainMultiprocessing():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=task, args=[1])
    p2 = multiprocessing.Process(target=task, args=[2])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

def image_excution():
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

if __name__ == '__main__':
    sys.exit(image_excution())