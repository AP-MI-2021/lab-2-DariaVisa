import math


def is_prime(n):
    """
1.Aflam daca numarul este prim
    :param n: numar intreg
    :return: Daca numarul este prim retruneaza True, iar daca nu este prim False
    """
    if n < 2:
        return False
    else: 
        for i in range(2, n-1):
            if n % i == 0:
                return False
    return True


def get_largest_prime_below(n):
    """
Cautam ultimul numar prim mai mic decat numarul dat
    :param n: numar intreg
    :return: ultimul numar prim mai mic decat numarul dat
    """
    n = n - 1
    if n < 2:
        print("nu e bun")
    else:
        while is_prime(n) is False:
            n = n - 1
    return n


def test_get_largest_prime_below():
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(9) == 7
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(3) == 2


def get_perfect_squares(start, end):
    """
12.Functia returneaza toate patratele perfecte din lista
    :param start: numar intreg
    :param end: numar intreg
    :return: o lista
    """
    if start < 0 and end < 0:
        return []
    if start > end:
        return []
    lst = []
    for i in range(start, end+1):
        if i >= 0:
            if int(math.sqrt(i))*int(math.sqrt(i)) == i:
                lst.append(i)
    return lst


def test_get_perfect_squares():
    assert get_perfect_squares(4, 9) == [4, 9]
    assert get_perfect_squares(2, 26) == [4, 9, 16, 25]
    assert get_perfect_squares(15, 1) == []
    assert get_perfect_squares(-20, -1) == []
    assert get_perfect_squares(-2, 10) == [0, 1, 4, 9]


def is_palindrome(n):
    """
Determinam daca un numar dat este palindrom
    :param n: numar luat ca string
    :return: True daca este palindrom si False daca nu este palindrom
    """
    numar = str(n)
    if numar == numar[::-1]:
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(123454321) is True
    assert is_palindrome(123456765) is False
    assert is_palindrome(567898765) is True
    assert is_palindrome(9876789) is True


def main():
    test_get_largest_prime_below()
    test_get_perfect_squares()
    test_is_palindrome()
    while True:
        print("1. Aflam ultimul numar prim mai mic decat numarul dat. ")
        print("2. Aflam toate patratele perfecte dintr-un interval dat. ")
        print("3. Aflam daca numarul este palindrom. ")
        print("x. Iesire")
        optiune = input("Alege exercitiul:")
        if optiune == "1":
            n = int(input("Alegeti un numar: "))
            print("Ultimul numai prim mai mic decat acesta este: ")
            print(get_largest_prime_below(n))
        elif optiune == "2":
            start = int(input("Alege primul numar al unui interval: "))
            end = int(input("Alege ultimul numar al intervalului ales: "))
            print("Patratele perfecte din interval sunt: ")
            print(get_perfect_squares(start, end))

        elif optiune == "3":
            n = input("Alege un numar: ")
            print(is_palindrome(n))
        elif optiune == "x":
            break
        else:
            print("Reincercati")


if __name__ == "__main__":

    main()
