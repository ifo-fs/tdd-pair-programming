# TDD Practice Tasks

## 1 Task Without Mocking

### Task 1: Palindrome Checker

Create a function `is_palindrome(s: str) -> bool` that checks if a given string is a palindrome (reads the same forward and backward).

Example:
```python
is_palindrome("racecar")  # True
is_palindrome("hello")    # False
```

Write unit tests to verify both palindrome and non-palindrome inputs.

---

## 4 Tasks With Mocking

### Task 2: Submit Bitcoin Transaction (Mock `requests.post`)

Create a function `submit_transaction(wallet_id: str, amount: float) -> str` that sends a `POST` request to `https://api.crypto.com/transactions` with JSON body containing `wallet_id` and `amount`, and returns the `transaction_id` from the response.

Example mock response:
```json
{ "transaction_id": "abc123" }
```

Mock `requests.post` in your unit test.

---

### Task 3: Generate Random Password (Mock `random.choice`)

Create a function generate_password(length: int) -> str that generates a random password of a given length using uppercase letters, lowercase letters, and digits.

Mock `random.choice` in your unit test.

---

### Task 4: Read Environment Variable (Mock `os.environ`)

Create a function `get_secret_key() -> str` that reads a value from the environment variable `SECRET_KEY`.

Mock `os.environ` in your unit test to simulate different environment values.

---

### Task 5: Get Current Time (Mock `datetime.datetime.now`)

Create a function `get_current_time() -> datetime` that returns the current system time using `datetime.datetime.now()`.

Mock `datetime.datetime.now()` in your unit test to simulate a fixed timestamp.

---

## Summary Table

| No | Task | Needs Mocking? | What to Mock |
|:--|:--|:--|:--|
| 1 | Palindrome checker | No | - |
| 2 | Submit Bitcoin transaction | Yes | `requests.post` |
| 3 | Send email notification | Yes | `smtplib.SMTP` |
| 4 | Read environment variable | Yes | `os.environ` |
| 5 | Get current time | Yes | `datetime.datetime.now` |

