# sum of multiple of 3 or 5 and <1000
begin   = 3
end     = 1000
sum     = 0
while begin <= end - 1:
    if(begin % 3 == 0 or begin % 5 == 0):
        sum += begin
    begin += 1
print(sum)