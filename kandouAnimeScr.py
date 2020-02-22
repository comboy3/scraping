# -*- coding: utf-8
import pandas as pd

from selenium import webdriver

"""
初期設定
"""
browser = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver\chromedriver.exe")
# df = pd.read_csv("default.csv" index_col=0)
df = pd.DataFrame(columns=["TITLE", "SEASON", "REVIEW_RANK","IMAGE"])
loginUrl = "https://www.anikore.jp/users/login/"
loginName = "slumdank3@gmail.com"
loginPass = "nishihigashi"
url = r"https://www.anikore.jp/tag/%E6%84%9F%E5%8B%95/" #感動ランキング

"""
CSS SELECTER
"""
PAGE_NEXT = ".next"
POSTS = "div.animeSearchResultBody"
TITLE = ".animeTitle"
SEASON = ".openDateRank"
REVIEW_RANK = ".reviewRank"
IMAGE = ".lazyload"

"""
ログイン
"""
browser.get(loginUrl)
browser.find_element_by_id("UserEmail").send_keys(loginName)
browser.find_element_by_id("UserPassword").send_keys(loginPass)
browser.find_element_by_id("login_btn").click()


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
                title = post.find_element_by_css_selector(TITLE).text
                if (str(title).find("映画") >= 0) | (str(title).find("OVA") >= 0) | (str(title).find("OAD") >= 0) :
                    continue
                print(rank)
                print(title)
                season = post.find_element_by_css_selector(SEASON).text
                print(season)
                reviewRank = post.find_element_by_css_selector(REVIEW_RANK).text
                print(reviewRank)
                image = post.find_element_by_css_selector(IMAGE).get_attribute("data-original")
                print(image)

                se = pd.Series([title,season,reviewRank,image], df.columns)    
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
df.to_csv("scraping/outputKandouAnime.csv")
print("完了")
