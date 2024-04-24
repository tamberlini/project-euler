from math import sqrt


class Problem:
    """
    The prime factors of 13195 are 5,7,13 and 29.
    What is the largest prime factor of the number 600851475143?
    """

    def compute_answer(self) -> int:
        value = 600_851_475_143

        prime_gen = self.gen_primes()
        while True:
            number = next(prime_gen)
            while True:
                if value % number != 0:
                    break
                value /= number

            if value == 1:
                return number

    @staticmethod
    def gen_primes():
        """ Generate an infinite sequence of prime numbers.
        """
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1