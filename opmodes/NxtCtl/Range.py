def clip(input,min,max):
    if(input<=min):
        return min
    elif(input>=max):
        return max
    else:
        return round(input,2)
