# 변수의 개수 셈
class Counter:
  def __init__(self):
    self.count = 0

  def num_count(self, num):
    self.count += 1
    return self.count

counter = Counter() # 객체 생성

# 평균계산기 3개
print("평균을 구하고 싶은 세 숫자를 입력하세요.>>")
num1 = int(input("첫 번째 숫자:"))
n = counter.num_count(num1)

num2 = int(input("두 번째 숫자:"))
n = counter.num_count(num2)

num3 = int(input("세 번째 숫자:"))
n = counter.num_count(num3)

sum = num1 + num2 + num3

print(sum/n)



# 숫자 오름차순

# 다음에 계산기 만들어보기 (if부터)

