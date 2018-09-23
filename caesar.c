#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//This program will encrypt messages inputted by the user, shifting the letters in the message by a key inputted by the user, and will display the ciphertext.  

int main(int argc, string argv[])
{
    string s = argv[1];
// check to make sure the program was run with a single command-line. If not, print error message and stop running
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
// Check to make sure all characters of the input are digits. If they are not, print error message and stop running 
    for (int i=0, n = strlen(s); i < n; i++)
    {
        if (!isdigit(s[i])) 
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
//once we know the user has inputted an integer, convert the string to and integer and add the key to each character. To make sure it loops around, we will also subtract A, get the remainder when divided by 26 (this way, the key can be really high and it will stil loop through the 26 options), and then add A back again to get to the right section in ASCII numbers. However, separate upper case and lower case characters since they are in different sections of ASCII numbers. If a character in the plain text is not a letter, nothing will happen to it (it will skip the if commands and just stay the same).  
    int key = atoi(s);
    string text = get_string("plaintext: ");
    for (int j=0, m = strlen(text); j < m; j++)
    {
        if (isupper(text[j]))
        {
            text[j] = (text[j] - 'A' + key) % 26 + 'A';    
        }
        if (islower(text[j]))
        {
            text[j] = (text[j] - 'a' + key) % 26 + 'a';
        }
    }
//of course, once we have performed the transformation on the plaintext, the chiphertext should be printed for the user to see
    printf("ciphertext: %s\n", text);
}
