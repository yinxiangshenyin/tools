import webbrowser
import urllib.request as request
while True:
    print("搜索网站：csdn 知乎 quora")
    myinput=input("请输入要查询的词条: ")
    url = 'http://so.csdn.net/so/search/s.do?q=%s' % request.quote(myinput)
    webbrowser.open(url, new=0, autoraise=True)

    url='https://www.zhihu.com/search?type=content&q=%s' % request.quote(myinput)
    webbrowser.open(url, new=0, autoraise=True)

    url='https://www.quora.com/search?q=%s' % request.quote(myinput)
    webbrowser.open(url, new=0, autoraise=True)