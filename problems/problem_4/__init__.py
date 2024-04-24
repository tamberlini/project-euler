from math import sqrt


class Problem:
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
    numbers is 9009=91×99. Find the largest palindrome made from the product of two 3-digit numbers.
    """

    def compute_answer(self) -> int:
        n_digits = 4
        biggest_n_digit_number = int('9' * n_digits)
        smallest_n_digit_number = int('1' + '0' * (n_digits - 1))
        biggest_product = None

        for number_1 in range(smallest_n_digit_number, biggest_n_digit_number + 1):
            for number_2 in range(smallest_n_digit_number, biggest_n_digit_number + 1):
                product = number_1 * number_2
                if self.is_palindrome(product):
                    if biggest_product is None:
                        biggest_product = product
                    else:
                        biggest_product = max(biggest_product, product)

        return biggest_product

    def is_palindrome(self, number: int) -> bool:
        return str(number) == str(number)[::-1]
