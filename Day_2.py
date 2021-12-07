class Solution:
    def ope(l):

        output=[1]*(len(l))
        prod=1
        for i in range(1,len(l)):
            prod=prod*l[i-1]
            output[i]*=prod

        prod=1
        n= len(l)
        for j in range(n-2,-1,-1):
            prod=prod*l[j+1]
            output[j]*=prod
        return output


    
    l= [int(x) for x in input('Enter the list : ').split()]
    op=ope(l)
    print(op)
