import requests
import time
from pushbullet import Pushbullet

# Website URL'sini belirle
url = input("Enter website URL: ")
# URL girilene kadar kullanıcıyı uyar
while not url:
    print("Please enter a website URL!")
    url = input("Enter website URL: ")

# Pushbullet API anahtarını iste
pushbullet_api_key = input("Enter your Pushbullet API key: ")
# API key girilene kadar kullanıcıyı uyar
while not pushbullet_api_key:
    print("Please enter your Pushbullet API key!")
    pushbullet_api_key = input("Enter your Pushbullet API key: ")

# Pushbullet nesnesini oluştur
pb = Pushbullet(pushbullet_api_key)

# Website'nin durumunu kontrol etmek için bir fonksiyon tanımla
def is_website_up(url):
    try:
        # Website'ye istek gönder
        response = requests.get(url)
        # Website 200 OK yanıtı verirse, website açıktır
        if response.status_code == 200:
            return True
        # Diğer durumlarda website kapalıdır
        else:
            return False
    # İstek gönderirken bir hata oluşursa website kapalıdır
    except:
        return False

# Ana döngü
while True:
    # Website'nin durumunu kontrol et
    if is_website_up(url):
        print("Website is up!")
        # Website açıksa bekleyin ve tekrar kontrol edin
        time.sleep(300)
    else:
        print("Website is down!")
        # Website kapalıysa bildirim gönderin
        message = "The website is not responding."
        pb.push_note("Website is down!", message)
        # Website tekrar açılana kadar bekleyin
        while not is_website_up(url):
            time.sleep(60)
        # Website tekrar açıldığında mesaj verin
        print("Website is back up!")
