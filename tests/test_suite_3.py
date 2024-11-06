# Run test_suite.py python file
# python tests/test_suite_3.py

import pytest

pytest.main([
    "tests/login/TC001_login_1_test.py",
    "tests/login/TC001_login_2_test.py",
    "tests/login/TC002_login_negative_test.py",
    "--browser", "firefox"

    # "-m", "login"
    ])

# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)
# "-m", "login" -> useful as @tags to group tests



