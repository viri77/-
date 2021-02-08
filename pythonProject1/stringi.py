psw = input()
a = psw.split(':')
count=0
global_count=0

for i in range(1,int(a[1])+1):
    if int(a[1])%i==0:
       count +=1
if count==2:
    global_count+=1
if a[0]==a[0][-1::-1]  and global_count==1 and int(a[2])%2==0:
           print('True')
else:
    print('False')

#55:75:87