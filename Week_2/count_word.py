# Câu 3

import requests
import re

# Tải file từ Google Drive
url = 'https://drive.google.com/uc?export=download&id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
response = requests.get(url, stream=True)

# Lưu file vào đĩa
with open('P1_data.txt', 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)


def count_word(file_path):
    counter = {}

 # Your Code Here
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\w+', text)

        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1

 # End Code Here

    return counter


file_path = 'P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
# Đáp án: C 6
