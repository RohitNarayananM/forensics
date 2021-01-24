 # My-first-steganography

We intercepted the transmission between Russian spies, we got intel that they used something default to transmit message through images. Could you find it for us?

## Solving

Here we get two files blueprint.jpg and blueprinto.jpg. Doing `file` and `strings` gives nothing important. we tried `binwalk` and it too didn't have anything. The title says first steganography so I tried steghide

```shell
steghide extract -sf blueprint.jpg
```

gave us a password.txt which contains

**d4rk_s1d3**

After that we try same with blueprinto.jpg and give this as passphrase which will give us a plans.txt

```shell
steghide extract -sf blueprinto.jpg
```

and it contains the flag

## Flag

**inctfj{w3_4r3_pl4nt1ng_4_b0mb}**