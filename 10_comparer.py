the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]
max = the_list[0]
for i in range(len(the_list)):
    if (max < the_list[i]):
        max = the_list[i]
print(max)
