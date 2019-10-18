while 1:
    ess1 = int(input("Essay 1(/22) :"))
    ess2 = int(input("Essay 2(/22) :"))
    ess3 = int(input("Essay 3(/22) :"))
    pres = int(input("Oral Presentation(/8) :"))
    diss = int(input("Student Led Discussion(/7) :"))
    ascr = int(input("ASCR(/10) :"))
    refl = int(input("Self-progress Reflection Task(/5) :"))

    total = ess1*15/22 + ess2*15/22 + ess3*15/22 + pres + diss + ascr + refl

    A = (95-total)*2.5*22/100
    AE = (90-total)*2.5*22/100
    BA = (86-total)*2.5*22/100
    B = (82-total)*2.5*22/100
    BE = (78-total)*2.5*22/100
    CA = (74-total)*2.5*22/100
    C = (70-total)*2.5*22/100
    CE = (64-total)*2.5*22/100

    print(str(A)+" for A")
    print(str(AE)+" for A-")
    print(str(BA)+" for B+")
    print(str(B)+" for B")
    print(str(BE)+" for B-")
    print(str(CA)+" for C+")
    print(str(C)+" for C")
    print(str(CE)+" for C-")

