
def clip(VAL,MIN,MAX):
    if(VAL<MIN):
        return MIN
    elif(VAL>MAX):
        return MAX
    elif(VAL==MIN):
        return MIN
    elif(VAL==MAX):
        return MAX
    else:
        return round(VAL,2)
def isNear(var,target,threshold):
    diff = var-target
    return abs(diff)<=threshold
