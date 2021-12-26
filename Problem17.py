#Not a very good one, but eh
dic = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
       10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
       16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
       40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def numtoword(num):
    num = list(map(int, str(num)))
    string = ""
    if len(num) == 1:
        string = dic[num[0]]
    elif len(num) == 2:
        if num[0] == 1:
            string = dic[int(str(num[0]) + str(num[1]))]
        else:
            string = dic[num[0] * 10]
            if num[1] != 0:
                string += dic[num[1]]
    elif len(num) == 3:
        s = int(''.join(map(str, num))) % 10
        t = int(int(''.join(map(str, num))) / 10) % 10
        h = int(int(''.join(map(str, num))) / 100) % 10
        string = f"{dic[num[0]]}hundred"
        if s == 0 and t == 0:
            print(h, t, s)
        elif s == 0:
            string += f"and{dic[num[1] * 10]}"
        elif t == 1:
            string += f"and{dic[int(str(num[1]) + str(num[2]))]}"
        else:
            string += f"and{dic[num[1] * 10]}{dic[num[2]]}"

    else:
        string = "onethousand"
    return string


length = 0
print(len(''))
print(len(numtoword(342)))
words = []
for i in range(1, 1001):
    print(numtoword(i))
    length += len(numtoword(i))
print(length)
