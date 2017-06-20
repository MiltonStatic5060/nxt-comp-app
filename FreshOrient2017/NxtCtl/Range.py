def clip(INPUT,MIN,MAX):
    if(INPUT<=MIN):
        return MIN
    elif(INPUT>=MAX):
        return MAX
    else:
        return round(input,2)
def isNear(var,target,threshold):
    diff = var-target
    return abs(diff)<=threshold
