# Omega Directive

## Questions

6.1. Selection sort is Ω(n2) and not Ω(n) because if in the best case scenario (the numbers are in order), selection sort still
has to search through the unsorted part of the array for a smaller number and it does this for each value in the unsorted data, so this would
be n comparisons made n times, leading to n^2 steps. It doesn't matter how sorted the array is -- this process will be the same.
However, in bubble sort, we would go through the array one time, making a comparison for each pair of values. Since there would be
no swapping done, the sort would be finished after the first time through, after only taking n steps

6.2. In both upper bound and lower bound on the running time for a merge sort, the array will be split n times, therefore there will
be log(n) steps taken. Then, the algorithm will have to make n comparisons for each time the array is split in 2, so log(n) will be
done n steps, and therefore a merge sort is in ϴ(n log n). The process is independent of how well sorted an array already is: we have
n elements and we have to combine them log(n) times.

6.3. strlen in C is a function that returns the length of any string up to, but not including the null character \0 at the end of all
strings. It takes n steps because, no matter what character is passed, it just adds 1 to a counter for each character.

6.4. Perhaps the len function in python just returns the index value of the last element in the array/list.

6.5. For each character that is passed, the isupper function in C probably just retrieves the ASCII code of the character and if this
value is in between 65 and 90, it returns true, and otherwise, it returns false.

## Debrief

a. Review video/lecture video on sorting was helpful

b. 40 minutes
