# -*- coding: utf-8
import pandas as pd

from selenium import webdriver

"""
初期設定
"""
browser = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver\chromedriver.exe")
# df = pd.read_csv("default.csv" index_col=0)
df = pd.DataFrame(columns=["NAME","RATING", "AREA","TITLE","NIGHT_PRICE","HIRU_PRICE","IMAGE"])
""" loginUrl = "https://www.anikore.jp/users/login/"
loginName = "slumdank3@gmail.com"
loginPass = "nishihigashi" """

print('URLを入力してください')
url = r"https://tabelog.com/tokyo/rstLst/cond04-00-03/?Srt=D&SrtT=rt&sort_mode=1&LstSmoking=0&svd=20180502&svt=1900&svps=2&LstCosT=3&RdoCosTp=2"

"""
CSS SELECTER
"""
PAGE_NEXT = ".next"
POSTS = "div.list-rst__bookmark.js-void-opennewtab"
NAME = ".list-rst__rst-name-target.cpy-rst-name.js-ranking-num"
RATING = "c-rating__val c-rating__val--strong.list-rst__rating-val"
AREA = ".list-rst__area-genre.cpy-area-genre"
TITLE = ".list-rst__pr-title.cpy-pr-title"
NIGHT_PRICE = ".c-rating__val list-rst__budget-val.cpy-dinner-budget-val"
HIRU_PRICE = ".c-rating__val list-rst__budget-val.cpy-lunch-budget-val"
IMAGE = "js-cassette-imgcpy-main-image"
"""
ログイン
"""
""" browser.get(loginUrl)
browser.find_element_by_id("UserEmail").send_keys(loginName)
browser.find_element_by_id("UserPassword").send_keys(loginPass)
browser.find_element_by_id("login_btn").click()
 """

"""
メイン
"""
browser.get(url)

rank = 1
while True: # 最後のページまで

    if browser.find_element_by_css_selector(PAGE_NEXT).get_attribute("href") is not None:
        posts = browser.find_elements_by_css_selector(POSTS)
        print(len(posts))
        for post in posts:
            try:
                name = post.find_element_by_css_selector(NAME).text
                print(name)
                rating = post.find_element_by_css_selector(RATING).text
                print(rating)
                area = post.find_element_by_css_selector(AREA).text
                print(area)
                title = post.find_element_by_css_selector(TITLE).text
                print(title)
                title = post.find_element_by_css_selector(TITLE).text
                print(title)

                image = post.find_element_by_css_selector(IMAGE).get_attribute("data-original")
                print(image)

                se = pd.Series([title,season,reviewRank,image,gaiyou], df.columns)    
                df = df.append(se, ignore_index=True)
                rank += 1
            except Exception as e:
                print(e)

        # btn = url + "?page=" + str(num)
        btn = browser.find_element_by_css_selector(PAGE_NEXT).get_attribute("href")
        print("go nextpage=" + btn)
        browser.get(btn)
            #browser.get(nextpage)
    else:
        print("end")
        break

#CSV出力
print("CSVの出力")
df.to_csv("scraping/outputRestran.csv")
print("完了")
