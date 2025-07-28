
# 🐍 Python String Methods

Python provides a set of built-in methods that we can use to alter and modify the strings.

---

### `upper()`
The `upper()` method converts a string to upper case.

```python
str1 = "AbcDEfghIJ"
print(str1.upper())
```

**Output:**
```
ABCDEFGHIJ
```

---

### `lower()`
The `lower()` method converts a string to lower case.

```python
str1 = "AbcDEfghIJ"
print(str1.lower())
```

**Output:**
```
abcdefghij
```

---

### `strip()`
The `strip()` method removes any white spaces before and after the string.

```python
str2 = " Silver Spoon "
print(str2.strip())
```

**Output:**
```
Silver Spoon
```

---

### `rstrip()`
The `rstrip()` removes any trailing characters.

```python
str3 = "Hello !!!"
print(str3.rstrip("!"))
```

**Output:**
```
Hello
```

---

### `replace()`
The `replace()` method replaces all occurrences of a string with another string.

```python
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```

**Output:**
```
Silver Moon
```

---

### `split()`
The `split()` method splits the given string at the specified instance and returns the separated strings as list items.

```python
str2 = "Silver Spoon"
print(str2.split(" "))  # Splits the string at the whitespace " ".
```

**Output:**
```
['Silver', 'Spoon']
```

---

### `capitalize()`
The `capitalize()` method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.

```python
str1 = "hello"
print(str1.capitalize())

str2 = "hello WorlD"
print(str2.capitalize())
```

**Output:**
```
Hello
Hello world
```

---

### `center()`
The `center()` method aligns the string to the center as per the parameters given by the user.

```python
str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(str1.center(50, "."))
```

**Output:**
```
            Welcome to the Console!!!            
............Welcome to the Console!!!.............
```

---

### `count()`
The `count()` method returns the number of times the given value has occurred within the given string.

```python
str2 = "Abracadabra"
print(str2.count("a"))
```

**Output:**
```
4
```

---

### `endswith()`
The `endswith()` method checks if the string ends with a given value.

```python
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))
```

**Output:**
```
True
True
```

---

### `find()`
The `find()` method searches for the first occurrence of the given value and returns the index. Returns -1 if not found.

```python
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("Daniel"))
```

**Output:**
```
10
-1
```

---

### `index()`
The `index()` method searches for the first occurrence of the given value. Raises an exception if not found.

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# print(str1.index("Daniel"))  # Raises ValueError
```

**Output:**
```
13
```

---

### `isalnum()`
Returns True if all characters are alphanumeric.

```python
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```

**Output:**
```
True
```

---

### `isalpha()`
Returns True if all characters are alphabetic.

```python
str1 = "Welcome"
print(str1.isalpha())
```

**Output:**
```
True
```

---

### `islower()`
Returns True if all characters are lowercase.

```python
str1 = "hello world"
print(str1.islower())
```

**Output:**
```
True
```

---

### `isprintable()`
Returns True if all characters are printable.

```python
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```

**Output:**
```
True
```

---

### `isspace()`
Returns True only if the string contains whitespace characters.

```python
str1 = "        "
str2 = "\t\t\t\t"
print(str1.isspace())
print(str2.isspace())
```

**Output:**
```
True
True
```

---

### `istitle()`
Returns True if each word starts with an uppercase letter.

```python
str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())
```

**Output:**
```
True
False
```

---

### `isupper()`
Returns True if all characters are uppercase.

```python
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())
```

**Output:**
```
True
```

---

### `startswith()`
Returns True if the string starts with the specified prefix.

```python
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))
```

**Output:**
```
True
```

---

### `swapcase()`
Converts uppercase letters to lowercase and vice versa.

```python
str1 = "Python is a Interpreted Language"
print(str1.swapcase())
```

**Output:**
```
pYTHON IS A iNTERPRETED lANGUAGE
```

---

### `title()`
Capitalizes the first letter of every word in the string.

```python
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```

**Output:**
```
He'S Name Is Dan. Dan Is An Honest Man.
```
