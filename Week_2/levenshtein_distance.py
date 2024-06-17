# Câu 4


def levenshtein_distance(token1, token2):
    m, n = len(token1), len(token2)

    # Your Code Here
    # Tạo bảng để lưu khoảng cách Levenshtein
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Khởi tạo dòng đầu tiên và cột đầu tiên
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Tính khoảng cách Levenshtein
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i]
                                   [j - 1], dp[i - 1][j - 1])

    distance = dp[m][n]
    # End Code Here

    return distance


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))

# Đáp án: C: 3
