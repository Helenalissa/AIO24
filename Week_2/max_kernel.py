# Câu 1

import requests
import re
from collections import deque


def max_kernel(num_list, k):
    result = []
    if not num_list or k > len(num_list):
        return result

    window = deque()

    # xử lý K phần tử đầu tiên của num_list
    for i in range(k):
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        window.append(i)
    # thêm phần từ lớn nhất của cửa sổ đầu tiên vào result
    result.append(num_list[window[0]])

    # xử lý các cửa số tiếp theo
    for i in range(k, len(num_list)):
        # loại bỏ các chỉ số không thuộc cửa số hiên tại
        if window[0] <= i - k:
            window.popleft()

        # loại bỏ các phần tử nhỏ hơn num_list[window[-1]]:
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()

        window.append(i)
        result.append(num_list[window[0]])

    return result


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
# Đáp án A [5, 5, 5, 5, 10, 12, 33, 33]
