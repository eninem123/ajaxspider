import requests,re
import json
class MovieSpider(object):

    def __init__(self):
        self.url='http://movie.mtime.com/99547/'
        # 票房是动态加载的，无法直接获取，找到具体的ajax，看评分在json字符串的哪个地方
        self.ajax_url='http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F99547%2F&t=201892510371259778&Ajax_CallBackArgument0=99547'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }

    def get_url_list(self):
        return self.ajax_url

    def get_page_from_url(self,url):
        response = requests.get(url, headers=self.headers)
        # response.encoding='utf8'
        print('response.text:',response.text)
        res = re.findall(r'=(.*?);',response.text)
        # 返回列表，０索引是目标值
        print(res)
        response = re.findall(r'=(.*?);',response.text)[0]
        print(response)
        print("json字符串",type(response))
        # json字符串转字典
        response=json.loads(response)
        print("字典对象：",type(response))
        print(response.get("value").get("boxOffice").get("TotalBoxOffice"))
        response=response.get("value").get("boxOffice").get("TotalBoxOffice")

        return None

    def save_page(self, page):
        file_name='movie.html'
        with open(file_name,'w',encoding='utf8')as f:
            f.write(page)


    def run(self):
        url = self.get_url_list()
        page = self.get_page_from_url(url)
        # self.save_page(page)

if __name__ == '__main__':

    mm = MovieSpider()
    mm.run()
