# Snow Snow

Ravi thinks there is something suspicious between these lines of this file. Can you help him find out what is suspicious?

Flag Format: **flag{some_l33t_string}**

## Solving

Here we have given a text file thisisit.txt What was in it was  a song. The challenge name is snow snow so I tried Stegsnow which is used for whitespace steganography

When we use Stegsnow we get a string

```
ntio{eP1B35x4K3_aB3O0_q5_K00t}
```

This is a shift cipher. we know that first 4 letters are flag. so we find the shift as 8. Then we can decrypt this string and get the flag using the program

```python
x="ntio{eP1B35x4K3_aB3O0_q5_K00t}"
flag=''
for i in x:
    if(i.isupper()):
        flag+=chr((ord(i)-8-65)%26+65)
    elif(i.islower()):
        flag+=chr((ord(i)-8-97)%26+97)
    else:
        flag+=i
print(flag)
```

We get the flag

## Flag

flag{wH1T35p4C3_sT3G0_i5_C00l}