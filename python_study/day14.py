from time import time
from threading import Thread
import requests

class download_handler(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('E:/LH/' + filename, 'wb') as f:
            f.write(resp.content)

def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=c93c726aa79ee188f1ae69db8b8a0611&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    print(data_model)
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        download_handler(url).start()
    pass

if __name__ == '__main__':
    main()