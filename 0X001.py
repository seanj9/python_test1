# -*- coding:utf-8 -*-  
print ('*****************************************************************************')
#\转义'
print ('----------------------------------------------------------')
print ('I\'m ok')
print ('----------------------------------------------------------')
#\\转义\
print ('----------------------------------------------------------')
print ('\\\n\\')
print ('----------------------------------------------------------')
#r''表示''内部的字符串默认不转义
print ('----------------------------------------------------------')
print ('\\\t\\\n\\')
print ('----------------------------------------------------------')
print (r'\\\t\\\n\\')
print ('----------------------------------------------------------')
#'''...'''代替\n
print ('----------------------------------------------------------')
print ('''111
222
333''')
print ('----------------------------------------------------------')
print ('----------------------------------------------------------')
print ('''111
	222
	333''')
print ('----------------------------------------------------------')
print ('*****************************************************************************')