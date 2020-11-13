import requests
from lxml  import  etree



def  get_html(url):
    code = requests.get( url )
    if( code.status_code==200 ):
        html_str = code.content.decode('gbk')
        html = etree.HTML( html_str )
        return html
    else:
        print("网站未响应!")
        return None