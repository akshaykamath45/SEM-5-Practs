def restoring(a,q,m,n,n_len):
    print(f"{n} \t\t {a} \t\t {q}")
    if(n==0):
        return f"Quotient = {q} deci = {int(q,2)} \n Remainder = {a} deci = {int(a,2)}"
    a,q=ls(a,q)
    print(f"{n} \t\t {a} \t\t {q} \t after left shift")
    a=add(a,complement(m))
    if(len(a)>n_len):
        a=a[1:]
    print(f"{n} \t\t {a} \t\t {q} \t after A=A-M")
    if(a[0]=="1"):
        print("A<0")
        a=add(a,m)
        if(len(a)>n_len):
            a=a[1:]
        q=q.replace('_','0')
        print(f"{n} \t\t {a} \t\t {q} \t A=A+M , q0=0")
    elif(a[0]=="0"):
         print("A>0")
         q=q.replace('_','1')
         print(f"{n} \t\t {a} \t\t {q} \t  q0=1")
    return restoring(a,q,m,n-1,n_len)

def add(a,b):
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    carry=0
    result=""
    for i in range(max_len-1,-1,-1):
        r=carry
        r+=1 if (a[i]=="1") else 0
        r+=1 if (b[i]=="1") else 0
        result=("1" if r%2==1 else "0") + result
        carry=  0 if r<2 else 1
    if carry!=0:
        result="1"+result
    return result.zfill(max_len)


def complement(a):
     res=""
     for i in a :
         if i=="1":
             res=res+"0"
         elif i == "0" :
             res=res+"1"
     res=add(res,"1")
     return res
 
def ls(a,q):
    a=a[1:]+q[0]
    q=q[1:]+"_"
    return a,q

 
a=int(input('Enter numerator '))
b=int(input('Enter denominator '))
n=len(bin(max(abs(a),abs(b)))[2:])+1
a = bin(a)[2:].zfill(n) if a>=0 else complement(bin(a)[3:].zfill(n))
b = bin(b)[2:].zfill(n) if b>=0 else complement(bin(b)[3:].zfill(n))
print(f"Q={a},M={b},A={'0'*n},Count={n}")
print("Ct\t\tA\t\tQ\t\tAction")
print(restoring('0'*n,a.zfill(n),b.zfill(n),n,n))
