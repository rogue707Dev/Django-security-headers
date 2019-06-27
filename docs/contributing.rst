Contributing
============

1. Install development requirements  ::

    pip install -r requirements/dev-requirements.txt


2. Install pre-commit hooks  ::

    pre-commit install


3. To run localserver  ::

    python security_headers.py runserver


4. To run tests or to get http-observatory scan report, start a secure localhost (at 127.0.0.1:8000) to enable https ::

    python security_headers.py runsslserver


5. Run test suite as a separate process ::

    pytest
