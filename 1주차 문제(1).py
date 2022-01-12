a = int(input("점수를 입력하세요: "))

if ( 100 < a ):
        print("입력값이 올바르지 않습니다.")
elif ( 96 <= a ):
    print("A+")
elif ( 91 <= a ):
    print("A")
elif ( 86 <= a ):
    print("B+")
elif ( 81 <= a ):
    print("B")
elif ( 76 <= a ):
    print("C+")
elif ( 71 <= a ):
    print("C")
elif ( 66 <= a ):
    print("D+")
elif ( 61 <= a ):
    print("D")
elif ( 0 <= a ):
    print("F")
else:
    print("입력값이 올바르지 않습니다.")
