from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from search_tests import HomePageTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(HomePageTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)