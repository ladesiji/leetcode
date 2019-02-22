
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.lstrip()
    mark = True

    if str[0] == '-':
        mark = False
        str = str[1:]

    if str[0].isnumeric():
        if str[1:].isnumeric():
            ans = int(str)
        else:
            for i in range(0, len(str)):
                if not str[i].isnumeric():
                    break
            ans = int(str[0:i])
    else:
        ans = 0
    if mark:
        if ans < 2 ** 31:
            return ans
        else:
            return 2 ** 31 - 1
    else:
        if ans <= 2 ** 31:
            return -ans
        else:
            return -2 ** 31


foo = myAtoi("3.14159")

print(foo)

