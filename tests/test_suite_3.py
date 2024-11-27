# Run test_suite.py python file
# python tests/test_suite_3.py

import pytest

pytest.main([
    "tests/login/00_TC001_login_1.py",
    "tests/login/00_TC001_login_2.py",
    "tests/login/test_login_invalid.py",
    "--browser", "firefox"

    # "-m", "login"
    ])

# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)
# "-m", "login" -> useful as @tags to group tests



