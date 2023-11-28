# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from lxml import etree
import datetime
import requests

if __name__ == '__main__':
    url="https://top.baidu.com/board?tab=realtime"
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    # 设定返回的数据编码
    response.encoding="utf-8"
    # print(response.text)
    f=open("./baidu.html","w",encoding='utf-8')
    f.write(response.text)
    f.close()
    # 设定解析器类型为html且编码为utf-8,否则直接解析可能会报错
    parser=etree.HTMLParser(encoding="utf-8")
    tree=etree.parse("baidu.html",parser=parser)
    text1=[]
    text2=[]
    for i in range(20):
        text1.append(tree.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div['+str(i+1)+']/div[2]/a/div[1]/text()'))
        text2.append(tree.xpath('//*[@id="sanRoot"]/main/div[2]/div/div[2]/div['+str(i+1)+']/div[1]/div[2]/text()'))
    for i in range(20):
        print(str(text1[i])+",热搜指数:"+str(text2[i]))
    date=datetime.datetime.today()
    print(date)
    f = open("./Topdata.txt", "a", encoding='utf-8')
    f.write("------"+str(date)+"-------\n")
    for i in range(20):
        f.write("Top"+str(i+1)+" "+str(text1[i])+"  热搜指数："+str(text2[i])+"\n")
    f.close()
