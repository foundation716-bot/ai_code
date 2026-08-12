# 이 코드는 사용자의 나이를 입력받아 출력하는 코드이다.
age = input("나이를 입력하세요: ")
print("당신의 나이는", age, "세입니다.") # 입력된 나이를 출력

# 변수 선언   
name = "Alice"
print(f"이름: {name}, 나이: {age}")
# 나이 입력받기  
age = int(input("나이를 입력하세요: ") or "20")
# 결과 출력  
print(f"이름: {name}, 나이: {age}")


def calculate_sum(a, b):
    result = a + b # 들여쓰기된 코드 블록
    return result # 같은 레벨의 들여쓰기
result = calculate_sum(10, 5)
if result > 0:
    print("양수입니다") # if문 내부의 들여쓰기된 코드

"""
이 프로그램은 사용자의 정보를 입력 받아 출력하는 기능을 한다.
사용자가 입력한 이름과 나이를 출력하는 간단한 예제이다.
""" 