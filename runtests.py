#!/usr/bin/env python
import unittest
from tests import naco_test


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(naco_test.suite())
    return test_suite


runner = unittest.TextTestRunner()
runner.run(suite())
