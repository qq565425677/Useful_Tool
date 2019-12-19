from selenium import webdriver,common
import re,math,time,os
import random as r

downloadposition='/home/far/PythonPractice/知网下载'

def txtmerge(path):
    os.chdir(path)
    os.system('type *.txt > download_all.txt')
    files=os.listdir()
    for f in files:
        if 'CNKI' in f:
            os.remove(f)          

#浏览器下载路径设置
options=webdriver.ChromeOptions()
prefs={'profile.default_content_settings.popups': 0, 'download.default_directory':downloadposition}
options.add_experimental_option('prefs', prefs)

browser=webdriver.Chrome(chrome_options=options,executable_path='/home/far/PythonPractice/chromedriver')
browser.get('http://www.cnki.net/')
keyword=input('请输入搜索关键字：')
keyword+='\n'
#搜索关键字
browser.find_element_by_id('txt_SearchText').send_keys(keyword)
#转换到搜索结果框架
time.sleep(3+r.random())
browser.switch_to_frame('iframeResult')
#获取文献总数
strnum_of_literature=browser.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div')
strnum_of_literature=re.split(' ',strnum_of_literature.text)[2]
strnum_of_literature=re.split(',',strnum_of_literature)
num_of_literature=''
for i in strnum_of_literature:
    num_of_literature+=i
num_of_literature=int(num_of_literature)
print("找到文献",num_of_literature,'篇')
#设置按相关性排序
browser.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[1]/td/table/tbody/tr/td[1]/span[2]/a').click()
#设置每页显示50篇文献
time.sleep(2+r.random())
browser.find_element_by_xpath('//*[@id="id_grid_display_num"]/a[3]').click()
#获取总页数
totalpages=math.ceil(num_of_literature/50)
######################限制一下页数######################
totalpages=20 if totalpages>20 else totalpages

input(1)
#browser.switch_to_frame('iframeResult')

#开始下载
for i in range(0,10000):
    #全选当页文献
    try:
        while browser.find_element_by_id('selectCount').text=='0':
            time.sleep(2+r.random()-0.5)
            browser.execute_script('arguments[0].click();',browser.find_element_by_id('selectCheckbox'))
    except common.exceptions.NoSuchElementException as ne:
        input('请调整页面，按回车继续')
        continue
    #打开新网页
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[1]/div/a[2]').click()
    #获得当前窗口句柄
    current_window_handle=browser.current_window_handle
    #获得所有窗口句柄
    window_handles=browser.window_handles
    #切换窗口
    browser.switch_to_window(window_handles[1])
    #选择Refworks
    time.sleep(2+r.random()-0.5)
    browser.find_element_by_xpath('//*[@id="SaveTypeList"]/li[6]/span[1]/a').click()
    #下载到桌面
    time.sleep(2+r.random()-0.5)
    browser.find_element_by_id('exportTxt').click()
    #关闭当前页
    browser.close()
    #清楚当前页候选
    browser.switch_to_window(current_window_handle)
    browser.switch_to_frame('iframeResult')
    while browser.find_element_by_id('selectCount').text!='0':
        time.sleep(2+r.random()-0.5)
        browser.execute_script('arguments[0].click();',browser.find_element_by_class_name('zero'))
        #browser.execute_script('arguments[0].click();',browser.find_element_by_id('selectCheckbox'))
    time.sleep(2+r.random()-0.5)
    for j in range(1,13):
        try:
            controlpage=browser.find_element_by_xpath('//*[@id="ctl00"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/a[%d]'%(j))
            if controlpage.text=='下一页':
                controlpage.click()
                break
        except common.exceptions.NoSuchElementException as ne:
            if controlpage.text==str(totalpages-1):
                input('下载完毕')
                txtmerge(downloadposition)
                exit()
        except BaseException as be:
                print('----------------------------',be)
                input()
input('下载完毕')
txtmerge(downloadposition)


