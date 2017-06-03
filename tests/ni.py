import datetime
f=open("inner_time","a")
for i in range(9):
    a=datetime.datetime.now()
    f.write(str(i))
    b=datetime.datetime.now()
    f.write(str(b-a))
