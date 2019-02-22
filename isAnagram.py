"""
    给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

    示例 1:

    输入: s = "anagram", t = "nagaram"
    输出: true
    示例 2:

    输入: s = "rat", t = "car"
    输出: false
    说明:
    你可以假设字符串只包含小写字母。


"""



def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dicts = {}
    dictt = {}

    for i in s:
        if dicts.__contains__(i):
            dicts[i] += 1
        else:
            dicts[i] = 1
    for i in t:
        if dictt.__contains__(i):
            dictt[i] += 1
        else:
            dictt[i] = 1
    for i in list(set(s + t)):
        if dicts[i] != dictt[i]:
            return False
    return True


foo = isAnagram('aab', 'baa')

print(foo)
