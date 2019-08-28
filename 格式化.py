from win32com import client as com
from win32com.client import constants as c
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
logging.basicConfig(filename=r'C:\Users\Sun\Desktop\CMA\格式化.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

fi=r'C:\Users\Sun\Desktop\CMA\质量手册 - 副本.docx'
word=com.gencache.EnsureDispatch('Word.Application')
doc=word.Documents.Open(FileName=fi)

try:
	while True:
		word.ActiveDocument.Lists(1).ConvertNumbersToText()
except:
    logging.info("\t编号转文字完成.")
logging.info("\t-----------------------开始替换-----------------------")
word.Selection.Find.ClearFormatting()
word.Selection.Find.Replacement.ClearFormatting()
word.Selection.Find.Execute('^w',False,False,False,False,False,True,1,True,'',2)
logging.info("\t消除空格完成.")
word.Selection.Find.Execute('[0-9].[!0-9]',False,False,True,False,False,True,1,True,'^&dele',2)
word.Selection.Find.Execute('?dele',False,False,True,False,False,True,1,True,' ^&',2)
word.Selection.Find.Execute('dele',False,False,True,False,False,True,1,True,'',2)
logging.info("\t一级标题加空格完成.")
word.Selection.Find.Execute('.[0-9]{1,2}[!.]',False,False,True,False,False,True,1,True,'^&dele',2)
word.Selection.Find.Execute('?dele',False,False,True,False,False,True,1,True,' ^&',2)
word.Selection.Find.Execute('dele',False,False,True,False,False,True,1,True,'',2)
logging.info("\t二、三、四级标题加空格完成.")
word.Selection.Find.Execute('【[0-9]】',False,False,True,False,False,True,1,True,'^& ',2)
logging.info("\t引用文件加空格完成.")


logging.info("\t-----------------------开始设置一级标题-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[0-9]{1,2}.[!0-9]{1,2}'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('标题 1')
	word.Selection.EndKey()
	logging.info("\t第%d个一级标题设置完成" % i)
	i=i+1
logging.info("\t-----------------------开始设置二级标题-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[0-9]{1,2}.[0-9]{1,2}[!.]'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles("标题 2")
	word.Selection.EndKey()
	logging.info("\t第%d个二级标题设置完成" % i)
	i=i+1
logging.info("\t-----------------------开始清空三级标题-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,2}[!.]'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	logging.info("\t第%d个三级标题设置完成" % i)
	i=i+1
logging.info("\t-----------------------开始设置三级标题-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('4.5.[0-9]{1,2}[!.]'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('标题 3')
	word.Selection.EndKey()
	logging.info("\t第%d个三级标题设置完成" % i)
	i=i+1
logging.info("\t-----------------------开始清空四级标题-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,2}.[0-9]{1,2}'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.EndKey(Extend=c.wdExtend)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	logging.info("\t第%d个四级标题设置完成" % i)
	i=i+1
logging.info("\t-----------------------取消[1-9].编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[1-9]、'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('正文')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（一）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（一）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（二）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（二）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（三）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（三）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（四）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（四）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（五）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（五）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------取消（六）.编号-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('（六）'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------设置【】-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('【[1-9]】'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('样式0.0.0.0')
	word.Selection.EndKey()
	i=i+1
logging.info("\t-----------------------设置a-z)-----------------------")
i=1
range=doc.Range(0,0)
range.Select()
while word.Selection.Find.Execute('[a-z]\)'):
	word.Selection.HomeKey()
	word.Selection.MoveEnd(c.wdParagraph)
	word.Selection.Style=word.ActiveDocument.Styles('正文')
	word.Selection.EndKey()
	i=i+1