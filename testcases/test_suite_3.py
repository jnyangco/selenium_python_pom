# Run test_suite.py python file
# python testcases/test_suite_3.py

import pytest

pytest.main([
            # "testcases/login/TC001_login_test_experiment2_test.py",
             "testcases/login/TC001_login_test_experiment3_test.py",
             "-m", "login"])

# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)