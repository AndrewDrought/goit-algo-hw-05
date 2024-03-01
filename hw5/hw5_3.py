import timeit
from pip._vendor import requests


def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)

    badChar = {}
    for i in range(m):
        badChar[ord(pattern[i])] = i;

    s = 0
    while (s <= n - m):
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            print("Патерн знайдено на позиції " + str(s))
            s += (m - badChar.get(ord(text[s + m]), -1) if s + m < n else 1)
        else:
            s += max(1, j - badChar.get(ord(text[s + j]), -1))


def knuth_morris_pratt_search(text, pattern):
    m = len(pattern)
    n = len(text)

    prefix_function = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[j] != pattern[i]:
            j = prefix_function[j - 1]

        if pattern[j] == pattern[i]:
            j += 1

        prefix_function[i] = j

    j = 0
    for i in range(n):
        while j > 0 and pattern[j] != text[i]:
            j = prefix_function[j - 1]

        if pattern[j] == text[i]:
            j += 1

        if j == m:
            print("Патерн знайдено на позиції " + str(i - (m - 1)))
            j = prefix_function[j - 1]


def rabin_karp_search(text, pattern):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    d = 256
    q = 101

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if text[i + j] != pattern[j]:
                    break
            j += 1

            if j == m:
                print("Патерн знайдено на позиції " + str(i))

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q

            if t < 0:
                t = t + q


def measure_time(function, text, pattern):
    start_time = timeit.default_timer()
    function(text, pattern)
    end_time = timeit.default_timer()
    return end_time - start_time

url_1 = "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
url_2 = "https://drive.google.com/uc?export=download&id=13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ"


def text_url(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else ""


text1 = text_url(url_1)
text2 = text_url(url_2)


pattern1 = "пошук"  # Підрядок, який існує в тексті
pattern2 = "ппьсо"  # Вигаданий підрядок

algorithms = [boyer_moore_search, knuth_morris_pratt_search, rabin_karp_search]

for algorithm in algorithms:
    time1 = measure_time(algorithm, text1, pattern1)
    time2 = measure_time(algorithm, text1, pattern2)
    time3 = measure_time(algorithm, text2, pattern1)
    time4 = measure_time(algorithm, text2, pattern2)
    print(f"Час виконання {algorithm.__name__} для тексту 1 і підрядка 1: {time1}")
    print(f"Час виконання {algorithm.__name__} для тексту 1 і підрядка 2: {time2}")
    print(f"Час виконання {algorithm.__name__} для тексту 2 і підрядка 1: {time3}")
    print(f"Час виконання {algorithm.__name__} для тексту 2 і підрядка 2: {time4}")
