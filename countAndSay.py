

a = 1
def qie(a):
    b = str(a)+"0"
    ans = []
    daan=[]
    c=0
    for i in range(len(b)-1):
        if b[i]==b[i+1]:
            c+=1
        else:
            ans.append(b[i-c:i+1])
            c=0
    for i in ans:

        daan.append(str(len(i))+str(i[0]))
    print("".join(daan))

    return int("".join(daan))


def xunhuan(n):
    if n == 1:
        return 1
    # elif n==2:
    #     return qie(1)

    else:
        return qie(xunhuan(n-1))



xunhuan(6)






