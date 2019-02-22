

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    l=[]
    s = s.lower()
    if len(s )<= 1:
        return True
    for i in s:
        if i.isalnum():
            l.append(i)
    for i in range(len(l)//2):
        if l[i] != l[-i-1]:
            return False
    return True


s="A man, a plan, a canal: Panama"

print(isPalindrome(s))