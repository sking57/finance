# Like Magic

## Questions

4.1. BM

4.2. %PDF

4.3. Because a lot of files have their own signature, or magic numbers, as the first bytes that indicate the file type. However, not
all files have this signature, especially if they aren't a common type, so not every file type can be determined based on the first
several bytes of the file. Also, even if a file begins with the string %PDF or BM, this could just coincidentally be the first strings
of a non-PDF or non-BM file. When trying to detect a file type using magic numbers, context is necessary.

4.4. This code uses a bitwise operator, which compares each bit of two arguments. If both bits are 1, then the operator will output 1;
in all other cases, the operator will output 0. If the file is a jpeg, all 16 possibilities for buffer[3] produce 0xe0 (11100000 in binary)
when compared to 0xf0 (which is 11110000) using the bitwise AND operator.

4.5. Less lines of code means it takes less time for the creator to write the code, which is a valuable thing.
It also takes up less space on the screen (making it easier for others to read and allowing more space for more functionality).
Using bitwise AND also eliminates copy-pasting, which is always a bad thing in programming.

4.6. See `magic.c`.

## Debrief

a. Hexidecimal to decimal converter was useful, as well as the chart provided and the link to the bitwise function wikipedia page.
For #6, it was helpful to look at my recover pset

b. 90
