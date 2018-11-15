# Complementary Questions

## Questions

1.1. 10000011

1.2. 11111101

1.3. Before PSY's video, youtube had been representing integers using 32 bits, which can store numbers in the range −2,147,483,648 to
2,147,483,647. However, PSY's video was so popular that the number of views exceeded 2,147,483,647, which is a case of integer overflow.
Since there was not enough storage for a bigger number, the representation looped back around to the beginning of the range, which in
the case of a signed integer, is a negative number. After this video, youtube had to make some changes and start storing views with a
64-bit integer instead.

1.4. The negative number of course occured when the number that was trying to be used got too high and therefore the computer looped the
number around to the beginning of the allowable interval. However, when the computer tried to multiply this giant negative number by 2 again,
it was like adding a giant negative number to a giant negative number, which gives zero by the way negative numbers are represented in
computers (I tested this by just adding -1 to -1 in binary, which looked like 11111111+11111111, which overflows at each place and returns
00000000).
Thereafter, when 0 got multiplied by two, it returned 0, which makes sense.

1.5. The software programmer didn't anticipate more than 16 bits were needed to represent a certain integer having to do with the
acceleration of the rocket, but this failed to account for the fact that this was a much faster rocket. The number was so big that it
actually required 64 bits to represent it, but only 16 bits were allocated, so there was integer overflow. The software program was
unable to accept the number it needed to.

## Debrief

a. In addition to the information given at the beginnning of the questions, the links provided were the most helpful resources, as
well as referring back to lecture notes.

b. 45 minutes
