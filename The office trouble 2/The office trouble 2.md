# The office trouble 2

Jim took his revenge by encrypting Dwight's client information which was in a PDF file You know what to do.. Right ?

## Solving

Here we are given a pdf and we have to crack its password

so first we make a hash file using `pdf2john` utility in ubuntu. 

it will give us :

```
The_office_trouble_2.pdf:$pdf$2*3*128*-3904*1*16*3bf30b707183a4d84e64967243b6d7b1*32*1ffd47ef46b45a422d0c1864e01a963500000000000000000000000000000000*32*76202f5357cb19b937fa5e0c14ba8f7ff7aef55ab96a938f817f36dc1005ff72
```

We have to  delete the first part for this to be used by hashcat. We change it to :

```
$pdf$2*3*128*-3904*1*16*3bf30b707183a4d84e64967243b6d7b1*32*1ffd47ef46b45a422d0c1864e01a963500000000000000000000000000000000*32*76202f5357cb19b937fa5e0c14ba8f7ff7aef55ab96a938f817f36dc1005ff72
```

Then we use hash cat to get the password

```shell
hashcat -m 10500 hash -a 0 rockyou.txt
```

Which will give us the password as - **fear420**

When we open the pdf there is an image with the flag :

![image-20210130230748942](The office trouble 2.png)



## Flag

**inctfj{ass1stant_t0_th3_regi0nal_man4ger}**

