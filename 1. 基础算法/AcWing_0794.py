def division_high_precision(A: str, B: str) -> str:
    base_size = 9
    BASE = 10 ** base_size
    
    split_number = lambda num: [int(num[max(i-base_size, 0):i]) for i in range(len(num), 0, -base_size)][::-1]
    a_parts = split_number(A)
    b = int(B)
    
    remainder = 0
    result = []
    for part in a_parts:
        current = remainder * BASE + part
        result.append(current // b)
        remainder = current % b
    if result:
        final_result = [str(result[0])]
        final_result.extend(f"{num:09d}" for num in result[1:])
        quotient = ''.join(final_result).lstrip('0') or '0'
    else:
        quotient = '0'
    return quotient, remainder


if __name__ == "__main__":
    A = input()
    B = input()
    
    quotient, remainder = division_high_precision(A, B)
    print(quotient)
    print(remainder)
