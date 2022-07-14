def min(list):
    rv = list[0]
    for i in range(0,len(list),1):
        if list[i]<rv:
            rv = list[i]
    return rv

def max(list):
    rv = list[0]
    for i in range(0,len(list),1):
        if list[i]>rv:
            rv = list[i]
    return rv

def avg(list):
    rv = 0
    for i in range(0,len(list),1):
        rv += list[i]
    return (rv)/(len(list))

def sum(list):
    rv = 0
    for i in range(0,len(list),1):
        rv += list[i]
    return rv

def abs(num):
    if num<0:
        return num*(-1)
    elif num>0:
        return num
    else:
        return 0

def find(key,list):
    rv = False
    for i in range(0,len(list),1):
       if list[i] == key:
           rv = True
           return rv
    return False

def even(num):
    if num%2 == 0:
        return True
    else:
        return False

