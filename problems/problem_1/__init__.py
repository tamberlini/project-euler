class Problem:
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these
    multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    """

    def compute_answer(self) -> int:
        multiples_of_3 = {(x + 1) * 3 for x in range(999 // 3)}
        multiples_of_5 = {(x + 1) * 5 for x in range(999 // 5)}

        answer = sum(multiples_of_3 | multiples_of_5)

        return answer
