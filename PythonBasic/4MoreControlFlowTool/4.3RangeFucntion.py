for i in range(5):
    print(i)


print(list(range(5, 10))) #range(start,end)

print(list(range(0,10,3))) #range(start,end,step)
#also work with negative number
print(list(range(-10,-100,-30)))



a = ['Its','Over','Anakin!','I','have','the','High','Ground']
for i in range(len(a)):
    print(i,a[i])

#we can also use like this 

print(sum(range(0,5)))