import unittest

# Import test classes
from testcases.login.TC001_login_test import LoginTest
# from testcases.login.TC001_login_test_data_driven import LoginTestDataDriven
# from testcases.login.TC001_login_test_data_driven_csv_file import LoginTestDataDrivenCSVFile
# from testcases.login.TC002_login_failed_data_driven import LoginFailedDataDriven
from testcases.login.TC003_login_and_logout import LoginAndLogout

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginTestDataDriven)
# tc3 = unittest.TestLoader().loadTestsFromTestCase(LoginTestDataDrivenCSVFile)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginFailedDataDriven)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LoginAndLogout)

# Create test suite combining all test classes
# SmokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
# SmokeTest = unittest.TestSuite([tc1, tc2, tc4, tc5])
SmokeTest = unittest.TestSuite([tc1, tc2])
# SmokeTest = unittest.TestSuite([tc1])

# Run Test Suite
# unittest.TextTestRunner(verbosity=2).run(SmokeTest)
unittest.TextTestRunner().run(SmokeTest)