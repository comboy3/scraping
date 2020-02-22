# -*- coding: utf-8
import pandas as pd
import requests
from selenium import webdriver

"""
初期設定
"""
browser = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver\chromedriver.exe")
# df = pd.read_csv("default.csv" index_col=0)
df = pd.DataFrame(columns=["TITLE","ANIME_TITLE","IMAGE","AUDIO"])
url ="https://pc.animelo.jp/"
res = requests.get(url)
print(res.text)
"""
CSS SELECTER
"""
PAGE_NEXT = "div.page-links.cf"
TITLE = "h3"
IMAGE = "img.appIconImg"
AUDIO = "audio"

"""
メイン
"""
# browser.get(url)

# numPage = 2
# while True: # 最後のページまで

#     if numPage <= 5:   
#         titles = browser.find_elements_by_css_selector(TITLE)
#         images = browser.find_elements_by_css_selector(IMAGE)
#         audios = browser.find_elements_by_css_selector(AUDIO)
#         print(len(titles))
#         print(len(images))
#         print(len(audios))
#         minNum = min(len(titles),len(images),len(audios))
#         print(minNum)

#         for i in range(minNum):
#             try:
#                 title = titles[i].text
#                 print(title)
#                 num = title.find("「")
#                 num += 1
#                 tmpTitle = title[num:]
#                 titleList = tmpTitle.split("」/")
#                 title1 = titleList[0]
#                 title2 = titleList[1]
#                 print(title1)
#                 print(title2)
#                 image = images[i].get_attribute("src")
#                 print(image)
#                 audio = audios[i].get_attribute("src")
#                 print(audio)

#                 se = pd.Series([title1,title2,image,audio], df.columns)    
#                 df = df.append(se, ignore_index=True)
                
#             except Exception as e:
#                 print(e)
        
#         btn = url + "/" + str(numPage)
#         print("go nextpage=" + btn)
#         browser.get(btn)
#         numPage += 1
#                 #browser.get(nextpage)
#     else:
#         print("end")
#         break

# #CSV出力
# print("CSVの出力")
# df.to_csv("scraping/outputAnison.csv")
# print("完了")
