import requests
from bs4 import BeautifulSoup
import re
import os

# 目标URL列表
urls = [
    'https://ip.164746.xyz/ipTop10.html',
    'https://cf.090227.xyz',
    'https://api.uouin.com/cloudflare.html',
    'https://www.wetest.vip/page/cloudflare/address_v4.html',
    'https://stock.hostmonit.com/CloudFlareYes'
]

# 正则表达式用于匹配IP地址
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# 检查ip.txt文件是否存在,如果存在则删除它
if os.path.exists('ip.txt'):
    os.remove('ip.txt')

# 创建一个文件来存储IP地址
with open('ip.txt', 'w') as file:
    for url in urls:
        try:
            # 发送HTTP请求获取网页内容
            response = requests.get(url, timeout=10)
            response.encoding = 'utf-8'

            # 使用BeautifulSoup解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # 根据网站的不同结构找到包含IP地址的元素
            if url in ['https://ip.164746.xyz/ipTop10.html', 'https://cf.090227.xyz']:
                elements = soup.find_all('tr')
            elif url == 'https://api.uouin.com/cloudflare.html':
                elements = soup.find_all('div', class_='ip')
            elif url == 'https://www.wetest.vip/page/cloudflare/address_v4.html':
                elements = soup.find_all('p')
            elif url == 'https://stock.hostmonit.com/CloudFlareYes':
                # 这是一个纯文本页面，不用解析 HTML
                ip_matches = re.findall(ip_pattern, response.text)
                for ip in ip_matches:
                    file.write(ip + '\n')
                continue
            else:
                elements = soup.find_all('li')

            # 遍历所有元素,查找IP地址
            for element in elements:
                element_text = element.get_text()
                ip_matches = re.findall(ip_pattern, element_text)

                # 如果找到IP地址,则写入文件
                for ip in ip_matches:
                    file.write(ip + '\n')

        except Exception as e:
            print(f"处理 {url} 时出错：{e}")

print('IP地址已保存到 ip.txt 文件中。')
