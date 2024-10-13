#   Viết hàm chọn sinh viên được chấp nhận và bị từ chối theo một ngưỡng.
#   Hàm phải được gọi select_studentvà nhận hai đối số:
#   một danh sách trong đó mỗi phần tử là danh sách gồm hai phần tử: tên và lớp của một học sinh,
#   một ngưỡng. Điểm của học sinh phải lớn hơn hoặc bằng ngưỡng để được chấp nhận.
#   Hàm của bạn sẽ trả về một từ điển chứa hai mục:
#   "Accepted" : danh sách sinh viên trúng tuyển sắp xếp theo cấp lớp giảm dần.
#   "Refused" : danh sách sinh viên bị loại sắp xếp theo điểm tăng dần

def select_student(students, threshold):
    accepted = []
    refused = []

    # Phân loại sinh viên vào danh sách Accepted hoặc Refused dựa trên ngưỡng
    for student in students:
        name, score = student
        if score >= threshold:
            accepted.append(student)
        else:
            refused.append(student)

    # Sắp xếp danh sách Accepted theo điểm giảm dần
    accepted.sort(key=lambda x: x[1], reverse=True)

    # Sắp xếp danh sách Refused theo điểm tăng dần
    refused.sort(key=lambda x: x[1])

    # Tạo từ điển kết quả
    result = {
        "Accepted": accepted,
        "Refused": refused
    }

    return result

# Example usage
my_class = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]

print(select_student(my_class, 20))

print(select_student(my_class, 50))
