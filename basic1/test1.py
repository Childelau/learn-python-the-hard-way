n = int(raw_input())
number = [int(x) for x in raw_input().split(' ')]
target = int(raw_input())
list = []
b = 0
for x in number:
    a=b+1
    while a<n:
        if x+number[a] == target:
            list = [b,a]
        a+=1
    b+=1
print ' '.join(str(x+1) for x in list)