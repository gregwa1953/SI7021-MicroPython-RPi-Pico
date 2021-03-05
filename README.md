# SI7021-MicroPython-RPi-Pico
Si7021 Temperature and Relative Humidity Sensor

I had ordered a Si7021 from Adafruit, looking for another Temp sensor for my arsonal of goodies to hone my coding skills on the RPi Pico.

While I was waiting on it to arrive, I started looking on the web for a library that would support it and I found one that looked like it would fill the bill at https://github.com/robert-hh/SI7021.  I downloaded the repository and eagerly awaited delivery.

As soon as it arrived, I unpacked it and plugged it in, only to have my "worst" fears justified.  It threw an error...



```
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "/lib/SI7021.py", line 136, in humidity
  File "/lib/SI7021.py", line 83, in _write_command
TypeError: object with buffer protocol required


```

After a bit of digging through other sensor support libraries, I found the answer.  In his _write_command function he has two i2c.writeto calls.  The first one is for double byte commands, which works fine.  However, if the command is only a single byte, his code looks like this...

```
self.i2c.writeto(self.addr, command_byte)
```

Because of the way the Pico handles the byte that gets written, passing it a standard hex value like 0xE5 (the command for 'Read Relative Humidity') returns the above mentioned TypeError.  Replacing the line with:

```
self.i2c.writeto(self.addr, ustruct.pack('<H',command_byte))
```

and adding an import to ustruct, got it to work.

There are still some issues with the library, but for the most part it does work.

If you notice in the test demo code there are the following lines...

```
humidity = si7021.humidity()
temperature = si7021.temperature()
```

I call for the humidity first, then the temperature second, but I don't print them out.  This is because there are two ways to get the temperature on the si7021.  The "normal" way is to get the humidity, which also pulls the temperature, which then you just read the already pulled temperature.  The other is a pull temperature read.  This call is one of the things that doesn't work right at the moment.



Greg