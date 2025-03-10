
#2816 # 250305
n = int(input())
channels = list()
ch1, ch2 = 0, 0
now = 0
for i in range(n):
    channel = input()
    if (channel == "KBS1"):
        ch1 = i
    elif ( channel == "KBS2"):
        ch2 = i
    channels.append(channel)

if (ch1 < ch2):
    if (ch1 != 0):
        print("1"*ch1, end="")
        print("4"*ch1, end="")
        print("1"*ch2, end="")
        print("4"*(ch2-1), end="")
    else:
        print("1"*ch2, end="")
        print("4"*(ch2-1), end="")
else:
    if (ch2 != 0):
        print("1"*ch2, end="")
        print("4"*ch2, end="")
        print("1"*ch1, end="")
        print("4"*ch1, end="")
    else:
        print("1"*ch1, end="")
        print("4"*ch1, end="")

# print(channels)
