# Project Euler #1
## Find the sum of the multiples of 3 or 5 below 1000 (natural numbers only)

This can be easily solved using a loop of some sort, but that will get slow once we increase the range.
I was curious as to how I could solve this more efficiently, and after a couple of hours, I discovered the **Finite Sum of Arithmetic Series** formula. 

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/fsoasFormula.svg' height='80px'>

This formula calculates the sum of numbers in a range. For example, if I wanted to know what the answer would be if I added up all the numbers between 1 and 10, this formula would correctly give me the answer 55. Let's figure out how to use this formula now. 

I'm no mathematician, so I'm not sure what the exact word for the variable __*a*__ would be, but I like to think of it as an array, and that it represents the entire range you're working with. The subscripts would be the index you use to access a specific number/term in the range.

Here is an example.
### 2, 4, 6, 8, 10

___a<sub>1</sub>___ would equal 2, as it is the *1st* term in the range. ___a<sub>2</sub>___ = 4 | ___a<sub>3</sub>___ = 6 | ___a<sub>4</sub>___ = 8 | ___a<sub>n</sub>___ = 10. ___n___ is going to be total number of terms in the range. That number will always correlate with the index of the last term in the range. In this case,  ___a<sub>n</sub>___ = ___a<sub>5</sub>___ = 10.

Here are some uses of the formula.

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example1.svg'>

<hr>

Armed with that information, you could use this formula to now calculate for yourself what 
