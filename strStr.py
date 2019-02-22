
# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     ans = ""
#     if len(needle) == "":
#         return 0
#     if needle in haystack:
#         if len(needle) == len(haystack):
#             return 0
#         else:
#             for i in range(len(haystack)):
#
#                 ans = haystack[i:i + len(needle)]
#                 if haystack[i:i + len(needle)] == needle:
#                     return i
#     else:
#         return -1



def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n = len(needle)

    if n == 0:
        return 0

    for i in range(len(haystack)):
        if haystack[i:i + n] == needle:
            return i
    return -1

a= "mississippi"
b= "pi"
print(strStr(a,b))