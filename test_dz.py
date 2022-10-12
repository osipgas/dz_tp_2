from dz import _min, _max, _sum, _mult, _file
from unittest import TestCase, main

class Test(TestCase):
    def test__min(self):
        self.assertEqual(_min([1, 1, 3, 1, 1, 0, 0, 8, 0, -20, -13, 1002000, -123, 17, 57, -123.5, 347, 12]), -123.5)

    def test__max(self):
        self.assertEqual(_max([1, 1, 3, 0, 0, 1, 7, 0, -10, 103456, 712, -131, -465.4, 103201.111, 17, 11, 11]), 103456)

    def test__sum(self):
        self.assertEqual(_sum([1, 1, 3, 0, 0, 1, 7, 0, -10, 103456, 712, -131, -465.4, 103201.111, 17, 11]), 206803.711)

    def test__mult(self):
        self.assertEqual(_mult([1, 1, 3, 1, 7, -10, 103456, 712, -131, -465, 10, 17, 11, 11]), -19382665974731136000)



if __name__ == '__main__':
    main()