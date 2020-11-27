# Project Euler #1
## Find the sum of the multiples of 3 or 5 below 1000 (natural numbers only)

This can be easily solved using a loop of some sort, but that will get slow once we increase the range.
I was curious as to how I could solve this more efficiently, and after a couple of hours, I discovered the **Finite Sum of Arithmetic Series** formula. 

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/fsoasFormula.svg' height='80px'>

This formula calculates the sum of numbers in a range. For example, if I wanted to know what the answer would be if I added up all the numbers between 1 and 10, this formula would correctly give me the answer 55. It can only be used if the range goes up by a constant amount. Let's figure out how to use this formula now. 

I'm no mathematician, so I'm not sure what the exact word for the variable __*a*__ would be, but I like to think of it as an array, and that it represents the entire range you're working with. The subscripts would be the index you use to access a specific number/term in the range.

Here is an example.
### 2, 4, 6, 8, 10

___a<sub>1</sub>___ would equal 2, as it is the *1st* term in the range. ___a<sub>2</sub>___ = 4 | ___a<sub>3</sub>___ = 6 | ___a<sub>4</sub>___ = 8 | ___a<sub>n</sub>___ = 10. ___n___ is going to be total number of terms in the range. That number will always correlate with the index of the last term in the range. In this case,  ___a<sub>n</sub>___ = ___a<sub>5</sub>___ = 10.

__Here are some uses of the formula.__

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example1.svg'>
<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example2.svg'>
<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example3.svg'>

> Note: You might recognize that the first part of the formula (the division) is just finding the median/average of the first and last terms. So this is is basically just getting  the middle of the range, then multiplying it by how many values are in the range.
---

# Code Functionality

We can't use this formula to answer this Project Euler question yet. Even if you knew the last term (___a<sub>n</sub>___) of 3 and 5 under 1000, there is probably no way you know how many terms there are (the value of _n_), which is going to be how many multiples of 3 there are between 3-999, and how many multiples of 5 there are between 5-999.

First thing I did when writing this CLI was just focusing on getting the right answer for one given number. So I started off by just trying to get the correct sum of the multiples of 3 under 1000. Finding the sum of multiples for 2 different numbers is a bit different.

Let's say I've passed in 3 as the number we are going to look for multiples for, and that we only want to look for mulitiples between 1 and 100. Here is what the CLI does to solve this using the **Finite Sum of Arithmetic Series Formula**. There are only 3 steps.

## Step 1. Find the correct first and last term.

Since we are dealing with multiples, we know every number in the series will be a multiple of 3. That already means that I can't use the upper and lower bounds of the range that i passed to the CLI. 1 and 100 will not be in the series, so we have to find the correct first and last term. Luckily, my CLI does not assume that the bounds of the range are exact. Here is how we find the correct ___a<sub>1</sub>___ and ___a<sub>n</sub>___.

Let's start with ___a<sub>n</sub>___, our last term. We want to find the multiple of 3 that is closest to 100. That can easily be done by dividing 100 by 3, stripping off the decimal, then multiplying it back up by 3. Stripping off the decimal (aka flooring) is important to make sure you get a 
