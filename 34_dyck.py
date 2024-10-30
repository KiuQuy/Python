
# Tham so truyen vao la string
# Kieu du lieu tra ve la bool
# Khong can ghi cung duoc

def is_a_dyck_word(word: str) -> bool:
    # Neu chuoi rong -> True
    if word == '':
        return True
    
    # [1] Neu chuoi co nhieu hon 2 ki hieu khac nhau -> False
    # set(word): Mot kieu du lieu chi chua cac gia tri duy nhat
    unique_symbols = set(word)
    if len(unique_symbols) != 2:
        return False
    
    # [2] Xac dinh hai ki hieu
    # Do chi con 2 ki hieu nen xac dinh ki hieu dau va cuoi
    open_symbol, close_symbol = list(unique_symbols)
    
    # Hàm kiểm tra nếu một chuỗi là Dyck dựa trên cặp ký hiệu mở và đóng
    # Duyet tu dau den cuoi word, neu co ki hieu mo -> balance + 1, nen khong balance - 1
    def check_dyck(word, open_symbol, close_symbol):
        balance = 0
        for char in word:
            if char == open_symbol:
                balance += 1
            elif char == close_symbol:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    # Kiểm tra cả hai khả năng và trả về True nếu một trong hai là hợp lệ
    return check_dyck(word, open_symbol, close_symbol) or check_dyck(word, close_symbol, open_symbol)


# Test
# Các trường hợp chuỗi Dyck hợp lệ
assert is_a_dyck_word("()") is True
assert is_a_dyck_word("(((())))") is True
assert is_a_dyck_word("()()()()") is True
assert is_a_dyck_word("()(())()") is True
assert is_a_dyck_word("[]") is True
assert is_a_dyck_word("[[]]") is True
assert is_a_dyck_word("{{}}") is True
assert is_a_dyck_word("<<>>") is True
assert is_a_dyck_word("ABAB") is True
assert is_a_dyck_word("AABB") is True
assert is_a_dyck_word("coco") is True
assert is_a_dyck_word("tutu") is True

# Các trường hợp chuỗi Dyck không hợp lệ
assert is_a_dyck_word("(((") is False
assert is_a_dyck_word("((()") is False
assert is_a_dyck_word("()))") is False
assert is_a_dyck_word("()()()(") is False
assert is_a_dyck_word("ABC") is False
assert is_a_dyck_word("AA") is False
assert is_a_dyck_word("AABAA") is False
assert is_a_dyck_word("ABBA") is False
assert is_a_dyck_word("ABBB") is False

# Các trường hợp đặc biệt
assert is_a_dyck_word("") is True  # Chuỗi rỗng
assert is_a_dyck_word(",.") is True  # Các ký hiệu bất kỳ
assert is_a_dyck_word(")(") is True  # Chuỗi ngược lại vẫn hợp lệ
assert is_a_dyck_word("}") is False  # Một ký hiệu đơn lẻ
assert is_a_dyck_word("abcabc") is False  # Hơn hai ký hiệu khác nhau

print("Tất cả các bài kiểm tra đều thành công!")
