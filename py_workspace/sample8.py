#f문자열 예제, 간단한 연산 가능

name = "Yoseph,kim"
age = 30

line = f"나의 이름은 {name}이고, 나이는{age-2} 입니다."
print(line)

#dictionary
dic = {'name':'홍길동 ', 'age':24}

line = f"{dic['name']*2},{dic['age']+2}"
print(line)
print(f'{소수:0.4f}')
print(f'{"H":^10}')
print(f'{"=":*^15}')
