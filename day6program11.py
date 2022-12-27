"""import time

inpNo=int(input("Enter a no: "))
start=time.time()
for i in range(inpNo):
    print("i=",i,"1^8=",i*i)
print("Time taken by loop:",(time.time()-start)*1000)"""




"""ans=[i for i in range(1,1001)if i%8==0]
print(ans)"""


"""print([ i for i in range(1,1001) if i%8==0 ])"""


s=50
e=100
print([ i for i in range(s,e+1) if i%2==0 ])
