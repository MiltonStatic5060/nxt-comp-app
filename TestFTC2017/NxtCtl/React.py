class ReactCtl(object):
    CURRSTATE = {}
    PREVSTATE = CURRSTATE.copy()

    def __init__(self):
        pass

    def is_diff(self,ident,initial,newest):
        # returns boolean of whether the values of CURRSTATE and PREVSTATE
        # have changed at all at the identity given
        
        
        if ident not in self.CURRSTATE:
            self.CURRSTATE[ident] = initial
            self.PREVSTATE[ident] = initial
            self.PREVSTATE[ident] = self.CURRSTATE[ident]

        # self.CURRSTATE[ident] = newest
        # result = self.CURRSTATE[ident]==self.PREVSTATE[ident]
        # self.PREVSTATE[ident] = self.CURRSTATE[ident]
        # return not result

        return self.update(ident,newest)

    def get_val(self,ident):
        return self.CURRSTATE[ident] if ident in self.CURRSTATE else 0
    
    def update(self,ident,value):
        # changes value at identity
        # returns boolean true if there was a difference
        self.CURRSTATE[ident] = value
        result = self.CURRSTATE[ident]==self.PREVSTATE[ident]
        self.PREVSTATE[ident] = self.CURRSTATE[ident]
        return not result

react = ReactCtl()