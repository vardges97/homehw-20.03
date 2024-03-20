def evens(n):
    ls = []
    for i in range(1,n+1):
        if i%2 == 0:
            ls.append(i)
    return ls
# print(evens(200))

def divs(n):
    ls = []
    for i in range(1,n):
        if n%i ==0:
            ls.append(i)
    return ls
# print(divs(12))

def pyth(n):
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if pow(a, 2) + pow(b, 2) == pow(c, 2):
                    print(str(a) + "," + str(b) + "," + str(c))

# print(pyth(12))

res = [[i*3+j for i in range(1,5)]for j in range(0,4)]
print(res)

transactions = [
('Կարապետ', 'Կարապետյան', 11000, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 13700, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 7200, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 10900, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 6200, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 5000, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 4500, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 2800, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 9430, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 1700, 'aperitivo'),
]

# lis = list(map(lambda x: max(x), transactions))

sales_data = [
{'month': 'January', 'sales': [500, 750, 321, 910, 621, 410, 890, 720, 331, 641, 530, 780]},
{'month': 'February', 'sales': [420, 911, 610, 371, 900, 680, 431, 561, 421, 711, 871, 520]},
{'month': 'March', 'sales': [361, 490, 721, 621, 311, 810, 660, 780, 561, 421, 471, 691]},
{'month': 'April', 'sales': [781, 621, 431, 590, 811, 641, 371, 721, 881, 521, 391, 671]},
{'month': 'May', 'sales': [930, 680, 440, 571, 841, 730, 311, 671, 931, 561, 321, 481]},
{'month': 'June', 'sales': [711, 481, 931, 721, 511, 841, 361, 731, 471, 891, 651, 521]},
{'month': 'July', 'sales': [811, 591, 341, 971, 671, 431, 751, 621, 411, 881, 391, 761]},
{'month': 'August', 'sales': [940, 731, 591, 421, 841, 611, 371, 721, 891, 561, 331, 811]},
{'month': 'September', 'sales': [961, 721, 381, 561, 821, 661, 431, 791, 521, 891, 471, 741]},
{'month': 'October', 'sales': [921, 681, 341, 811, 651, 421, 791, 561, 331, 711, 491, 761]},
{'month': 'November', 'sales': [951, 711, 381, 671, 441, 831, 621, 391, 771, 531, 911, 481]},
{'month': 'December', 'sales': [921, 781, 511]}
]

def salestotal():
    for i in sales_data:
        total={k:v for (k,v) in zip(i.keys(),sum(i.values()))}
    return total

# print(salestotal())


def squares(n):
    x = {i:i**3 for i in range(1,n+1) }
    return x
# print(squares(5))