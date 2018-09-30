# Questions

## What's `stdint.h`?

'stdint.h' is a a header file in the C library that specify exact-width integer types. Each type has a defined minimum and maximum value. This helps make code more portable. 

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

This is a more specific way of writing integers. For example, 'uint8_t' specifies that the integer is 8 bits wide. 

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

a BYTE is 1 byte, a 'DWORD' and 'LONG' are each 4 bytes, and a 'WORD' is 2 bytes 

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

the first two bytes, in any of these numbering systems, is a word that denotes the file type of the file, AKA 'bftype'. It must be set to BM.

## What's the difference between `bfSize` and `biSize`?

'bfSize' is the size of a bitfile map, in bytes, while 'biSize' is  the nunber of bytes required by the whole structure.

## What does it mean if `biHeight` is negative?

If biHeight is negative, the bitmap is a top-down DIB and its origin is the upper-left corner. In this case, biCompression must be either BI_RGB or BI_BITFIELDS. Top-down DIBs cannot be compressed.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount specifies the number of bits for each pixel and the maximum number of colors in the bitmap

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

This will happen if it can't create an inflie nor and outfile like it is supposed to. 

## Why is the third argument to `fread` always `1` in our code? (For example, see lines 40, 44, and 75.)

It only reads 1 RGB value at a time

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

If the size of the RBG value is 9 bytes (3 pixels X 3 bytes per pixel), then padding will equal 1

## What does `fseek` do?

It seems to just skip over the padding and then look for the next pixel? idk

## What is `SEEK_CUR`?

this moves a file poniter position to a given location. 
