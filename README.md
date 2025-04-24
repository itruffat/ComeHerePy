# Come Here! (Python Interpreter)

## Warning: this is an early release. May need further testing.

## Introduction 

----

Looking online for different Eso languages I came across 
[ComeHere](https://wwwep.stewartsplace.org.uk/languages/comehere/), which looked like a fun concept to work with. 
Playing on the generally frowned upon `goto` statement (linking code-structure wth its semantic meaning), it tries
to make things one-step wackier by using a dynamic `comefrom` statement. (a reverse `goto` that can also take variables)


    NOTE This is an infinity loop
    NOTE "CALL <Z> <W>" just means "<W> = <Z>"
    CALL 10 X    
    COMEFROM X 
    10 CALL 20 Y 

In my opinion the fun part is that, beyond its transgressive defiance of a good practice, it also lacks any kind of 
explicit branching logic, so workflow myst be done by using this feature. To me this greatly elevates the language in
the eso-lang tier.

In turn, I decided to make a quick Python interpreter. As a warning, it's more of a proof of concept and code is far
from perfect. It can be found inside the `v0` folder.


##  Theoretical V1

----

As personal opinions,there are a handful of things I don't completely love about the language, and would probably change
if I ever design a `v1` of my own.

* Non-named lines do not count for the `comehere`. This turns line-numbers into boring `labels` and reduce potential 
  syntaxis simplicity by making the line number implicitly increase.
* List and array support is unnecessary lack-luster.
  * String-formatting is outright awful. Using a power-based encoding means your upper limit is around 1786 characters 
  in modern implementations of Python. Trying to extract a single character from a string implies multiples operations.
  * It lacks any way of indirectly making any references to a variable or any way to create a list. This means that if 
  you want to handle potentially big inputs (such as parsing a File), there can be no practical way to storage and 
  handle them.
  * While there are some workarounds for this solution, but I can not think of a single one that's not ugly and would 
  probably need a framework to work properly.
* Lacks an instruction to read a single char from the input, the `READ` input reads always reads a full line.
* The `NEXT` keyword is weird and somewhat unnecessary. Would probably remove it if able. 
