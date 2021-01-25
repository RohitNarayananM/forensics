

# You can't see me

We have received an image but seems like somebody has messed up with the data. Can you help us?

## Solving

Here we are given an image which is not openable. As it is not openable we try `pngcheck` and it gives:

```
image.png:  CORRUPTED by text conversion
ERROR: image.png
```

Then we looked at its hex dump and there the magic numbers weren't correct. So we corrected it

Still it wasn't opening

We again checked it using :

```shell
 pngcheck -vf image.png
```

It gave :

```shell
File: image.png (43860 bytes)
  chunk IDHR at offset 0x0000c, length 13:  first chunk must be IHDR
:  illegal (unless recently approved) unknown, public chunk
  chunk gama at offset 0x00025, length 4:  first chunk must be IHDR
:  illegal reserved-bit-set chunk
  chunk cHRM at offset 0x00035, length 32:  first chunk must be IHDR
  chunk bKGD at offset 0x00061, length 6:  first chunk must be IHDR
  chunk tIME at offset 0x00073, length 7:  first chunk must be IHDR
  chunk idat at offset 0x00086, length 32768:  first chunk must be IHDR
:  illegal reserved-bit-set chunk
:  invalid chunk length (too large)
ERRORS DETECTED in image.png
```

When we fix these errors we could open the file and it had the flag

![image-20210124223439770](youcan'tseeme.png)



## Flag

**inctfj{WH4t_ar3_pNgCHUnkS?}**