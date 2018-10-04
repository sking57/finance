#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }
    // remember filenames
    char *rawfile = argv[1];

    // declare that this file pointer exists
    FILE *img = NULL;

    // open image file
    FILE *inptr = fopen(rawfile, "r");

    // make sure image is opened
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", rawfile);
        return 2;
    }
    // initialize counter, which will keep track of how many JPEGs we have found
    int counter = 0;

    // assign jpeg as an array of characters (the lenghth used is arbitrary)
    char jpeg[50];

    //create temporary buffer that will be filled with 512 bytes each time through the loop
    unsigned char buffer[512];

    // repeat these steps until the entire card is read through
    while (fread(&buffer, 512, 1, inptr) == 1)
    {
        // check to see if the beginning of each block resembles a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if this is not the first jpeg we've seen, close current file before continuing
            if (counter != 0)
            {
                fclose(img);
            }
            // create new jpeg file
            sprintf(jpeg, "%03i.jpg", counter);

            // open file (img is a FILE * declared earlier)
            img = fopen(jpeg, "w");

            // keeps track of file number
            counter ++;
        }
        // if we are in a jpeg, we have to recover 512 bytes (write them into the jpeg file). Otherwise, just go to next block
        if (counter != 0)
        {
            fwrite(&buffer, 512, 1, img);
        }
    }
    // close infile
    fclose(inptr);

    // close remaining file
    fclose(img);

    // success
    return 0;
}
