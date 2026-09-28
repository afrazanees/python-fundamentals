# Python Fundamentals & Advanced Concepts

A structured, comprehensive repository containing hands-on practice scripts, notes, and exercises covering core Python programming, Object-Oriented Programming (OOP), Data Structures & Algorithms (DSA), FastAPI web development, and technical interview preparation.

---

## Repository Structure

```
python-fundamentals/
├── 01_basics/                         # Variables, type casting, PEP 8 formatting, and linting
├── 02_strings/                        # Slicing, indexing, escape sequences, f-strings, methods
├── 03_numbers/                        # Numeric types, arithmetic operators, math functions
├── 04_conditionals/                   # if/elif/else, chained comparisons, ternary & logical operators
├── 05_loops/                          # for/while loops, range(), for...else, nested loops, iterables
├── 06_functions/                      # Custom functions, parameters, *args, **kwargs, return values
├── 07_file_handling/                  # File I/O operations (reading and writing files)
├── 08_exercises/                      # Practice exercises and fundamentals review quizzes
├── 09_oop/                            # Object-Oriented Programming concepts and patterns
├── 10_data_structures_and_algorithms/ # Classical DSA implementations and problem-solving patterns
├── 11_fastapi/                        # FastAPI REST APIs, routing, validation, and Task CRUD API
├── 12_interview_prep/                 # Common interview questions, tricky outputs, and core drills
└── README.md                          # Repository documentation
```

---

## Modules Breakdown

### 1. `01_basics/`
- **`hello_world.py`** – First Python script and standard output.
- **`variables.py`** – Declaring and assigning variables with dynamic typing.
- **`type_conversion.py`** – Explicit and implicit type conversion (`int()`, `float()`, `str()`, etc.).
- **`code_formatting.py`** – Writing clean, readable code following PEP 8 guidelines.
- **`code_linting.py`** – Catching style errors and code smells with linters.

### 2. `02_strings/`
- **`string_basics.py`** – String creation, indexing, and multi-line strings.
- **`escape_sequences.py`** – Special characters (`\n`, `\t`, `\\`, `\"`).
- **`formatted_strings.py`** – String interpolation using `f-strings`.
- **`string_methods.py`** – Built-in string methods (`.upper()`, `.lower()`, `.strip()`, `.replace()`, etc.).

### 3. `03_numbers/`
- **`numbers_and_arithmetic.py`** – Integers, floats, complex numbers, standard operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
- **`math_functions.py`** – Common built-in math functions (`round()`, `abs()`, `math` module).

### 4. `04_conditionals/`
- **`comparison_operators.py`** – Relational comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`).
- **`chained_comparisons.py`** – Clean syntax like `18 <= age < 65`.
- **`if_elif_else.py`** – Branching execution with conditional blocks.
- **`ternary_operator.py`** – Inline conditional expressions (`x if condition else y`).
- **`logical_operators.py`** – Combining conditions with `and`, `or`, and `not`.
- **`short_circuit_evaluation.py`** – How Python evaluates logical expressions lazily.

### 5. `05_loops/`
- **`for_loops.py`** – Iterating over ranges, sequences, and collections.
- **`for_else_loops.py`** – The unique `for...else` construct in Python.
- **`while_loops.py`** – Condition-based iteration and accumulator loops.
- **`nested_loops.py`** – Multi-dimensional loops and coordinate grids.
- **`iterables.py`** – Working with iterable objects and sequences.
- **`infinite_loops.py`** – Intentional infinite loops and `break`/`continue` control flow.

### 6. `06_functions/`
- **`defining_functions.py`** – Function syntax, parameters, and invocation.
- **`function_arguments.py`** – Positional arguments and parameter passing.
- **`default_parameters.py`** – Optional parameters with default values.
- **`keyword_arguments.py`** – Explicit named arguments for clarity.
- **`function_return_values.py`** – Returning single and multiple values.

### 7. `07_file_handling/`
- **`writing_files.py`** – Creating, opening, writing to, and properly closing files using context managers (`with open(...)`).

### 8. `08_exercises/`
- **`count_even_numbers.py`** – Practical loop and condition exercise.
- **`fundamentals_quiz.py`** – Conceptual check questions on Python basics.

### 9. `09_oop/`
- **`oop_basics.py`** – Classes, instances, class attributes vs instance attributes, `__init__`, and the role of `self`.
- **`inheritance.py`** – Establishing "is-a" relationships and reusing parent class behavior.
- **`super_function.py`** – Calling parent class constructors and methods cleanly with `super()`.
- **`polymorphism.py`** – Method overriding, built-in polymorphism, and operator overloading.
- **`encapsulation.py`** – Public, protected (`_var`), and private (`__var`) attributes, along with Name Mangling.
- **`abstraction.py`** – Defining strict blueprints with Abstract Base Classes (`abc.ABC` and `@abstractmethod`).
- **`inheritance_and_composition.py`** – Comparing "Is-A" (inheritance) vs "Has-A" (composition) design patterns.
- **`exercises.py`** – Predict-the-output exercise testing OOP fundamentals.
- **`interview_questions.md`** – Curated list of high-yield OOP interview questions.

### 10. `10_data_structures_and_algorithms/`
- **`linear_search.py`** – Sequential search algorithm ($O(n)$ time complexity).
- **`binary_search.py`** – Logarithmic search on sorted collections ($O(\log n)$ time complexity).
- **`sorting.py`** – In-place `.sort()` vs out-of-place `sorted()` function.
- **`recursion.py`** – Recursive function structure: base case and recursive case.
- **`stack.py`** – LIFO (Last In, First Out) stack implementation using Python lists (`append` and `pop`).
- **`queue.py`** – FIFO (First In, First Out) queue using `collections.deque` ($O(1)$ operations vs $O(n)$ list shifting).
- **`two_pointer_technique.py`** – Efficient two-pointer pattern for palindrome verification and Two Sum on sorted arrays.

### 11. `11_fastapi/`
- **`main.py`** – Minimal FastAPI server with a root GET endpoint.
- **`get_endpoints.py`** – Path parameters and returning structured JSON data.
- **`post_endpoints.py`** – Accepting JSON request bodies and validating with Pydantic `BaseModel`.
- **`put_endpoints.py`** – Handling updates via PUT requests.
- **`delete_endpoints.py`** – Deleting resources via DELETE requests.
- **`path_parameters.py`** – Dynamic URL routing and type validation.
- **`query_parameters.py`** – Handling optional and required URL query parameters (`?key=value`).
- **`error_handling.py`** – Raising structured HTTP error responses with `HTTPException`.
- **`exercise_1.py`** – Practice endpoint exercise.
- **`things_to_remember.md`** – Reference guide for parameter resolution rules and Swagger UI (`/docs`) vs ReDoc (`/redoc`).
- **`task_api/`** – A complete in-memory Task Management CRUD API demonstrating GET, POST, PUT, DELETE, and route precedence.

### 12_interview_prep/
- **`interview_practice.py`** – 20+ comprehensive interview drills covering:
  - Lists, tuples, dictionaries, and sets
  - Frequency counting algorithms
  - Object identity (`is`) vs equality (`==`)
  - LEGB variable scope (Local, Enclosing, Global, Built-in)
  - Exception handling (`try`, `except`, `else`, `finally`)
  - List comprehensions and filtering
  - Shallow copy vs Deep copy (`copy` module)
  - `*args` and `**kwargs`
  - Two Sum and first non-repeating character algorithms

---

## Getting Started

### Prerequisites
- **Python 3.10+** installed on your system.
- Optional dependencies for the FastAPI module:
  ```bash
  pip install fastapi uvicorn pydantic
  ```

### Running Scripts

Run any individual Python script from the repository root:

```bash
# Core fundamentals
python 01_basics/hello_world.py
python 02_strings/string_methods.py
python 06_functions/defining_functions.py

# OOP
python 09_oop/oop_basics.py
python 09_oop/inheritance.py

# DSA
python 10_data_structures_and_algorithms/binary_search.py
python 10_data_structures_and_algorithms/two_pointer_technique.py

# Interview practice
python 12_interview_prep/interview_practice.py
```

### Running the FastAPI Applications

To start the interactive FastAPI dev server with auto-reload:

```bash
# Minimal FastAPI app:
uvicorn 11_fastapi.main:app --reload

# Full Task CRUD API:
uvicorn 11_fastapi.task_api.main:app --reload
```

Once running, visit:
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
