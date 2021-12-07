class solution:
    def search(l,k):
        dic={}
        for i in l:
            tar= k-i
            if tar in dic:
                return True
            
            dic[i]=tar




    l= [int(x) for x in input('Enter the list :').split()]
    k=int(input('Enter the target value: '))
    s= search(l,k)
    print(s)
