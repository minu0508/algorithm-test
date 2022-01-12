## 변수 선언 ##
e = 0
num2 = 1
num3 = 4

## 실행 부분 ##
while e<3 :
    for i in range(1, 10):
        
        for k in range(num2, num3):
            print(k,"*",i,"=", k*i, end="\t")
            
        print()
        
    print("\n")
    e += 1
    num2 += 3
    num3 += 3
