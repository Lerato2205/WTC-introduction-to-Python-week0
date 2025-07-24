📚 What I’ve Learned So Far
🔧 Git & GitHub
I’ve learned how to create a repository on GitHub and connect it to Visual Studio Code.

I can pull changes using git pull and push my work with git push.

I know how to access and edit repositories through VSCode.

I’m still practicing how to clone repositories using git clone.

🐍 Python Basics
I’ve started learning Python and created a simple file called hello.py.

I can run a Python file using:

nginx
Copy
Edit
python hello.py
This command runs the file and shows the output in the terminal.

✅ Helpful Terminal Commands:
clear – clears the terminal screen.

cp hello.py newfile.py – copies a file.

ls – lists files in the current folder.

rm filename.py – deletes a file.

🔁 Python Functions & Variables
I’ve learned how to define and call functions in Python. For example:

python
Copy
Edit
def main():
    print("Hello, world")
    print("This is CS50P.")

main()
I understand that variables can store:

Numbers

Strings (text)

Other data types

I’m still practicing how to return variables from functions and becoming more comfortable with how they work.

💥 Side Effects
I’ve learned that functions can have side effects, like changing data outside their own scope.

I now understand how to use the global keyword to modify variables defined outside a function.

I can pass arguments into functions to make them more dynamic and reusable.

🧹 String Methods
I’ve learned how to clean and format strings using methods like:

strip() – removes whitespace from the beginning and end of a string.

title() – capitalizes the first letter of each word.

I can also combine strings using join() to form complete messages or sentences.



######################################################################################
# CS50 Problem Set 0 – Python

This Part contains my solutions for CS50's Problem Set 0, implemented in Python. Each program is designed to practice core concepts such as user input, string manipulation, arithmetic operations, and formatted output.

---

## 🟩 1. indoor.py

**Goal:** Convert user input to lowercase.

**Description:**  
Prompts the user to type anything and then prints the same message in all lowercase. This reinforces understanding of string methods like `.lower()`.

**Example:**
- Input: `HELLO`
- Output: `hello`

---

## 🟩 2. playback.py

**Goal:** Simulate playback by replacing spaces with ellipses.

**Description:**  
Takes a user’s phrase and replaces every space with `...` to mimic slow or dramatic speech. Introduces string manipulation using `.replace()`.

**Example:**
- Input: `Lerato Chitaya`
- Output: `Lerato...Chitaya`

---

## 🟩 3. faces.py

**Goal:** Replace emoticons with emojis.

**Description:**  
Converts text-based emoticons like `:)` and `:(` into corresponding emoji faces using string replacement.

**Example:**
- Input: `Hello :)`
- Output: `Hello 🙂`

---

## 🟩 4. einstein.py

**Goal:** Calculate energy using Einstein’s mass-energy formula.

**Description:**  
Applies the formula `E = mc²` where `c = 300000000 m/s`. Prompts the user for mass in kilograms and outputs the equivalent energy in joules as an integer.

**Example:**
- Input: `1`
- Output: `90000000000000000`

---

## 🟩 5. tip.py

**Goal:** Calculate a tip based on a meal cost.

**Description:**  
Asks the user how much the meal cost (in Rands, e.g., `R200`) and calculates a 10% tip. Demonstrates use of string replacement, type conversion, arithmetic, and formatted printing.

**Example:**
- Input: `R200`
- Output: `Leave R20.00`

---

## ✅ Summary

This problem set introduced me to:
- Basic Python syntax and functions
- User input handling
- String methods like `.lower()` and `.replace()`
- Type conversion (`int`, `float`)
- Arithmetic and scientific notation
- Formatted output using f-strings

These exercises built a strong foundation for writing clean, functional Python programs and prepared me for more advanced topics ahead.
