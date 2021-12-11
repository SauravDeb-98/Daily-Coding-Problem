class solution:
    def search(l):
        first=0
        second=0
        mx=0
        for i in range(len(l)):

            mx= max(l[i]+second,first)

            second= first
            first = mx
        return first






    l= [int(x) for x in input('Enter the list :').split()]
    s=search(l)
    print(s)
