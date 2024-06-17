# Câu 5


def check_the_number(k):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(str(i))
    list_of_numbers = [str(x) for x in list_of_numbers]
    if k in list_of_numbers:
        results = "True"
    else:
        results = "False"
    return results


k = 7
assert check_the_number(k) == " False "
k = 2
results = check_the_number(k)
print(results)

# Đáp án: D raise an error
