from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionTest
from searchtest import SearchTest

assertion_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    "output": "reports/smoke-report",
    "report_name": "smoke-report",
    "combine_reports": True,
    "add_timestamp": False
}


runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)