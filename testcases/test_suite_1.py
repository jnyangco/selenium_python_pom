import unittest

# Import test classes
from testcases.login.archived_tests.TC001_login_test_backup_v3_1 import LoginTest
from testcases.login.TC002_login_negative_test import LoginNegativeTest
from testcases.dashboard.TC001_dashboard_ui_verification import DashboardUIVerification

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginNegativeTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(DashboardUIVerification)

# Create test suite combining all test classes
SmokeTest = unittest.TestSuite([tc1, tc2, tc3])

# Run Test Suite
# unittest.TextTestRunner(verbosity=2).run(SmokeTest)
unittest.TextTestRunner().run(SmokeTest)