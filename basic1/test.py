str = raw_input()
str = str.split(' ')

index = 0
key1 = []
key2 = []
value1 = []
value2 = []
while index<len(str):
    temp = str[index]
    if (index+1)%3!=0 and (index+1)%2==0:
        value1.append(temp)
        key1.append(index)
    elif (index+1)%3==0:
        value2.append(temp)
        key2.append(index)
    index+=1

value2 = sorted(value2,reverse=True)
value1 = sorted(value1)


key = key1 + key2
value = value1 + value2
index = 0
while index<len(key):
    x = key[index]
    str[x] = value[index]
    index+=1

str = ' '.join(str)
print str