def is_prime(num: int) -> bool:
    """Shows is the number prime or not"""
    if num <= 0:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


def factorial(num: int) -> int:
    """Take note that this function can't work with big numbers"""
    if num == 1:
        return 1
    else:
        return factorial(num - 1) * num


def find_divisors(num: int) -> list:
    """Finds a list of divisors for a num. Also not great for big numbers"""
    if num <= 0:
        return []
    else:
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
    return divisors
