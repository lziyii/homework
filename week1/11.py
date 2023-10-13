'''输入一个字符串S，去掉其中所有的空格后输出。
例如，“DataScience and Engineering”，去掉空格后为“DataScienceandEngineering”
'''


S = input("请输入一个字符串：")
S_no_spaces = S.replace(" ", "")
print(S_no_spaces)
