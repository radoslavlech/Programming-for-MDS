#!/usr/bin/env python3
# coding: utf8
env = globals().copy()

import sys
import unittest


def runfile(name, skip=16, **kwargs):
    filename = name + '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    source = "\n".join([""] * skip + source.splitlines()[skip:]) + "\n"
    code = compile(source, filename, 'exec')
    vars = kwargs.copy()
    vars['xx'] = ()
    exec(code, env, vars)
    return vars.get('xx')


########################################################################################################################


class TestRoots(unittest.TestCase):
    def assert_roots(self, xx, *ref):
        xx = sorted(xx)
        self.assertEqual(len(xx), len(ref), "Wrong number of results")
        for x, r in zip(xx, ref):
            self.assertAlmostEqual(x, r)

    def test_sample0(self):
        xx = runfile('exercise1', a=1, b=2, c=3)
        self.assert_roots(xx)

    def test_sample1(self):
        xx = runfile('exercise1', a=1, b=-2, c=1)
        self.assert_roots(xx, 1.)

    def test_sample2(self):
        xx = runfile('exercise1', a=3, b=-2, c=-1)
        self.assert_roots(xx, -0.33333333333333, 1.)

    def test_sampleL(self):
        xx = runfile('exercise1', a=0, b=-2, c=1)
        self.assert_roots(xx, 0.5)


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())
