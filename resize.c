// Rezises a BMP file

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }
    //ensure the first argument is made of digits
    for (int m = 0, s = strlen(argv[1]); m < s; m++)
    {
        if (!isdigit(argv[1][m]))
        {
            printf("Usage: ./resize n infile outfile\n");
            return 1;
        }
    }

    // convert first argument to an integer
    int n = atoi(argv[1]);

    //ensure the integer is positive and less than 100
    if (n <= 0 || n > 100)
    {
        printf("Usage: ./resize n infile outfile\n");
        return 2;
    }

    // remember filenames
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 1;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 1;
    }

    // determine old padding
    int oldpadding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;

    // alter bi and bf header sizes & determine new padding
    int newwidth = bi.biWidth * n;
    int newpadding = (4 - (newwidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int newheight = bi.biHeight * n;
    bi.biHeight = newheight;
    bi.biWidth = newwidth;
    bi.biSizeImage = ((newwidth) * sizeof(RGBTRIPLE) + newpadding) * abs(newheight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, (sizeof(BITMAPFILEHEADER)), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, (sizeof(BITMAPINFOHEADER)), 1, outptr);

    // iterate over infile's old scanlines (divide by scale)
    for (int i = 0, biHeight = abs(bi.biHeight) / n; i < biHeight; i++)
    {
        // reset counter
        int counter = 0;

        // create temporary buffer to fill with new width values
        RGBTRIPLE outrow[newwidth];

        // iterate over pixels in old scanline (divide by scale)
        for (int j = 0; j < bi.biWidth / n; j++)
        {
            // hold place of counter for the whole row, needs to keep counting for the whole row (up to the new width)
            counter = j * n;

            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // fill up buffer with each pixel from the infile n times.
            for (int l = 0; l < n; l++)
            {
                outrow[counter] = triple;
                counter++;
            }
        }
        for (int l = 0; l < n; l++)
        {
            // write array of new outrow to outfile n times. Make sure size is scaled.
            fwrite(&outrow, sizeof(RGBTRIPLE)*newwidth, 1, outptr);

            // then add back new padding to each of the n row (to demonstrate how).
            for (int k = 0; k < newpadding; k++)
            {
                fputc(0x00, outptr);
            }
        }
        // skip over old padding, if any
        fseek(inptr, oldpadding, SEEK_CUR);
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}