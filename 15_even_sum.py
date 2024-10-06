# sum of even in [0, 100]
sum     = 0
start   = 0
end     = 100 
while start <= end:
    if (start % 2 == 0):
        sum += start
    start += 1
        

print(sum)