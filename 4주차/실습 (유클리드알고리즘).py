# 정수 A와 B의 최대 공약수 (a>= b>0) 을 G(a,b) 라고 하면
# if b== 0, 종료, a가 최대 공약수
# a= b, b= a%b
#이 행위를 반복한 값이 결국 a와 b의 최대 공약수임
a, b = map(int, input("큰 수를 처음에 넣어주십시오.").split())
if b > a:
    print("나쁜 사람! 오류 만들려고!")
    a, b = b, a
while b!=0:
    tempn= a
    a = b
    b = tempn%b
print("최대공약수는 %d 입니다." %a)