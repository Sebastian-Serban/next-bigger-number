import unittest


def next_bigger(n):
    digits = list(str(n))
    pivot = -1
    for i in range(len(digits) - 2, -1, -1):
        if digits[i] < digits[i + 1]:
            pivot = i
            break
    if pivot == -1:
        return -1
    for i in range(len(digits) - 1, pivot, -1):
        if digits[i] > digits[pivot]:
            digits[i], digits[pivot] = digits[pivot], digits[i]
            break
    digits[pivot + 1:] = sorted(digits[pivot + 1:])
    return int(''.join(digits))


class TestNextBigger(unittest.TestCase):

    def test_examples(self):
        self.assertEqual(next_bigger(12), 21)
        self.assertEqual(next_bigger(21), -1)
        self.assertEqual(next_bigger(513), 531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger(414), 441)
        self.assertEqual(next_bigger(144), 414)

    def test_additional_cases(self):
        self.assertEqual(next_bigger(9), -1)
        self.assertEqual(next_bigger(111), -1)
        self.assertEqual(next_bigger(531), -1)
        self.assertEqual(next_bigger(123), 132)
        self.assertEqual(next_bigger(132), 213)

        self.assertEqual(next_bigger(123456789), 123456798)
        self.assertEqual(next_bigger(9876543210), -1)
        self.assertEqual(next_bigger(1234567890), 1234567908)
        self.assertEqual(next_bigger(9876543201), 9876543210)
        self.assertEqual(next_bigger(12345678901234567890), 12345678901234567908)


if __name__ == "__main__":
    unittest.main()
