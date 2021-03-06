from scapy.all import *
import requests
import re

wifi = ''  # 把网卡名字加上
def MacToProduct(MAC):
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    url='https://mac.51240.com/{0}__mac/'.format(MAC)
    response=requests.get(url,headers=header)
    pattern=re.compile(' style="font-size:16px;">(.*?)</td>',re.S)
    results=re.findall(pattern,response.text)
    print(results)
    
while True:
    p = Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst='192.168.0.1/24')
    # ans表示收到的包的回复
    ans, unans = srp(p, iface=wifi, timeout=4)
    print("一共扫描到{0}台主机：" .format(len(ans)))
    #for s in ans:
        #print(s)
    #ans.show()
    # 将需要的IP地址和Mac地址存放在result列表中
    result = []
    for s, r in ans:
        MAC=r[ARP].hwsrc
        #print(MAC)
        MacToProduct(MAC)
    time.sleep(5)
