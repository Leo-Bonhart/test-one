
# 导包
from selenium.webdriver import Chrome
import time
import datetime
import random

def login_web():
    chrome_obj = Chrome(executable_path='D:/chromedriver.exe')  
    chrome_obj.get('http://192.168.2.19:8010/eoffice10/client/web/login')
    time.sleep(10)
    
    user = chrome_obj.find_element_by_xpath('//*[@id="user_account"]')
    time.sleep(1)
    user.click() 
    user.send_keys('yourname')
    time.sleep(0.3)
    
    password = chrome_obj.find_element_by_xpath('//*[@id="password"]')
    time.sleep(1)
    password.click()
    password.send_keys('yourpasswd')
    time.sleep(0.3)
 
    button = chrome_obj.find_element_by_xpath('//*[@class="login-btn"]')
    time.sleep(0.3)
    button.click()
    time.sleep(10)
    #关闭页面
    chrome_obj.close()

def get_random_time():

    login_web_time='08:5'
    random_time=random.randint(0,7)
    login_web_time=login_web_time+str(random_time)
    return login_web_time
    
if __name__ == '__main__':

    target_time=get_random_time()
    print(target_time)
    
    
    while(True):
        time.sleep(50)
        current_time=time.strftime("%H:%M",time.localtime(time.time()))
        
        s=time.strftime("%a",time.localtime(time.time()))


        if(current_time==target_time or current_time=='08:58'):
            if(s=='Satt' or s=='Sun'):
                continue
            login_web()
            break
            