from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import geckodriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

#Hàm tự động login Facebook từ tài khoản và mật khẩu người dùng nhập
def login_facebook(user,passw):
    driver.get("https://www.facebook.com/")
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
    username.clear()
    username.send_keys(user)
    password.clear()
    password.send_keys(passw)
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    option = Options()
#Hàm nhập các link post cần thống kê lượng react
def get_link_facebook():
    Array_link = []
    number_of_link = int(input('The number of Facebook posts you want to analyze: '))

    for i in range(number_of_link):
        Array_link.append(input('Enter your link of post: '))
    Modified_links = []
    #chuyển từ www sang mbasic để dễ dàng thống kê
    for link in Array_link:
        Modified_links.append(link.replace("www", "mbasic"))
    return  Modified_links
#Hàm Thống kê lượng react
def get_sas_react(link):
    driver.get(link)
    info_arr= []#mảng lưu tên và tiêu đề 
    user = driver.find_element(By.TAG_NAME, 'strong').text
    time.sleep(3)
    title = driver.find_element(By.TAG_NAME,'p').text
    time.sleep(3)
    info_arr.append(user)
    info_arr.append(title)
    #lấy lượng react
    another_btn = driver.find_elements(By.XPATH, '//a[contains(@href, "/ufi/reaction/profile")]')
    a=another_btn[0].get_attribute("href")
    driver.get(a)
    time.sleep(3)
    sasti_react = driver.find_elements(By.XPATH, '//a[contains(@href, "/ufi/reaction/profile")]')
    sasti_arr=[0,0,0,0,0,0,0,0]
    for i in range(len(sasti_react)-1):
        sasti_arr[i]=sasti_react[i].text
    info_arr += sasti_arr
    return info_arr
#chuyển thông tin lấy được vào bảng
def analyze_post(arr,statis_table):
    for i in range(len(arr)) :
        sasti_arr= get_sas_react(arr[i])
        statis_table.loc[i]= sasti_arr[:10]
    return statis_table
#Chạy chương trình
if __name__ == "__main__":
    #khởi tạo bảng các thông tin
    statis_table = pd.DataFrame(columns=['User','Title','Sum','Like','Love','LoveLove','HaHa','Wow','Sad','Angry'])
    user_facebook = input('Your UserName on Facebook: ')
    pass_facebook = input('Your PassWord on Facebook: ')
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    login_facebook(user_facebook,pass_facebook)
    time.sleep(5)
    link_facebook= get_link_facebook()
    print("Below are the statistical results")
    result= analyze_post(link_facebook,statis_table)
    print(result)                   



