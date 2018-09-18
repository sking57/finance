#include <cs50.h>
#include <stdio.h>

int main(void)
{
//prompt user for height 
int height = get_int ("height: ");
//We want the height to be between 1 and 8. When the inputted height is below 1 or above 8, re-prompt user again and again until correct integer is inputted
while (height<1 || height>8)
{
    height = get_int ("height: ");
}
//we want the number of rows to equal the height that the user inputs, so the outer for loop requires that the commands for each row should repeat themselves 4 times, going to the next line each loop.
for (int i=1; i<height+1; i++)
    {
//right-align the pyramid by pushing the hashes to the right with spaces. Each row should have (height-i) spaces. 
        for (int k=height; k>i; k--)
             {
                printf(" ");
             }
//For each iteration of the outer for loop, i, print that many hashes
        for (int j=0; j<i; j++)
            {
                printf("#");
            }
        printf("\n");        
    }
}
 
   
