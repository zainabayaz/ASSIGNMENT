arr=[4,0,6,1,7]
process=['p1','p2','p3','p4','p5']
b_time=[5,6,1,6,1]
average=0
ta_time=[0]*5
w_time=[0]*5
t=0
a=0
for i in range(5):
     b=i+1
     for a in range(b,5):
         if arr[i]>arr[a]:
              temp=arr[a]
              arr[a]=arr[i]
              arr[i]=temp
              temp= process[a]
              process[a]=process[i]
              process[i]=temp 
              temp= b_time[a]
              b_time[a]=b_time[i]
              b_time[i]=temp
              
           
     
     t=t+b_time[i]
     ta_time[i]=t-arr[i]  
     w_time[i]=ta_time[i]-b_time[i]
     average=average+ta_time[i]
     print "Turn around time of ",process[i],"is ",ta_time[i]  
     print "waiting time of ",process[i],"is",w_time[i]

average=average/5
print"average turn around time is ", average 
