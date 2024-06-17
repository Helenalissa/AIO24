# Câu 7


def my_function2(x, y):
    # Your code here
    x.extend(y)
    return x
    # Sử dụng extend để nối y vào x
    # return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]

assert my_function2(list_num1, my_function2(
    list_num2, list_num3)) == ['a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function2(list_num1, my_function2(list_num2, list_num3)))
# Đáp án: A 1 23400

# Câu 8


def my_function3(n):
    # Your code here
    return min(n)


my_list2 = [1, 22, 93, -100]
assert my_function3(my_list2) == -100

my_list2 = [1, 2, 3, -1]
print(my_function3(my_list2))
# Đáp án: C: -1

# Câu 9


def my_function4(m):
    return max(m)


my_list3 = [1001, 9, 100, 0]
assert my_function4(my_list3) == 1001

my_list3 = [1, 9, 9, 0]
print(my_function4(my_list3))
# Đáp án D: 9

# Câu 10


def my_function5(integers, number=1):
    return any(x == number for x in integers)
    # Thực hiện duyệt từng phần tử trong integers, so sánh từng phần tử với number
    # Nếu bằng nhau trả về True, khác nhau trả về False


my_list4 = [1, 3, 9, 4]
assert my_function5(my_list4, -1) == False

my_list4 = [1, 2, 3, 4]
print(my_function5(my_list4, 2))

# C. True

# Câu 11


def my_function6(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var / len(list_nums)


assert my_function6([4, 6, 8]) == 6
print(my_function6())

# A. 1.0

# Câu 12:


def my_function7(data):
    var = []
    for i in data:
        if i % 3 == 0:  # Nếu i chia hết cho 3 thì thêm i vào list var
            var.append(i)
    return var


assert my_function7([3, 9, 4, 5]) == [3, 9]
print(my_function7([1, 2, 3, 5, 6]))

# A 3,6

# câu 13


def my_function8(y):
    var = 1
    while y > 1:
        var *= y  # Nhân var với y
        y -= 1  # Giảm y đi 1 đơn vị
    return var


assert my_function8(8) == 40320
print(my_function8(4))

# C 24

# Câu 14


def my_function9(x):
    return x[::-1]  # Đảo ngược chuỗi x


x = 'I can do it'
assert my_function9(x) == "ti od nac I"

x = 'apricot'
print(my_function9(x))

# b. to..

# Câu 15


def function_helper(x):
    return 'T' if x > 0 else 'N'  # Nếu x > 0 trả về 'T', ngược lại trả về 'N'


def my_function10(data):
    # Sử dụng list comprehension để áp dụng function_helper cho từng phần tử trong data
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function10(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function10(data))

# C tttn

# Câu 16


def function_helper3(x, data):
    if x in data:  # Nếu x có trong data thì trả về 0
        return 0
    return 1  # Ngược lại trả về 1


def my_function11(data):
    res2 = []
    for i in data:
        if function_helper3(i, res2):
            res2.append(i)

    return res2


lst = [10, 10, 9, 7, 7]
assert my_function11(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function11(lst))

# A 981
