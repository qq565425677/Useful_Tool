from win32com import client as com
from win32com.client import constants as c
#import logging

#LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#DATE_FORMAT = "%Y/%m/%d %H:%M:%S %p"
#logging.basicConfig(filename=r'C:\Users\Sun\Desktop\CMA\格式化2.log', level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT)

fi=r'C:\Users\Sun\Desktop\CMA\质量手册 - 副本 - 副本.docx'
word=com.gencache.EnsureDispatch('Word.Application')
doc=word.Documents.Open(FileName=fi)
doc=word.Documents.Open(FileName=fi)

word.Selection.GoTo(What=c.wdGoToPage,Which=c.wdGoToFirst)
word.Selection.GoTo(What=c.wdGoToPage,Which=c.wdGoToNext)
word.Selection.GoTo(What=c.wdGoToPage,Which=c.wdGoToNext)
Page=62
for i in range(Page-3):
	word.ActiveWindow.ActivePane.View.NextHeaderFooter()
	word.Selection.HeaderFooter.PageNumbers.RestartNumberingAtSection=False
	
	#word.Selection.InsertBreak(Type=c.wdSectionBreakContinuous)
