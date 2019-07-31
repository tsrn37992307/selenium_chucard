from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import os
import json

#設定帳號密碼
myemail = input("請輸入帳號 : ")
mypassword = input("請輸入密碼 : ")
#今日時間
date = datetime.datetime.now().date()
#設定網址
DcardAPI_URL = "https://www.dcard.tw/_api/dcard"
URL = "https://www.dcard.tw/f"
#mypath = 檔案的位置
mypath = os.getcwd()
#開啟chromedriver
driver = webdriver.Chrome(mypath+"\\chromedriver")
#等待開啟時間3秒
driver.implicitly_wait(3)
#開啟網址
driver.get(URL)

#點擊登入按鈕
driver.find_element_by_class_name("Header_navText_1m5321").click()
#輸入帳號密碼
driver.find_element_by_name("email").send_keys(myemail)
driver.find_element_by_name("password").send_keys(mypassword)
#submit帳號密碼
driver.find_element_by_class_name("SignupForm_formBtn_3lPuuc").click()

#點擊抽卡畫面
driver.find_element_by_class_name("Header_dcardBtn_1vJVP3").click()

driver.get(DcardAPI_URL)
#當前的原始碼
Source_code = driver.page_source
#解析
soup = BeautifulSoup(Source_code,"html.parser")

#把抽卡頁面存取jason
with open ('dcard.json','w',encoding="utf-8") as fp :
    fp.write(soup.text)
    fp.close()
#讀取json檔
with open(mypath+"\\dcard.json",'r',encoding="utf-8") as load_f:
    load_dict = json.load(load_f)
    all = load_dict["dcard"]
    #取出需要json資料
    print("日期 : " + str(date) + "\n學校 : "+str(all["school"]),"\n科系 : " +str(all["department"]) , "\n性別 : " + str(all["gender"]) ,"\n專長與興趣 : " + str(all["talent"]) , "\n社團 : " + str(all["club"]), "\n喜歡的課 :" + str(all["lecture"]) , "\n喜歡的國家" + str(all["lovedCountry"]),"\n最近的困擾 : " + str(all["trouble"]) , "\n可交換的才藝 : " + str(all["exchange"]) , "\n想嘗試的事情 : " + str(all["wantToTry"]))

    #抓取圖片網址
    imgeURL = all["avatar"]
    #輸入網址
    driver.get(imgeURL)
    #擷取圖片
    driver.get_screenshot_as_file(mypath+"\\dcard.png")
    load_f.close()
driver.close()
