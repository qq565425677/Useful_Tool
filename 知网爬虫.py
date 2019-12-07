from selenium import webdriver
import re,math,time

#浏览器下载路径设置
options=webdriver.ChromeOptions()
prefs={'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\56542\\Desktop\\'}
options.add_experimental_option('prefs', prefs)

browser=webdriver.Chrome(chrome_options=options)
browser.get('http://www.cnki.net/')
keyword=input('请输入搜索关键字：')
keyword+='\n'
#搜索关键字
browser.find_element_by_id('txt_SearchText').send_keys(keyword)
#转换到搜索结果框架
browser.switch_to_frame('iframeResult')
#获取文献总数
num_of_literature=browser.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[2]/div/div')
num_of_literature=int(re.split(' ',num_of_literature.text)[2])
#设置每页显示50篇文献
browser.find_element_by_xpath('//*[@id="id_grid_display_num"]/a[3]').click()
#获取总页数
totalpages=math.ceil(num_of_literature/50)
######################限制一下页数######################
totalpages=10 if totalpages>10 else totalpages

#for i in range(1,totalpages+1):
#全选当页文献
time.sleep(2)
browser.find_element_by_id('selectCheckbox').click()
#打开新网页
time.sleep(3)
browser.find_element_by_xpath('//*[@id="J_ORDER"]/tbody/tr[2]/td/table/tbody/tr/td[1]/div/a[2]').click()
#获得当前窗口句柄
current_window_handle=browser.current_window_handle
#获得所有窗口句柄
window_handles=browser.window_handles
#切换窗口
browser.switch_to_window(window_handles[1])
#选择Refworks
time.sleep(2)
browser.find_element_by_xpath('//*[@id="SaveTypeList"]/li[6]/span[1]/a').click()
#下载到桌面
time.sleep(2)
browser.find_element_by_id('exportTxt').click()
#关闭当前页
browser.close()
#切换至下一页

