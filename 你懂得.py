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
f.write('错误状态,VIP类别,节点类型,名称,地址,端口,密码ID,加密方式,带宽,状态,链接\n')
home=s.xpath('/html/body/div[1]/div/div[2]/div[8]/table/tbody/tr')
for i in home:
    error=i.xpath('./td[3]/span[1]/@title')#错误状态
    VIPtype=i.xpath('./td[1]/span[1]/text()')#年费/包月
    name=i.xpath('./td[1]/span[2]/text()')[0].split(' · ')#名称
    nodetype=name[0]
    if len(name)==3:
        name=name[1]+name[2]
    elif len(name)==2:
        name=name[1]
    else:
        input('请打开网页检查名称')
        exit()	
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
    link=i.xpath('./td[9]/a/@data-content')#链接
    f.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n'%(error[0][9:11],VIPtype[0],nodetype,name,address[0],port[0],key[0],method[0],speed[0],state[0],link[0]))
f.close()

if os.path.exists('你懂得.xlsx'):
    os.remove('你懂得.xlsx')
try:
    excel=com.gencache.EnsureDispatch('Excel.Application')
    csv=excel.Workbooks.Open(r'E:\PYPRA\你懂得.csv')
    excel.Workbooks('你懂得.csv').SaveAs('E:\PYPRA\你懂得.xlsx',ConflictResolution=c.xlLocalSessionChanges,FileFormat=c.xlWorkbookDefault)
    os.remove('你懂得.csv')
    excel.Range('A1').AutoFilter(4,'=*高速*')
    excel.Range('A1').AutoFilter(1,'=*正常*')
    range=excel.Range('A1','K%s'%len(excel.Worksheets("你懂得").UsedRange()))
    range.Sort(excel.Range('J1'),c.xlDescending,Orientation=c.xlSortColumns)
    excel.Columns('A:F').EntireColumn.AutoFit()
    excel.Columns('I:J').EntireColumn.AutoFit()
    excel.Workbooks('你懂得.xlsx').Save()
    excel.Workbooks('你懂得.xlsx').Close()
except Exception as E:
    print(e)