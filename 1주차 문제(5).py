a = int(input("첫 줄의 별 갯수를 입력하세요: "))
for b in range(a, 1, -2):
    print(" "*int((a - b)/2), "*"*b)

print(" "*int(((a-b)/2)+1), "*")
