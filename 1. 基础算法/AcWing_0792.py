def subtract_high_precision(s1: str, s2: str) -> str:
    base_size = 9
    BASE = 10 ** base_size

    num1_bigger = (len(s1) > len(s2)) or (len(s1) == len(s2) and s1 > s2)
    if not num1_bigger:
        s1, s2 = s2, s1

    num1 = [int(s1[max(0, len(s1) - i - base_size):len(s1) - i]) for i in range(0, len(s1), base_size)]
    num2 = [int(s2[max(0, len(s2) - i - base_size):len(s2) - i]) for i in range(0, len(s2), base_size)]

    result = []
    borrow = 0

    for i in range(max(len(num1), len(num2))):
        val1 = num1[i] if i < len(num1) else 0
        val2 = num2[i] if i < len(num2) else 0
        diff = val1 - val2 - borrow
        if diff < 0:
            diff += BASE
            borrow = 1
        else:
            borrow = 0
        result.append(diff)

    while len(result) > 1 and result[-1] == 0:
        result.pop()
        
    if result == [0]:
        return '0'
        
    result_str = ''.join(map(lambda x: f"{x:09d}", reversed(result))).lstrip('0')
    return result_str if num1_bigger else "-" + result_str


def main():
    num1 = input()
    num2 = input()
    print(subtract_high_precision(num1, num2))


if __name__ == "__main__":
    main()
