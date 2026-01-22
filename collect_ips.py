import requests
from bs4 import BeautifulSoup
import re
import os
import time

# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

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

# 存储所有IP地址的集合（用于去重）
all_ips = set()

for url in urls:
    try:
        print(f"正在处理: {url}")
        # 发送HTTP请求获取网页内容
        response = requests.get(url, headers=headers, timeout=15)
        response.encoding = 'utf-8'
        
        if response.status_code != 200:
            print(f"  HTTP状态码: {response.status_code}, 跳过")
            continue

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
                all_ips.add(ip)
            print(f"  从{url}找到{len(ip_matches)}个IP")
            continue
        else:
            elements = soup.find_all('li')

        # 遍历所有元素,查找IP地址
        ip_count = 0
        for element in elements:
            element_text = element.get_text()
            ip_matches = re.findall(ip_pattern, element_text)

            # 如果找到IP地址,则添加到集合
            for ip in ip_matches:
                all_ips.add(ip)
                ip_count += 1
        
        print(f"  从{url}找到{ip_count}个IP")
        time.sleep(1)  # 避免请求过快
        
    except requests.exceptions.Timeout:
        print(f"处理 {url} 时超时，跳过")
    except Exception as e:
        print(f"处理 {url} 时出错：{e}")

# 将去重后的IP地址写入文件
with open('ip.txt', 'w') as file:
    for ip in sorted(all_ips):  # 排序后写入
        file.write(ip + '\n')

print(f'总共找到 {len(all_ips)} 个唯一IP地址，已保存到 ip.txt 文件中。')
