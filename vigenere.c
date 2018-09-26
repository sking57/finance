#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//This program will get a keyword and a message from the user and assign shift values to the letters in this word. Each integer value of the keyword will shift the letters in the message by a key inputted by the user, and will display the encrypted ciphertext.

//Call shift function operation
int shift(char c);

int main(int argc, string argv[])
{
//Declare all variables
    string s = argv[1];
    int n = strlen(s);
    int key;
    int nonaslphas = 0;
    int alphabet = 26;
// check to make sure the program was run with a single command-line. If not, print error message and stop running.
    if (argc != 2)
    {
        printf("Usage: ./vigenere keyword\n");
        return 1;
    }
// Check to make sure all characters of the input are alphabetic characters. If they are not, print error message and stop running.
    for (int i = 0; i < n; i++)
    {
        if (!isalpha(s[i]))
        {
            printf("Usage: ./vigenere keyword\n");
            return 1;
        }
    }
//Encrypt plaintext message by adding each key to each corresponding character in the string. To make sure the ciphertext loops around the alphabet and preserves case, we will also subtract A, get the remainder when divided by 26 (alphabet), and then add A back again to get to the right section in ASCII numbers. Upper case and lower case characters are separated since they are in different sections of ASCII numbers. For each key, mod the shift value by its own string length to make sure the key keeps looping through the length of the argument given. Subtract the iteration by integer nonalphas to account for any time the plain text has a non-alphabetical character (like a spacebar).
    string text = get_string("plaintext: ");
    for (int j = 0, m = strlen(text); j < m; j++)
    {
        key = shift(s[(j - nonaslphas) % n]);
        if (isupper(text[j]))
        {
            text[j] = (text[j] - 'A' + key) % alphabet + 'A';
        }
        if (islower(text[j]))
        {
            text[j] = (text[j] - 'a' + key) % alphabet + 'a';
        }
        if (!isalpha(text[j]))
        {
            nonaslphas++;
        }
    }
//of course, once we have performed the transformation on the plaintext, the chiphertext should be printed for the user to see
    printf("ciphertext: %s\n", text);
}

//This function will convert the characters to their corresponding shift value (key) by subracting 'a' (97) from lowercase letters and 'A' (65) from uppercase letters
int shift(char c)
{
    int cnum;
    if (isupper(c))
    {
        cnum = c - 'A';
    }
    if (islower(c))
    {
        cnum = c - 'a';
    }
    return cnum;
}
