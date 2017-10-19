
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
    """method that returns true if a value is close to
    a target.
    var         is the input number
    target      is the number you want to get near to
    threshold   is how close you want to get to it"""
    diff = var-target
    return abs(diff)<=threshold
