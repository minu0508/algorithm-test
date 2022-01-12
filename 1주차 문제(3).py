
x = int(input("x의 좌표를 입력하세요: "))
y = int(input("y의 좌표를 입력하세요: "))

if ( 0 < x ):
    if (0 < y):
        print("1")
    if (0 > y):
        print("4")

if ( 0 > x ):
    if (0 < y):
        print("2")
    if (0 > y):
        print("3")

if ( 0 == x or 0 == y ):
    print("x좌표와 y좌표는 0이 될 수 없습니다.");
