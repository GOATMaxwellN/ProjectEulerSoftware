# Find sum of even fibonacci numbers below 4000000 (4 million)
Wasn't able to figure out a way to do this other than iteratively, so I just did that. This CLI is able to list fibonacci numbers up to any term or value you want,
and also filter them by if they're divisible by certain numbers. It can also find the sum of these fibonacci numbers.

When I looked into the overview for this question, there was an efficient way to calculate the even values of the fibonacci sequence, so I added two more functions
that use it. Here's how it works.

2, 8, 34, 144

Those are the first 4 even numbers of the fibonacci sequence, and there is an interesting pattern here. **E(n) = 4 * E(n-1) + E(n-2)**

_E_ is the sequence, _n_ is the index. That equation tells us that if you multiply the previous value by 4 and add it to the value before that, you get the current value.
This is the pattern that the even values in the fibonacci sequence follows, which makes calculating for them a lot more efficient.
