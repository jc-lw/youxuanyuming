import requests
from bs4 import BeautifulSoup
import re
import os

def fetch_page_content(url):
    """获取网页内容，返回 BeautifulSoup 对象"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f'请求失败: {url}, 错误: {e}')
        return None

def extract_ips(soup, url):
    """从网页内容中提取符合要求的 IP 地址"""
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    
    if not soup:
        return []
    
    # 根据 URL 选择合适的标签
    elements = soup.find_all('tr') if url in urls else soup.find_all('li')
    
    valid_ips = []
    for element in elements:
        text = element.get_text()
        ip_matches = re.findall(ip_pattern, text)
        
        # 检查是否包含速度信息，并筛选速度不为 0 的 IP
        speed_match = re.search(r'速度[:：]?\s*(\d+(?:\.\d+)?)', text)
        if not speed_match or float(speed_match.group(1)) > 0:
            valid_ips.extend(ip_matches)
    
    return valid_ips

def save_ips(ip_list, filename='ip.txt'):
    """将 IP 地址列表保存到文件"""
    with open(filename, 'w') as file:
        file.write('\n'.join(ip_list))
    print(f'IP 地址已保存到 {filename} 文件中。')

if __name__ == "__main__":
    urls = [
        'https://ip.164746.xyz/ipTop10.html',
        'https://cf.090227.xyz'
    ]
    
    if os.path.exists('ip.txt'):
        os.remove('ip.txt')
    
    all_ips = []
    for url in urls:
        soup = fetch_page_content(url)
        all_ips.extend(extract_ips(soup, url))
    
    save_ips(all_ips)
