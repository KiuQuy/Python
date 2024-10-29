import unicodedata

def normalize_string(s):
    # Chuyển chuỗi sang dạng NFD để tách dấu phụ khỏi chữ cái

    # NFD: Normalization Form D
    s = unicodedata.normalize('NFD', s)
    print ("s_before:", s)
    # Loại bỏ các ký tự kết hợp (dấu phụ) và các ký tự không phải chữ cái hoặc số
    s = ''.join(char for char in s if not unicodedata.combining(char) and char.isalnum())
    # char for char in s: lap qua tung ki tu trong s
    # if not unicodedata.combining(char) 
    # and char.isalnum()
    # Giu lai cac ki tu neu no khong phai ki tu ket (la ki tu co dau)
    # and char.isalnum(): Giu lai cac ki tu neu no la chu cai hoac so
    # VD: Noé -> Noe
    print("s_after", s)

    # Chuyển về chữ thường
    return s.lower()

def is_anagram(str1, str2):

    # Chuẩn hóa hai chuỗi
    normalized_str1 = normalize_string(str1)
    normalized_str2 = normalize_string(str2)
    print ("Normal: ", normalized_str1, normalized_str2)
    
    # Sap xep cac ki tu mac dinh la tang dan
    return sorted(normalized_str1) == sorted(normalized_str2)

# Kiểm tra hàm với ví dụ
print(is_anagram("funeral", "real fun"))  
print(is_anagram("Marion", "Romain"))     
print(is_anagram("Noé", "One"))           
print(is_anagram("abc", "def"))           
