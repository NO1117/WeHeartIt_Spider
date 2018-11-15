#!/usr/bin/env/ python 
# -*- coding:utf-8 -*-
# Author:Mr.Xu

import requests
import time
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class WeHeartIt():
    max_num = 50
    def __init__(self):
        self.ua = UserAgent()
        self.temp_url = "http://weheartit.com/inspirations/beach?page={}"
        self.headers = {
            "User-Agent": self.ua.random
        }
        self.parse_times = 0

    # 请求相应URL,并返回HTML文档
    def parse_url(self, url):
        response = requests.get(url,headers=self.headers)
        # 请求前睡眠2秒
        time.sleep(2)
        if response.status_code != 200:
            print('parsing not success!--',url)
            # 请求不成功
            if self.parse_times < 3:
                # 重复请求三次
                self.parse_times += 1
                return self.parse_url(url)
            else:
                # 请求不成功, parse_times置为0
                self.parse_times = 0
                return None
        else:
            # 请求成功
            print('parsing success!--',url)
            # 请求成功, parse_times重置为0
            return response.text

    # 解析网页，并提取数据
    def parse_html(self, html):
        item_list = []
        soup = BeautifulSoup(html, 'lxml')
        divs = soup.select("div.entry.grid-item")
        for div in divs:
            title = div.select("span.text-big")[0].get_text()
            img_src = div.select("img.entry-thumbnail")[0].attrs['src']
            temp_name = div.select("a.js-blc-t-user")[0].attrs['href']
            name = temp_name.replace('/', '')
            host_src = div.select("img.avatar")[0].attrs['src']
            comment = div.select("span.js-heart-count")[0].get_text()
            item = dict(
                title=title,
                img_src=img_src,
                name=name,
                host_src=host_src,
                comment=comment,
                )
            print(item)
            item_list.append(item)
        return item_list

    # 保存数据
    def save_item(self, item_list):
        with open('WeHeartIt.txt', 'a+', encoding='utf-8') as f:
            for item in item_list:
                json.dump(item, f, ensure_ascii=False, indent=2)
            f.close()
        print("Save success!")

    # 逻辑实现
    def run(self):
        # 1.Find URL
        for i in range(1, self.max_num):
            url = self.temp_url.format(i)
            # 2.Send Request, Get Response
            html = self.parse_url(url)
            # 3.Get item
            if html:
                item = self.parse_html(html)
                # 4.save information
                self.save_item(item)

if __name__=='__main__':
    spider = WeHeartIt()
    spider.run()

"""
https://weheartit.com/inspirations/beach?page=1
https://weheartit.com/inspirations/beach?page=2
https://weheartit.com/inspirations/beach?page=3
...
https://weheartit.com/inspirations/beach?page=X
"""