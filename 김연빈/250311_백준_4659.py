# 비밀번호 발음하기

# 모음 1개
# 연속3 ㄴㄴ
# 같은 글자 두번x, e,o예외

while True:
    word = input()
    if (word=="end"):
        break
    vowels = ['a', 'e', 'i', 'o', 'u']
    flag = True # True면 가능
    v_flag = False # True면 가능
    cnt = 0
    cnt_flag = False # True면 모음
    for i in range(len(word)):
        is_v = False # True면 모음
        if (word[i] in vowels):
            v_flag = True
            is_v = True
        if (i==0):
            cnt = 1
            if (is_v==False):
                cnt_flag = False
            else:
                cnt_flag = True
        else:
            if (cnt_flag==True): # 연속-모음
                if (is_v==False):
                    cnt_flag = False
                    cnt = 1
                else:
                    cnt += 1
            else:
                if (is_v==False):
                    cnt += 1
                else:
                    cnt_flag = True
                    cnt = 1
            if (cnt>2):
                flag = False
                break
            if (word[i]==word[i-1]):
                if (word[i]=='e' or word[i]=='o'):
                    pass
                else:
                    flag = False
    if (flag==True and v_flag==True):
        print('<'+word+'> is acceptable.')
    else:
        print('<'+word+'> is not acceptable.')