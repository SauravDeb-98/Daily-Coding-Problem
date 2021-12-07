class solution:
    def search(l):

        count=0
        res=[]

        for i in l:
            if i<0:
                continue

            count+=1

            res.append(count)
        
        for i in res:
            if i not in l:
                return i






    l= [int(x) for x in input('Enter the list :').split()]
    s=search(l)
    print(s)
