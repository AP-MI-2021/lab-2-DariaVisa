import math


def is_prime(n):
    """
1.Aflam daca numarul este prim
    :param n: numar intreg
    :return: Daca numarul este prim retruneaza True, iar daca nu este prim False
    """
    if n < 2:
        return False
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
    while is_prime(n) == False:
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


def main():
    print("Exercitiul 1.")
    n = int(input("Adaugati un numar: "))
    print("Ultimul numar prim mai mic decat numarul dat este: ")
    print(get_largest_prime_below(n))
    test_get_largest_prime_below()
    print("Exercitiul 2.")
    print("Alegeti primul numar al unui interval: ")
    start = int(input())
    print("Alegeti ultimul numar al intervalului ales: ")
    end = int(input())
    print("Patratele perfecte din interval sunt: ")
    print(get_perfect_squares(start, end))
    test_get_perfect_squares()


if __name__ == "__main__":

    main()
