# Viết đoạn script tính toán và hiển thị số 
# nguyên tố đầu tiên lớn hơn 100_000_000.
# Bạn có thể sử dụng itertools.count(), 
# và cũng có thể sys.exit().
import itertools
import sys

def is_prime (n):
    if n < 2:
        return False
    else:
        for i in range (2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
def find_first_prime_above(limit):
    for num in itertools.count(limit + 1):  # Bắt đầu từ limit + 1, lặp vô hạn
        if is_prime(num):
            print(num)
            sys.exit()  # Thoát ngay khi is_prime trả về true


find_first_prime_above(100_000_000)
