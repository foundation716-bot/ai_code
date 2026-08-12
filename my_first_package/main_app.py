
from magic_calc import basic_ops
from magic_calc.basic_ops import add
from magic_calc.advanced_ops import power, sqrt, magic_multiply
import magic_calc.basic_ops as myops

result = basic_ops.add(10, 5)
print(result)

# 이미 import한 함수 직접 사용
result = power(2, 3)
result_add = add(10, 5)

print(f"10+5={result_add} 2의 3제곱은 {result}입니다.")