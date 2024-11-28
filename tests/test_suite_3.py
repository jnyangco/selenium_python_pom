# TEST SUITE - using PYTHON FILE
# Run test_suite.py python file
# cmd: python tests/test_suite_3.py

import pytest

pytest.main([
    "tests/login/test_login.py",             # using python files to run
    "tests/login/test_login_header.py",    # using python files to run
    "--browser", "chrome",                   # browser
    "-n", "auto",                            # parallel run
    # "-m", "login"                          # usings tags to run
    "-v"                                     # verbose
    ])


# NOTE: "-m", "login" -> OPTIONAL - we can run just to specify test cases using .py files (without @pytest.mark.<custom_mark_name>)
# "-m", "login" -> useful as @tags to group tests



