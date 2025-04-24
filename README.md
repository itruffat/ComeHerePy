# Come Here! (Python Interpreter)

## Introduction 

----

Looking online for different Eso languages I came across 
[ComeHere](https://wwwep.stewartsplace.org.uk/languages/comehere/), which looked like a fun concept to work with. 
Playing on the generally frowned upon `goto` statement (linking code-structure wth its semantic meaning), it tries
to make things one-step wackier by using a dynamic `comefrom` statement. (a reverse `goto` that can also take variables)


    NOTE This is an infinity loop ("CALL <Z> <W>" just means "<W> = <Z>")
    CALL 10 X    
    COMEFROM X 
    10 CALL 20 Y 

In my opinion the fun part is that, beyond its transgressive defiance of a good practice, it also lacks any kind of 
explicit branching logic, so workflow myst be done by using this feature. To me this greatly elevates the language in
the eso-lang tier.

In turn, I decided to make a quick Python interpreter. **As a warning, it's more of a proof of concept and code is far
from perfect.** It can be found inside the `v0` folder, and run using the `runner.py` program.

     python runner.py <file_path>

