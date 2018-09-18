#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
//prompt user for how much change is owed
    float change = get_float("Change owed: ");
//makes sure that the user is re-prompted contunually if they input a negative value 
    while (change<0)
    {
        change = get_float("Change owed: ");
    }
//convert the user's inputted dollars to cents for precision
    int cents = round(change * 100);
//set number of coins equal to zero to start
    int coins = 0;   
//When quarters can be used (there is more than 25 cents of change left), decrease amount by quarter and then increase the number of coins used by 1
    while (cents >= 25)
    {
        cents = cents-25;
        coins++;
    } 
//When dimes can be used (there is more than 10 cents of change left), decrease amount by dime and then increase the number of coins used by 1
    while (cents >= 10)
    {
         cents = cents-10;
         coins++;
    }      
//When nickels can be used (there is more than 5 cents of change left), decrease amount by nickel and then increase the number of coins used by 1
    while (cents >= 5)
    {
       cents = cents-5;
       coins++;
    }   
//When pennies can be used (there is more than 1 cent of change left), decrease amount by penny and then increase the number of coins used by 1
     while (cents >= 1)
     {
          cents = cents-1;
          coins++;
     }   
//print the final value of coins used and then go to next line
    printf("%i\n",coins);
}
