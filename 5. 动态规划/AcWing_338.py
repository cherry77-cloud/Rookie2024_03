def countDigitX(n: int, x: int) -> int:
    # 计算 1-n 中任意数字 x 出现的次数  0 <= x <= 9
    digit, result = 1, 0
    high, cur, low = n // 10, n % 10, 0
    
    # 循环处理每一位
    while high or cur:
        if cur < x:
            result += high * digit
        elif cur == x:
            result += high * digit + low + 1
            if x == 0:
                result -= digit if high > 0 else 0
        else:
            result += (high + (x > 0)) * digit
        
        # 更新低位、当前位、高位和位因子
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    
    return result
    

if __name__ == "__main__":
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        if a > b:
            a, b = b, a
        for i in range(10):
            print(countDigitX(b, i) - countDigitX(a - 1, i), end=" ")
        print()
