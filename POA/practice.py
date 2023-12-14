# restoring

def restoring(a,q,m,n,n_len):
    print(f"{n} \t {a} \t {q}")
    if(n==0):
        return f"Quotient is {q} deci={int(q,2)} \nRemainder is {a} dec={int(q,2)}"
    a,q=ls(a,q)
    a=add(a,complement(m.zfill(n_len)))
    if(len(a)!=n_len):
        a=a[1:]
    if(a[0]=="0"):
        q=q.replace('_','1')
    elif(a[0]=="1"):
        a=add(a,m)
        if(len(a)!=n_len):
            a=a[1:]
        q=q.replace('_','0')
    return restoring(a,q,m,n-1,n_len)

def add(a,b):
    result=""
    carry=0
    max_len=max(len(a),len(b))
    a=a.zfill(max_len)
    b=b.zfill(max_len)
    for i in range(max_len-1,-1,-1):
        r=carry
        r+=1 if (a[i]=="1") else 0
        r+=1 if (b[i]=="1") else 0
        result=("1" if (r%2==1) else "0")+result
        carry=0 if r<2 else 1
    if carry !=0:
        result='1'+result
    return result.zfill(max_len)
    
def complement(a):
    res=''
    for i in a:
        if i=="1":
            res+="0"
        elif i =="0":
            res+="1"
    res=add(res,'1')
    return res   

def ls(a,q):
    a=a[1:]+q[0]
    q=q[1:]+"_"
    return a,q

a=int(input("Enter Numerator : "))
b=int(input("Enter Denominator : "))
n=len(bin(max(abs(a),abs(b)))[2:])+1
a=bin(a)[2:].zfill(n) if a>=0 else complement(bin(a)[3:].zfill(n))
b=bin(b)[2:].zfill(n) if b>=0 else complement(bin(b)[3:].zfill(n))
    
print(restoring('0'*n,a.zfill(n),b.zfill(n),n,n))
