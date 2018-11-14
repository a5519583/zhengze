import re

###匹配单个字符###
# 1.匹配某个字符串
# text = 'hello'
# ret = re.match('he', text)  # match从字符串开头开始匹配
# print(ret.group())

# 2..匹配任意单个字符,但是不能匹配换行符 \n
# text = 'hello'
# ret = re.match('.', text)
# print(ret.group())

# 3.\d匹配任意的数字(0-9),等价于[0-9]
# text = '4d3的'
# ret = re.match('\d', text)
# print(ret.group())

# 4.\D匹配任意的非数字,等价于[^0-9]
# text = '收到4d3的'
# ret = re.match('\D', text)
# print(ret.group())

# 5.\s匹配空白字符(\n, \t, \r, 空格)
# text = '\r'
# ret = re.match('\s', text)
# print(ret.group())

# 6.\w匹配(a-z和A-Z以及数字和下划线),等价于[0-9a-zA-Z]
# text = '__2Ssd'
# ret = re.match('\w', text)
# print(ret.group())

# 7.\W匹配\w相反,等价于[^0-9a-zA-Z_]
# text = '+__2Ssd'
# ret = re.match('\W', text)
# print(ret.group())

# 8.[]只要满足中括号中的字符就可以匹配到
# text = '啊02=是1sa341a2对方-_的7dsh2'
# ret = re.match('[^0-8]', text)
# print(ret.group())


###匹配多个字符###
# 9.*匹配0或者任意多个字符
# text = '2132'
# ret = re.match('\d*', text)
# print(ret.group())

# 10.+匹配1或者任意多个字符
# text = '2132'
# ret = re.match('\d+', text)
# print(ret.group())

# 11.?匹配1或0个
# text = '是2132'
# ret = re.match('\d?', text)
# print(ret.group())

# 12.{m}匹配m个字符
# text = '21.3是2'
# ret = re.match('\d{2,4}', text)
# print(ret.group())


###小练习###
# 13.匹配手机号开头是1,第二位是34578,后九位随意
# text = '13688193431'
# ret = re.match('1[34578]\d{9}', text)
# print(ret.group())

# 14.验证邮箱
# text = '455932358@qq.com'
# ret = re.match('\w+@\w+.[a-zA-Z]+', text)
# print(ret.group())

# 15.验证URL
# text = 'https://study.163.com/course/courseLearn.htm?courseId=1004530011#/learn/video?lessonId=1051091331&courseId=1004530011'
# ret = re.match('(http|https|ftp)://[^\s]+', text)
# print(ret.group())


###正则表达式开始/结束/和/或语法###
# 16.^符号,以...开始
# text = 'https://study.163.com/course/courseLearn.htm?courseId=1004530011#/learn/video?lessonId=1051091331&courseId=1004530011'
# ret = re.search('^.*?:', text)
# print(ret.group())

# 17.$符号,以...结束
# text = 'https://study.163.com/course/courseLearn.htm?courseId=1004530011#/learn/video?lessonId=1051091331&courseId=1004530011'
# ret = re.search('11$', text)
# print(ret.group())

# 18.|符号,匹配多个字符或者表达式
# text = 'as|ss|sss'
# ret = re.search('(as|ss|sss|a)', text)
# print(ret.group())

# 19.贪婪(不加?)与非贪婪(加?)
# text = 'dewaaa'
# ret = re.search('[a-zA-Z]+?', text)
# print(ret.group())

# 20.匹配0-100之间的数字
# text = '1'
# ret = re.match('[1-9]\d?$|100$', text)
# print(ret.group())

# 21.转义符号
# text = '萨达ds^f上'
# ret = re.search('\\^[a-z]+', text)
# 或
# ret = re.search(r'\^[a-z]+', text)


###re模块###
# 22.group()和groups()
# text = '萨达ds^f上'
# ret = re.search(r'.*(萨).*(ds).*', text)
# print(ret.groups())

# 23.find_all()
# text = '萨达ds$^f上 收到 32$ 23s$ 额度我a$'
# ret = re.findall('.*?\$', text)
# print(ret)

24.sub()

25.split()

36.compile()