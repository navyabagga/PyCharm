def isPrime(a):
    if a > 1:
        for j in range(2, int(a / 2) + 1):
            if (a % j) == 0:
                return False
                break
        else:
            return True
    else:
        return False


n = int(input())
lis = list(map(str, input().split()))
elements = ["Land", "Road", "People", "Stone", "Clouds", "House", "Forest", "Gates", "Water", "Electricity",
            "Agricultural", "Farms", "Shops", "Transport", "Mountains"]
emotion = {"Happy": 10, "Sad": 5, "Neutral": 2, "None": 1}
em = list(map(str, input().split()))
vowels = {"Land": 1, "Road": 2, "People": 3, "Stone": 2, "Clouds": 2, "House": 3, "Forest": 2, "Gates": 2, "Water": 2,
          "Electricity": 4, "Agricultural": 5, "Farms": 1, "Shops": 1, "Transport": 2, "Mountains": 4}
listt = ["Zero","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
ans1 = 0
elements_l1 = []
for i in lis:
    j = 0
    for k in range(len(i)):
        if i[k].isdigit():
            j += 1
        else:
            break
    elements_l1.append([int(i[:j]), i[j:]])
t_s = 0
for i in range(n):
    t_s += elements_l1[i][0] * emotion[em[i]]
t_v = 0
for i in elements_l1:
    t_v += vowels[i[1]] * i[0]
val = 0
if t_v > t_s:
    val = t_v // t_s
else:
    val = t_s // t_v
if isPrime(val):
    print("Yes", listt[val])
else:
    print("No", listt[val])