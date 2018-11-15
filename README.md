# WeHeartIt_Spider

Python 爬虫实战--WeHeartIt

## 业务逻辑
    def run(self):
        # 1.Find URL
        for i in range(1, self.max_num):
            url = self.temp_url.format(i)
            # 2.Send Request, Get Response
            html = self.parse_url(url)
            # 3.Get item
            if html:
                item = self.parse_html(html)
                # 4.save item
                self.save_item(item)

## 资源展示
{
  "img_src": "https://data.whicdn.com/images/321055677/superthumb.jpg?t=1539956783",
  "name": "Ouissal | وصال",
  "host_src": "https://data.whicdn.com/avatars/29543100/thumb.jpg?t=1535291600",
  "comment": "22"
}

## 项目参考
https://blog.csdn.net/m0_37903789/article/details/84103383
