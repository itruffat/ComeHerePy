#  V1 (WIP)

## V0 and it's shortcommings

----

As personal opinions,there are a handful of things I don't completely love about the language, and would probably 
change on my `v1` proposal.

* [1] The way `"line number"`works is more similar to a `label` than a line number.
  * Lines that do not have an explicit line number do  not count for the `comehere` operand. This in turns reduce the 
   potential syntaxis simplicity by forcing you to add a number for every line you want to use.
  * It's not even similar to how languages with `GOTO` instructions (such as `Basic`). While it's true that the `GOTO`
  statement can ONLY go to explicitly numbered lines, and line-number is probably a misnomer (it's more the `block 
   number` since it can contain multiple lines), there is a reason why this label is a number. In such languages, the 
   code-source is read in order of `line-numbers`. So code examples such as the one below would not work.
  

    NOTE Example 4.2: A better conditional message
    TELL 'Would you like to see a message? (y/n)'
    10  ASK response
    11  TELL 'Hello, world!' NEXT
     9  NOTE Dummy label
        COME FROM 10 + SGN(response - "n")

* [2] List and array support is unnecessary lack-luster.
  * Generally speaking, simplicity is a FEATURE of esolanguages and not an issue. However, that's because they invite us
  to think the problem differently. Lack of array support does not add any meaningful challenge while being very 
  annoying.
  * String-formatting is outright awful. Using a power-based encoding means your upper limit is around 1786 characters 
  in modern implementations of Python. Trying to extract a single character from a string implies multiples operations.
  * It lacks any way of indirectly making any references to a variable or any way to create a list. This means that if 
  you want to handle potentially big inputs (such as parsing a File), there can be no practical way to storage and 
  handle them.
  * While there are some workarounds for this solution, but I can not think of a single one that's not ugly and would 
  probably need a framework to work properly.
* [3] Lacks an instruction to read a single char from the input, the `READ` input reads always reads a full line.
* [4] The `NEXT` keyword is weird and somewhat unnecessary. Would probably remove it if able. 
