def add_high_precision(s1: str, s2: str) -> str:
    base_size = 9
    BASE = 10 ** base_size
    
    # 切分成小块，转为整数
    num1 = [int(s1[max(0, len(s1) - i - base_size):len(s1) - i]) for i in range(0, len(s1), base_size)]
    num2 = [int(s2[max(0, len(s2) - i - base_size):len(s2) - i]) for i in range(0, len(s2), base_size)]

    carry = 0
    result = []
    max_len = max(len(num1), len(num2))

    # 遍历数字块，执行加法和进位处理
    for i in range(max_len):
        val1 = num1[i] if i < len(num1) else 0
        val2 = num2[i] if i < len(num2) else 0
        sum_val = val1 + val2 + carry
        result.append(sum_val % BASE)
        carry = sum_val // BASE

    # 处理最后的进位
    if carry:
        result.append(carry)

    # 构建结果字符串，注意最高位数字块不进行零填充
    result_str = ""
    for i in reversed(range(len(result))):
        result_str += str(result[i]) if i == len(result) - 1 else f"{result[i]:09d}"
    
    return result_str


def main():
    s1 = input()
    s2 = input()
    print(add_high_precision(s1, s2))


if __name__ == "__main__":
    main()
