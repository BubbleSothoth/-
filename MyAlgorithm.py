alpha=[3,1,2,1,2,1]
beta=[1,1,2,3,1,2]
omega=[4,4,0,0,4,0]
k=[0,1,4]

def func(x:int,y:int)->int:
    return alpha[x%len(alpha)]+beta[y%len(beta)]

def Algorithm()->(int,int):
    for i in range(6):
        for j in range(6):
            if func(i+k[0],j+k[0])==omega[k[0]] and func(i+k[1],j+k[1])==omega[k[1]] and func(i+k[2],j+k[2])==omega[k[2]]:
                return (i,j)
    return (None,None)
            

if __name__=="__main__":
    print(Algorithm())
        
