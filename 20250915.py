# def ojt():
#     import math
    
#     n1, n2 = 10, 34.1
#     print('n1 =', n1, 'n2 =', n2)
#     n1, n2 = n2, n1
#     print('n1 =', n1, 'n2 =', n2)
#     n1 = int(n1)
#     n2 = float(n2)
#     print('n1 =', n1, 'n2 =', n2)
#     print('Result:' + str(n1) + "+" + str(n2))
#     print()
#     a = 100
#     print(a%2 == 0)
#     print(a%3 == 0)
#     print(0.1+0.1+0.1 == 0.3)
#     print(round(0.1+0.1+0.1, 10) == 0.3)
#     print("################################")
#     num=81
#     print(num**0.5 == math.pow(num, 0.5))
#     print(math.pow(num, 0.5)  == math.sqrt(num))

def hundred_digit_after_five_times():
    import random

    a = random.randint(100, 999)

    print("Original number is", a)

    fivetimes = a * 5
    above_hundreds = fivetimes // 100
    hundreds = above_hundreds % 10

    print("Hundred-digit number after five times is", hundreds)


def main():
    hundred_digit_after_five_times()


if __name__ == "__main__":
    main()