import os,re

path=r'C:\Users\Sun\Desktop\CMA\2017-2019练兵项目\2017-2019练兵项目\涂层厚度检测'
fileList=os.listdir(path)

date=input('日期：')
for i in fileList:
	if ('副本' in i):
		oldname=path+os.sep+i
		newname=i[8:]
		newname=re.split(r' - 副本',newname)
		newname=path+os.sep+date+newname[0]+newname[1]
		os.rename(oldname,newname)

