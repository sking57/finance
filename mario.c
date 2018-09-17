#include <cs50.h>
#include <stdio.h>

int main(void)
{
int height = get_int ("height: ");
while (height<1 || height>8)
    {
        height = get_int ("height: ");
    }
for (int i=1; i<height+1; i++)
    {
        for (int k=height; k>i; k--)
                    {
                        printf(" ");
                    }
        for (int j=0; j<i; j++)
            {
                printf("#");
            }
        printf("\n");        
    }
}
 
   
