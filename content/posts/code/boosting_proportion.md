Title: Proportional Representation of a Boosted Sample
Date: 2015-8-02 08:18
Modified: 2015-8-03 09:29
Category: Code
Tags: data science, boosting
Slug: boosting-proportions
Authors: Cary Goltermann
Summary: A demonstration of why ~ $\frac{2}{3}$ of a samples elements are present in a bootstrapped sample of the same size.

So, we were told that if you have a sample, $S$, of size $n$, when you create a bootstrapped sample, $B_S$, also of size $n$, that roughly, on average, $\frac{2}{3} rds$ of the elements from $S$ are present in any $B_S$.

The importance of this, at least in my super small world right now, is that the items that are left out of bootstrapped samples can be used to cross-validate models built from the bootstrapped samples. This is especially cool with models akin to random forests, which make a bunch of trees from bootstrapped samples. Because we are bootstrapping the samples we can use the elements left out of the creation of each tree to cross-validate that specific model. The magnitude of these "out-of-bag" elements, for a sample of size $n$, ends up being roughly $\frac{n}{e} \approx \frac{n}{3}$.

The proof for this is actually pretty simple, so I'll do it here and then show some python code that gives more intuition for this fact.

First of all, the fraction of elements from $S$ that are represented in any $B_S$ approaches $1 - \frac{1}{e} \approx 0.632$.

The proof for this goes as follows. The probability that any single element isn't chosen from $S$ is $1-\frac{1}{n}$. So the probability that a single element isn't chosen for all of the choices that are made to construct any $B_S$ is $(1-\frac{1}{n})^n$. If you think about it a little bit longer you'll realize that is probability is also equal to the proportion of elements in that bootstrapped sample $B_S$. Once you realize that one of the accepted definitions of the exponential is, $$e^x = \lim_{n\to\infty} \Big(1 + \frac{x}{n}\Big)^n$$
Now, just plug in $x = -1$ and you get our proportion. Thus, said proportion approaches $1 - \frac{1}{e}$ as $n\to\infty$, $\Box$. 

I know that was a little handwavy, but I'm sure it gets me to the correct conclusion. With that in mind, here is a simple python script I wrote to demonstrate what size $n$ is necessary to get close to that "$\frac{2}{3} rds$".

    :::python
    import matplotlib.pyplot as plt
    import math

    x = range(1, 101)
    E_k = [1-(1 - 1./n)**n for n in x]

    plt.plot(x, E_k, 'bo-')
    plt.plot([0]+x, [1-1/math.exp(1) for _ in [0]+x], 'r-', label='1-1/e')
    plt.ylim(.5, 1.01)
    plt.xlabel('Sample size')
    plt.ylabel('Probability that any single item is\nin bootstrapped sample')
    plt.title('Proportion of items represented in a\nbootstrapped sample')
    plt.legend(loc='best', prop={'size':14})
    plt.show()

Resulting in the graph:
<div style="text-align: center"><img src="/images/bootstrap_pro.png" style="height: 350px"></div>
Looks like by the time you get to $n=20$ you're going to get pretty damn close to that $1 - \frac{1}{e}$. Pretty cool.
