class Sol:
    def printnto1(self,N):
        if N==0:
            return
        print(N)
        self.printnto1(N-1)

s=Sol()
s.printnto1(5)

