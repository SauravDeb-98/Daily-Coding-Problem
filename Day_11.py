class solution:
    def search(l,q):

        qlen=len(q)
        res=[]
        for i in l:

            if i[:qlen]==q:
                res.append(i)
            
        return res

        






    l= [str(x) for x in input('Enter the list :').split()]
    q=str(input())
    s=search(l,q)
    print(s)
