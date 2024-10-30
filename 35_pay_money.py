def how_to_pay(amount: int, currency: list) -> dict:
    # Tạo một từ điển để lưu số lượng tiền sử dụng
    result = {}

    # Nếu số tiền là 0, trả về từ điển rỗng
    if amount == 0:
        return result

    # Sắp xếp currency theo thứ tự giảm dần để sử dụng số tiền lớn nhất trước
    currency.sort(reverse=True)

    # Duyệt qua từng loại tiền trong currency
    for coin in currency:
        if amount == 0:  # Nếu không còn tiền cần thanh toán, dừng lại
            break
        
        if coin <= amount:  # Nếu loại tiền hiện tại có thể sử dụng
            count = amount // coin  # Tính số lượng loại tiền này cần sử dụng
            result[coin] = count  # Gán số lượng vào từ điển
            amount -= coin * count  # Giảm số tiền còn lại

    # Đảm bảo tất cả các đồng tiền đều có trong kết quả
    for coin in currency:
        if coin not in result:
            result[coin] = 0  # Ghi lại số lượng là 0 nếu không được sử dụng

    return result

# Ví dụ sử dụng
if __name__ == "__main__":
    euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    print(how_to_pay(500, euro))   # {500: 1}
    print(how_to_pay(10, euro))     # {10: 1}
    print(how_to_pay(123, euro))    # {100: 1, 20: 1, 2: 1, 1: 1}
    print(how_to_pay(1, [1, 5]))    # {1: 1, 5: 0}
    print(how_to_pay(1, [1, 5]))    # {1: 1}
