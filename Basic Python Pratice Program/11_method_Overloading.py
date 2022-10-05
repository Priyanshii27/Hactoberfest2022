class Total:
    def sum(self,*a):
        total=0
        for x in a:
            total=total+x
        print('The Sum is:',total)


t=Total()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
t.sum() 