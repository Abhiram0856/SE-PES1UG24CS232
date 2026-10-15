# Lab 5: Static Code Analysis — Employee Payroll System

## Issue Documentation

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval() | Security | 42 | eval() can execute arbitrary expressions. | Removed eval() and calculate net salary using the employee's tax rate. |
| Weak MD5 hash | Security | 47 | MD5 is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Shell command execution | Security | 58 | os.system() can introduce command injection risks. | Removed shell execution and used pathlib for file handling. |
| Insecure random token | Security | 51 | random is not intended for security-sensitive tokens. | Used the secrets module to generate the token. |
| Bare except | Code quality | 26 | Catches errors without identifying their type. | Added input validation and removed the broad exception handler. |
| Mutable default argument | Code quality | 15 | A shared default list can retain data between calls. | Changed the default to None and initialized the list inside the function. |
| Unused import and variables | Code quality | 6, 31, 41 | Unused code reduces readability. | Removed unused imports and variables. |
| Incorrect naming and missing docstrings | Style | Multiple | Naming and documentation did not follow Python conventions. | Used snake_case and added function docstrings. |
| Missing encoding and file handling | Code quality | 55 | File operations did not explicitly specify encoding or use a context manager. | Used pathlib and a context manager with UTF-8 encoding. |

## Before and After Results

| Tool | Before | After |
|---|---|---|
| Pylint | 5.32/10 | 10.00/10 |
| Bandit | 5 findings | No issues identified |
| Flake8 | 7 reported issues | No issues reported |

## Conclusion

Static code analysis helped identify security risks, coding mistakes, and style violations. After fixing the identified issues, the program achieved a Pylint score of 10.00/10, Bandit reported no issues, and Flake8 reported no violations. The corrected program also ran successfully.