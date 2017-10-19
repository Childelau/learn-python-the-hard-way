str = raw_input()


str_num = 0
spac_num = 0
figue_num = 0

for x in str:
    if x.isalpha():
        str_num += 1
    elif x.isdigit():
        figue_num += 1
    elif x == ' ':
        spac_num += 1
    else:
        pass

other_num = len(str) - str_num - spac_num - figue_num
arr = [1,2,3,4]
print str_num,figue_num,spac_num,other_num

