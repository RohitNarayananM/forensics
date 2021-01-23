# Detailed View

Sam, thinks there is more to know about this file. Can you help him know more about this file?

Flag format: **flag{some_l33t_string}**

## Solving

Here we get an image file.png

When we use strings on the image we get a link

https://pastebin.com/KudUCfTC

If we go to the link we get a string

**ZmxhZ3tNMTVzSTBOX2FDYzBNUEwxNWgzRH0=**

because of the "=" in the end we suspect it is a base64 string and we decode it and we get the flag

## Flag

**flag{M15sI0N_aCc0MPL15h3D}**