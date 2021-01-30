# Crack FDP

I forgot the password for this important file, can you help me in finding the password and important information present in this file?

Flag Format: **flag{some_l33t_string}**

## Solving

Here we are given a pdf and we have to crack its password

so first we make a hash file using `pdf2john` utility in ubuntu. 

it will give us :

```
FDP.pdf:$pdf$4*4*128*-4*1*16*a6cb7310e90cd9989d3d6ddf0bf51123*32*f401440e022445658c5e956dc2ae75a728bf4e5e4e758a4164004e56fffa0108*32*c76c86f02d9bf4234099da4556cbca835e0f8f7e2642e9f4a1c6bb83df7124b9
```

We have to  delete the first part for this to be used by hashcat. We change it to :

```
$pdf$4*4*128*-4*1*16*a6cb7310e90cd9989d3d6ddf0bf51123*32*f401440e022445658c5e956dc2ae75a728bf4e5e4e758a4164004e56fffa0108*32*c76c86f02d9bf4234099da4556cbca835e0f8f7e2642e9f4a1c6bb83df7124b9
```

Then we use hash cat to get the password

```shell
hashcat -m 10500 hash.txt -a 0 rockyou.txt
```

Which will give us the password as - **diosayudameenelesut**

We can open the pdf using this password and if we search for flag we get :

## Flag

**flag{1ae06a29a7abd6c07dba8976698f756b987f734d}**