import subprocess
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import  By
import time

geckopath=Service(r"C:\drivers\geckodriver.exe")
hostel="LPU Hostels-5G"
collage="LPU Wireless"
username="username"
password="password"

driver=webdriver.Firefox(service=geckopath)
# time.sleep(1)

def check_which_wifi_to_connect_to():
    wifi_list=str(subprocess.run("netsh wlan show networks",check=False,capture_output=True,text=True))
    if hostel in wifi_list:
        subprocess.run(["netsh", "wlan", "connect", f"name={hostel}", f"ssid={hostel}"],check=False)
    elif collage in wifi_list:
        subprocess.run(["netsh", "wlan", "connect", f"name={collage}", f"ssid={collage}"],check=False)



def setField():
    name=driver.find_element(By.NAME,"username")
    pasw=driver.find_element(By.NAME,"password")
    checkbox=driver.find_element(By.ID,"agreepolicy")
    login=driver.find_element(By.ID,"loginbtn")

    name.send_keys(username)
    pasw.send_keys(password)
    checkbox.click()
    login.click()

connected=str(subprocess.run("netsh wlan show interfaces",capture_output=True,text=True))
if hostel in connected or collage in connected:
    print("already connected")
else:
    check_which_wifi_to_connect_to()
time.sleep(1)
driver.get("https://internet.lpu.in/24online/servlet/E24onlineHTTPClient")
time.sleep(5)
setField()
time.sleep(1)
driver.quit()



# print(subprocess.run("netsh wlan show"))
# driver.get("https://amazon.com")
# time.sleep(6)
# cli=driver.find_element(By.ID,"twotabsearchtextbox")
# cli.send_keys("shoes")
