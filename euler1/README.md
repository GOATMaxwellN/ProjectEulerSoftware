# Project Euler #1
## Find the sum of the multiples of 3 or 5 below 1000 (natural numbers only)

This can be easily solved using a loop of some sort, but that will get slow once we increase the range.
I was curious as to how I could solve this more efficiently, and after a couple of hours, I discovered the **Finite Sum of Arithmetic Series** formula. 

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/fsoasFormula.svg' height='80'>

This formula calculates the sum of numbers in an arithmetic series. **An arithmetic series is just a series of numbers that increase by a constant amount**. For example, if I wanted to know what the answer would be if I added up all the numbers between 1 and 10, this formula would correctly give me the answer 55. It can only be used if the series goes up by a constant amount. Let's figure out how to use this formula now. 

I'm no mathematician, so I'm not sure what the exact word for the variable ___a___ would be, but I like to think of it as an array, and that it represents the entire series you're working with. The subscripts would be the index you use to access a specific number/term in the series.

Here is an example.
### 2, 4, 6, 8, 10

___a<sub>1</sub>___ would equal 2, as it is the *1st* term in the series. ___a<sub>2</sub>___ = 4 | ___a<sub>3</sub>___ = 6 | ___a<sub>4</sub>___ = 8 | ___a<sub>n</sub>___ = 10. ___n___ is going to be total number of terms in the series. That number will always correlate with the index of the last term in the series. In this case,  ___a<sub>n</sub>___ = ___a<sub>5</sub>___ = 10.

__Here are some uses of the formula.__

![example1](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example1.svg)

![example2](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example2.svg)

![example3](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/example3.svg)

> Note: You might recognize that the first part of the formula (the division) is just finding the median/average of the first and last terms. So this is is basically just getting  the middle of the range, then multiplying it by how many values are in the series.
---

# Code Functionality

We can't use this formula to answer this Project Euler question yet. Even if you knew the last term (___a<sub>n</sub>___) of 3 and 5 under 1000, there is probably no way you know how many terms there are (the value of _n_), which is going to be how many multiples of 3 there are between 3-999, and how many multiples of 5 there are between 5-999.

First thing I did when writing this CLI was just focusing on getting the right answer for one given number. So I started off by just trying to get the correct sum of the multiples of 3 under 1000. Finding the sum of multiples for 2 different numbers is a bit different.

Let's say I've passed in 3 as the number we are going to look for multiples for, and that we only want to look for mulitiples between 1 and 100. Here is what the CLI does to solve this using the **Finite Sum of Arithmetic Series Formula**. There are only 3 steps.

## Step 1. Find the correct first and last term (_a<sub>1</sub>_ and _a<sub>n</sub>_).

Since we are dealing with multiples, we know every number in the series will be a multiple of 3. That already means that I can't use the upper and lower bounds of the range that I passed to the CLI. 1 and 100 will not be in the series, so we have to find the correct first and last term. Luckily, my CLI does not assume that the bounds of the series are exact. Here is how we find the correct ___a<sub>1</sub>___ and ___a<sub>n</sub>___.

Let's start with ___a<sub>n</sub>___, our last term. We want to find the multiple of 3 that is closest to 100. That can easily be done by dividing 100 by 3, stripping off the decimal, then multiplying it back up by 3. Stripping off the decimal (aka flooring) is important part of this equation. If you don't do it, you are just going to get 100 back. Seeing it might make more sense. __(100 // 3) * 3__ (double slashes do floor division in Python).

- 100 / 3 = 33.33333..
- Floor the answer above if needed = 33
- 33 * 3 = 99

> If the upperbound of the range was already a multiple of 3, this equation would do nothing. It's only for if the upperbound is not a multiple of 3.

> This will work for any number and upperbound that is not a multiple of that number.

Let's figure out our ___a<sub>1</sub>___ now. It's pretty much the same equation as the one above, except that unless the lowerbound is already a multiple of 3, the answer will fall below the lowerbound. Here is a demonstration.

- 1 / 3 = 0.33333..
- Floor the answer above if needed = 0
- 0 * 3 = 0

0 is less than 1, which means it is outside of the range. What we need to do is add 1 after flooring the initial division. The equation would now look like this. __(100 // 3 + 1) * 3__.

- 1 / 3 = 0.33333..
- Floor the answer above, then add 1 = 0 + 1
- 1 * 3 = 3

___Remember, you only need to add 1 if the lowerbound is not a multiple of the number you're using___.

## Step 2. Finding how many multiples of your number are in the range. (_n_)

Now we need to know how many numbers are in the range. Your first thought might be to just divide the last term by 3 (or whatever number you're using), but that is actually not going to work for all cases. That will only work if the lowerbound is the lowest possible term, which would be whatever number you want to find the multiples for. In our case, since 3 is the lowerbound, dividing the last term by 3 would work fine, but we're not going to do that. This is what the CLI does.

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/solve_for_n.svg' height='30'>

At first sight, this is an equation that solves for the last term (___a<sub>n</sub>___) in the range. But we already know ___a<sub>n</sub>___, so we can actually use it to solve for ___n___, which is the total amount of terms in the series. ___d___ is the difference, which is just going to be the number we're finding the multiples for. It's basically the constant amount at which the series increases.

Quick examples: 1, 2, 3, 4 d=1 | 12, 15, 18, 21 d=4 | 10, 20, 30, 40 d=10

The equation makes a little bit more sense when you look at a series like this.

Normal series | __d = 3__
-------- | --------
__3, 6, 9, 12, .., 30__ | __0+d, 0+2d, 0+3d, 0+4d, .., 0+nd__

Hopefully that helps you see how the equation above can solve for the last term (___a<sub>n</sub>___). Because it starts at ___a<sub>1</sub>___, you got to subtract 1 from ___n___.
