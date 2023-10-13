#判断一个输入的字符串S，是否包含由两个或两个以上连续出现的相同字符组成的字符串。例如，abccccda中就包含cccc这个由4个连续字符组成的字符串。

def check_consecutive_chars(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False

S = input("请输入一个字符串：")
if check_consecutive_chars(S):
    print("包含")
else:
    print("不包含")

