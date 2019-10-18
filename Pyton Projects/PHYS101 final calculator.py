while 1:
    mid1 = int(input("Midterm 1 :"))
    mid2 = int(input("Midterm 2 :"))
    lab = int(input("Laboratory Work(/100) :"))
    quiz = int(input("Average Quiz Score(/10) :"))
    homework = int(input("Homework Score(/100) :"))

    total = (mid1*15 + mid2*20 + lab*20 + quiz*100 + homework*10) / 100
    A = (85-total)*2.5
    Ae = (80-total)*2.5
    Ba = (75-total)*2.5 
    B = (70-total)*2.5
    Be = (65-total)*2.5
    Ca = (60-total)*2.5
    C = (55-total)*2.5
    print(str(A)+" for A")
    print(str(Ae)+" for A-")
    print(str(Ba)+" for B+")
    print(str(B)+" for B")
    print(str(Be)+" for B-")
    print(str(Ca)+" for C+")
    print(str(C)+" for C")
