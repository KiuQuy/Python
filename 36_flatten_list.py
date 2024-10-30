def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):  # Kiểm tra nếu item là một danh sách
            flat_list.extend(flatten(item))  # Gọi đệ quy để phẳng hóa danh sách con
        else:
            flat_list.append(item)  # Nếu không phải danh sách, thêm phần tử vào flat_list
    return flat_list

# Ví dụ sử dụng
if __name__ == "__main__":
    result = flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []])
    print(result)  # [1, 2, 3, 4, 5, 6, 7, 8]
