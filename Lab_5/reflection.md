# Lab 5: Static Code Analysis — Reflection

### 1. What is static code analysis?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, and coding style violations.

### 2. What issues did you find?

Pylint identified issues such as a mutable default argument, a bare exception handler, unused variables, missing docstrings, and unsafe use of eval(). Bandit identified security concerns involving MD5, random token generation, eval(), and shell execution. Flake8 reported formatting and code quality issues.

### 3. How did you fix the issues?

I replaced eval() with a direct salary calculation, changed MD5 to SHA-256, used the secrets module for token generation, removed shell execution, fixed exception handling, corrected naming conventions, and removed unused code.

### 4. How did static analysis improve the program?

Pylint improved from 5.32/10 to 10.00/10. Bandit reported no issues after the changes, and Flake8 reported no violations. The program continued to execute successfully after the fixes.

Static analysis improves code quality, security, readability, and maintainability before the software is deployed.