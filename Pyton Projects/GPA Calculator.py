total = 0

print("AA for A, AB for A-, BA for B+, BB for B, BC for B-")
print("CB for C+, CC for C, CD for C-, DC for D+, DD for D")

pyt = input("CS115 :")
eng = input("ENG101 :")
ge100 = input("GE100 :")
mat = input("MATH101 :")
phy = input("PHYS101 :")
tur = input("TURK101 :")

myStr = pyt + eng + ge100 + mat + phy + tur
myInt = 244134

for i in range(0,12,2):
    letGrade = myStr[i] + myStr[i+1]
    k = myInt // (10**(i//2))
    k = k % 10
    print(k)
    if letGrade == 'AA':
        total  += k*4.0
    elif letGrade == 'AB':
        total += k*3.7
    elif letGrade == 'BA':
        total += k*3.3
    elif letGrade == 'BB':
        total += k*3.0
    elif letGrade == 'BC':
        total += k*2.7
    elif letGrade == 'CB':
        total += k*2.3
    elif letGrade == 'CC':
        total += k*2.0
    elif letGrade == 'CD':
        total += k*1.7
    elif letGrade == 'DC':
        total += k*1.3
    elif letGrade == 'DD':
        total += k*1.0
total /= 18
total *= 10000
if (int(total)%100) >= 50:
    total = (total // 100) + 1
    total /= 100
else:
    total //= 100
    total /= 100
print(total)
