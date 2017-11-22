
def clip(VAL,MIN,MAX):
    if(VAL<MIN):
        return MIN
    elif(VAL>MAX):
        return MAX
    elif(isNear(VAL,MIN,0.005)):  #elif(VAL==MIN):
        return MIN
    elif(isNear(VAL,MAX,0.005)):  #elif(VAL==MAX):
        return MAX
    else:
        return round(VAL,2)
def isNear(var,target,threshold):
    diff = var-target
    return abs(diff)<=threshold
