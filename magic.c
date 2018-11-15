// program detects file type for BMP, JPEG, or PDF

// Header files
#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./magic file\n");
        return 1;
    }
    // open file
    FILE *inptr = fopen(argv[1], "r");
    // ensure file is opened
    if (inptr == NULL)
    {
        fprintf(stderr, "Error: Cannot open %s.\n", argv[1]);
        return 1;
    }
    // Set aside a buffer to hold first four bytes of file
    unsigned char buffer[32];
    // read first four bytes from file into buffer
    fread(&buffer, 1, 32, inptr);
    // check if file is jpeg
    if (buffer[0] == 0xff &&
        buffer[1] == 0xd8 &&
        buffer[2] == 0xff &&
        (buffer[3] & 0xf0) == 0xe0)
    {
        printf("JPEG\n");
    }
    // check if file is a PDF
    else if (buffer[0] == 0x25 &&
             buffer[1] == 0x50 &&
             buffer[2] == 0x44 &&
             buffer[3] == 0x46)
    {
        printf("PDF\n");
    }
    // check if file is a BMP
    else if (buffer[0] == 0x42 &&
             buffer[1] == 0x4d)
    {
        printf("BMP\n");
    }
    else
    {
        printf("\n");
    }
    // close infile
    fclose(inptr);
    return 0;

}