# Song that Never Ends

## Questions

8.1. After printing out the lyrics around 1000 times, the program returns the following error message: "RecursionError: maximum
recursion depth exceeded while calling a Python object." This means that there is a maximum number of repeats that python allows, and
our program exceeds that (because it wants to go to infinity)

8.2. See `song.c`.

8.3. After a while, the C program finally returns a "Segmentation fault"

8.4. The C version eventually errs with a segmentation fault because the program tries to access areas of memory that it shouldn't. This
fault can occur, for example, if a program attempts to write to a read only location or overwrite parts of an operating system, but in
this case, the error is because we simply ran out of memory available to our program (the call stack became too big and overflowed).

8.5. See `song.py`.

8.6. This phonebook algorithm is recursive because the function calls upon itself each time it is executed. The function here bascially
involves splitting the phonebook in half again and again until a desired outcome is reached;
so, after we split it in half once and throw away the half we don't need, we repeat these steps of the function by calling upon it again,
and again, AKA recursively. Any time you have a function that is designed to repeat itself until a desired outcome is reached, you
have a recursive function or algorithm.

## Debrief

a. Researching the definition of recursive on the internet was helpful, as was looking at previous source code in C (like cough) to
help remember how to define functions syntactically in C.

b. 45 minutes
