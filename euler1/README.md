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

At first sight, this is an equation that solves for the last term (___a<sub>n</sub>___) in the range. But we already have a way to get ___a<sub>n</sub>___, so we can actually use it to solve for ___n___, which is the total amount of terms in the series. ___d___ is the difference, which is just going to be the number we're finding the multiples for. It's basically the constant amount at which the series increases.

Quick examples: 1, 2, 3, 4 __d=1__ | 12, 15, 18, 21 __d=4__ | 10, 20, 30, 40 __d=10__

The equation makes a little bit more sense when you look at a series like this.

Normal series | __d = 3__
-------- | --------
__3, 6, 9, 12, .., 30__ | __0+d, 0+2d, 0+3d, 0+4d, .., 0+nd__

Hopefully that helps you see how the equation above can solve for the last term (___a<sub>n</sub>___). Because it starts at ___a<sub>1</sub>___, you got to subtract 1 from ___n___, or else your answer would be ___d___ too high.

Let's plug in our numbers to figure out how many multiples of 3 are between 3 and 99.

![solve_for_n_example](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/solve_for_n_example.svg)

> Remember, if lowerbound of the range is lowest term possible (ie. the number you want the sum of multiples for), then simply dividing ___a<sub>n</sub>___ by that term is enough. It would work for the 3-99 range that we're using. If the range were 12-99, the equation above __must__ be used to get the correct ___n___. 

## Step 3. Solve with Finite Sum of Arithmetic series formula.

Now you know how the CLI gets the correct ___a<sub>1</sub>___, ___a<sub>n</sub>___ and ___n___. All we have to do now is plug all of those in to our Finite Sum of Arithmetic series formula.

<img src='https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/solve_with_fsoas.svg' height='60'>

You can double check that with a loop to find that the answer is correct! This is also a TON faster than a normal loop once it gets to the higher ranges and higher numbers. 

> To my knowledge, this should work for any number and any natural number range. If anybody actually sees this and is able to get an incorrect answer, please let me know.

# Solve for two different numbers.

Alright, the above is awesome. If you only want the sum of multiples of one number, just pass one number to the CLI and it will do the work for you. Once you pass two numbers though, i very slightly different. 

The thing that happens with two numbers is that there is going to a good chance there will be duplicate multiples. For example, the original Project Euler question asks for the sum of multiples of 3 or 5 under 1000, and they have a significant amount of shared multiples in that range, like 15, 30, 45, ....

That means you can't just get the sum of multiples for 3 and 5, and then add them up. In the sub 1000 range, you will be several thousand off. Thankfully, there is a way around it, while still maintaining peak efficiency. That way is the __least common multiple__ (__LCM__). If you didn't know, the LCM of __two__ numbers will contain all their shared multiples in its own multiples. Here is an example with 3 and 5. Their LCM is 15.

|||
|----|----|
|3|3, 6, 9, 12, __15__, 18, 21, 24, 27, __30__, 33, 36, 39, 42, __45__, 48, 51, 54, 57, __60__|
|5|5, 10, __15__, 20, 25, __30__, 35, 40, __45__, 50, 55, __60__|
|15|__15, 30, 45, 60__|

Look at that, their LCM __only__ contains their shared multiples. So now, the equation makes itself obvious. Add up the sum of multiples of 3 and 5 together, then subtract the sum of multiples of 15, all within the same range of course. 

This works for any two numbers, so this might be a better way to say it. Add up the sum of multiples of _a_ and _b_ together, then subtract the sum of multiples of LCM(a, b), all within the same range of course.

The question that comes up now is how to find the LCM of two numbers _efficiently_. Sometimes it is just the product of those two numbers, sometimes it's not. The easiest way is by dividing the product of the two numbers by their greatest common factor/divisor (GCF/GCD). I'm not going to go over how to find the GCF of two numbers. If you want to find out about an efficient way to get the GCF of two numbers, search up the __Eucalidean Algorithm__ _(unless you really want to, you don't have to understand the proof, just know that it works)_. In the case of Python, there are already functions to find the lcm and gcd, but when you're trying to learn cool math stuff like me, where's the fun in tha?

![solve_for_lcm](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/solve_for_lcm.svg)

As you've probably guessed, you plug in 3 and 5 to that equation and you will get 15 as the LCM. So now the final equation is this. (SOM = sum of multiples)

![solve_for_two_som](https://github.com/GOATMaxwellN/ProjectEulerSoftware/blob/main/euler1/formulae_images/solve_for_two_som.svg)

Once you plug in 3 and 5 to that equation, you will get the answer to the Project Euler question, in what might be one of the most efficient ways to do it.

# Conclusion

Learned a lot of cool stuff while making this very small CLI. Maybe one day somebody else will find this useful.
