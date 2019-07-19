Contributing
============

1. Install development requirements  ::

    pip install -r requirements/dev-requirements.txt


2. Install pre-commit hooks  ::

    pre-commit install


3. To run localserver  ::

    python security_headers.py runserver


4. To get http-observatory scan report, start a separate secure localhost (at 127.0.0.1:8000) to enable https and then navigate to the /scan/<name of url> from runserver  ::

    python security_headers.py runsslserver


5. To run test suite ::

    pytest


6. To test build ::

    tox


7. To make docs locally ::

    cd docs
    make html
