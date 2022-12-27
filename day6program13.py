#ans=[]
#for i in string:
    #if i in 'AEIOUaeiou':
      #  ans.append(i)
#print(*ans)


#ans=[ i  for i in string  if i ==' ']
#print(len(ans))

#string=input()
#ans=[i for i in string if i in 'AEIOUaeiou']
#print(*ans)


#inp=input()
#ans=[]
#for i in inp:
   # if i in '0123456789':
     #   ans.append(i)

#print(*ans)


#inp=input()
#ans=[i for i in inp if i in '0123456789']
#print(*ans)


string='''practice problems for
 list comprehension in python'''
"""ans=[]
for i in string:
    if i not in'AEIOUaeiou':
        ans.append(i)
print(*ans)"""

ans=[i for i in string if i not in 'AEIOUaeiou']
print(*ans)

