a = int(input("등산한 시간(초)을 입력하세요: "))
 
h = int (a/3600)
m = (a - (h*3600)) / 60
s = (a - (h*3600)) % 60

print( "%d시간 %d분 %d초" % (h, m, s))
print( "%d" %h)
print( "%d" %m)
print( "%d" %s)
