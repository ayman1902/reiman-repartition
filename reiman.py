import  numpy as np
import matplotlib.pyplot as plt
def repartition(max):
    x =[]
    #plt.axes(projection='polar')
    #for j in range(0,max):
    #    plt.polar(j*(180/np.pi),j,'k.')
    for n in range(0,max+1):
        if n > 1:
            for i in range(2,n):
                if(n%i) == 0:
                    break
            else:
                    x.append(n)
                    #print(n)
    x.sort()
    #print(len(x))
    return len(x)
def sh(n):
    a = []
    b = []
    r = []
    z = []
    for l in range(0,n):
        a.append(l)
        b.append(repartition(l))
    for c in range(1,n):
        r.append(c)
        z.append(c/np.log(c))
    plt.plot(a,b,label="les nombre premier")
    plt.plot(r,z,label="x/log(x)")
    plt.legend()
    plt.show()  
sh(50)
#print(repartition(5))