import requests,os
from lxml import etree
from win32com import client as com
from win32com.client import constants as c

url='你懂得'
cookie='你懂得'
cookies={i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
data=requests.get(url,cookies=cookies).text
s=etree.HTML(data)
f=open(r'你懂得.csv','w',encoding='ANSI')
f.write('错误状态,VIP类别,名称,地址,端口,密码ID,加密方式,带宽,状态\n')
home=s.xpath('/html/body/div[1]/div/div[2]/div[8]/table/tbody/tr')
for i in home:
    error=i.xpath('./td[3]/span[1]/@class')#错误状态
    error=error[0].split()[1].split('-')[2]
    VIPtype=i.xpath('./td[1]/span[1]/text()')#年费/包月
    name=i.xpath('./td[1]/span[2]/text()')#名称
    address=i.xpath('./td[2]/span/span[2]/text()')#地址
    port=i.xpath('./td[3]/span[2]/text()')#端口
    key=i.xpath('./td[4]/span/text()')#密码ID
    if not key:
        key=i.xpath('./td[4]/span/@data-content')
    method=i.xpath('./td[5]/span/text()')#加密
    if not method:
        method=i.xpath('./td[5]/span/@data-content')
    speed=i.xpath('./td[6]/text()')#带宽
    state=i.xpath('./td[8]/span/text()')#状态
    f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(error,VIPtype[0],name[0],address[0],port[0],key[0],method[0],speed[0],state[0]))
f.close()

if os.path.exists('你懂得.xlsx'):
    os.remove('你懂得.xlsx')

excel=com.gencache.EnsureDispatch('Excel.Application')
csv=excel.Workbooks.Open('你懂得.csv')
excel.Workbooks('你懂得.csv').SaveAs('你懂得.xlsx',ConflictResolution=c.xlLocalSessionChanges,FileFormat=c.xlWorkbookDefault)
os.remove('你懂得.csv')
excel.Range('A1').AutoFilter(3,'=*Trojan*',c.xlAnd,'=*高速*')
range=excel.Range('A1','I%s'%len(excel.Worksheets("你懂得").UsedRange()))
range.Sort(excel.Range('I1'),c.xlDescending,Orientation=c.xlSortColumns)
excel.Columns('A:E').EntireColumn.AutoFit()
excel.Columns('H:I').EntireColumn.AutoFit()
excel.Workbooks('你懂得.xlsx').Save()