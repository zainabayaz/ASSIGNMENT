a=1
processes=[1,2,3]
bursttime=[10,5,7]
q=2
finish=0
r_bt=[0]*3
done=1
wt_t=[0,0,0]
t=0   

for index in range (3):
       r_bt[index]=bursttime[index]
       

while (a==1) :
   done=1
   for i in range(3):
       if r_bt[i]>0:

          if r_bt[i]>q:
            done=0 
            r_bt[i]=r_bt[i]-q
            t=t+q
          else: 
            t=t+r_bt[i]
            wt_t[i]=t-bursttime[i]
            r_bt[i]=0
   if done==1:
    a=2






for s in range(3):
 print(wt_t[s])


