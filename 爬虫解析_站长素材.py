import urllib.request
from lxml import etree

def create_request(page):
    if page==1:
        url="https://sc.chinaz.com/tupian/xingganmeinvtupian.html"
    else:
        url = f"https://sc.chinaz.com/tupian/xingganmeinvtupian_{page}.html"
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    }

    request = urllib.request.Request(url=url,headers=headers)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content

def down_load(content):
    tree = etree.HTML(content)

    name_list=tree.xpath('//div[@class="item"]//img/@alt')
    src_list=tree.xpath('//div[@class="item"]//img/@data-original')
    for a in range(len(name_list)):

        name=name_list[a]
        src = src_list[a]


        url='https:'+src
        urllib.request.urlretrieve(url=url,filename=name+'.jpg')



if __name__=="__main__":
    start_page=int(input('请输入起始页码'))
    end_page=int(input("请输入结束页码"))
    for page in range(start_page,end_page+1):

        # 请求对象的定制
        request=create_request(page)
        # 获取内容
        content = get_content(request)

        # 内容下载
        down_load(content)
