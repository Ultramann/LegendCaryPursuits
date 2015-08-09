Title: Over the River and Through the...Forest
Date: 2015-8-09 10:29
Modified: 2015-8-09 14:09
Category: Blog
Tags: galvanize, data science
Slug: random-forests
Authors: Cary Goltermann
Summary: One decision tree is pretty cool, but what if we had an entire Amazon of them?? No, Jeff Bezos, I was talking about the other Amazon.

Alright kids, today we're going to talk about random forests. This machine learning method follows pretty naturally from decision trees, which wrote about [last time](|filename|./screw_your_parameters.md), so lets dive in. Of all the machine learning methods that I've learned so far, I think I'd choose random forets as the most elegant in terms of intuitive understandability. The basic idea here is that if one decision tree was good, then more are probably better. Now for those (non-existent) astute readers out there, you're probably thinking to yourself:
    
   > _"Self. Decision trees seem rather deterministic, so why would having more than one help me with anything? Talk about redundancy..._

And you'd be right! So how are we going to make it so that having more than one decision tree is helpful to us? First I'm going to introduce the idea of _bagging_. 

### Bagging
Bagging, short for bootstrap aggregating, is a general-purpose tool used to decrease the variance of a statistical learning method. To motivate this idea, consider that given a set of observations, $Z_1, Z_2, ..., Z_n$, each with variance $\sigma^2$, then the mean, $\overline{Z}$, of those observations is $\frac{\sigma^2}{n}$. Thus, by increasing $n$, we can decrease the variance in the mean.

With regards to reducing the variance of a learning method, we can simply increase the number of training sets we create a model from and average all of their predictions. Nice and easy, right? Maybe, if you have access to a ton of training sets; but, in the real world, access to more than one of these is often difficult to get a hold of (at least this is what I've been told, it's not like I've ever actually done any thing in the real world, so disclaimer). So what are we to do?? Simple answer, bootstrap that mother!

[Bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) is basically the process of making new, pseudo, training sets by sampling from the original training set with replacement. The really cool thing is that, assuming your population sample is representative of the population as a whole, by bootstrapping you can infer things about the whole population by assuming that the relationship between the bootstrapped samples and your sample is the same as the relationship between your sample and the whole population. Pretty mind-blowing in my book.

So basically, as applied to learning methods, bootstrapping looks like this, 

>1.  Make a bootstrapped sample from, and the same size as, your training data.
>2.  Fit a decision tree to this bootstrapped sample.
>3.  Repeat a bunch of times.
>4.  All of these trees now represent your model, one with less variance to boot(strap, insert winky face here)!

To predict on a new observation, just see what every tree predicts for it and take the average prediction. Easy peasy.

Ok, now that bagging is covered, let's talk about the meat of this post, random forests, which improve on this process even more, in the specific realm of decision trees.

### Random Forests
The main problem with applying bagging to decision trees is that, even after bootstrapping the all the bagged trees are still going to have a decently high correlation in their predictions. Aka, the trees are still deterministic in nature, and bootstrapping only solves some of this problem.

In order to decorrelate the our bagged trees we introduce a subtle change in the implementation of our steps from above. This change would look like:

>2b.  Every time you go to make a split during the tree making process, only consider a subset, magnitude $m$, from the total number of features, $p$, to split on. 

The size of this subset, $m$, is often chosen to be ~$\sqrt{p}$, but in theory there you could choose a subset of any size. Intuitively, this process makes some sense, add some variation to the way that a decision tree makes it's splits, then at the end average out out all of the variations to see what was really important. The exact mathematical reason for why this process is so effective are currently lost on me, but hopefully I'll find some time eventually to figure out what mathe-magical reason is makes this process so awesome and write about it.

### Out-of-Bag Error
Something that I haven't really talked about in any of my posts yet is the goodness of fit for some of these models. This gets into notions of over and under-fitting and how you can optimize fit. I plan on writing an entire post about this single topic at some point, but this seems to be as good a place as any to gloss over the topic.

The idea of out-of-bag error checking is that every time you make a bootstrapped sample to make a tree from, roughly one-third of the original observations are left out of that sample - remember, bootstrapping happens with replacement, so some observations will appear more than once in a bootstrapped sample and others not at all, I have written a post about the math behind this fact [here](|filename|../code/boosting_proportion.md), if you're interested -, these are referred to as the _out-of-bag (OOB)_ observations. We can leverage this unavoidable fact about bootstrapping to get an idea of how potentially well fit out model is to the real world, by checking how good our model is at predicting the outcome of the OOB observations. This might seems a little sketchy if you know anything about cross-validation, but it goes back to the fact that each observation is left out of samples that roughly one-third of the trees in our forest were made from. 

So we can, without breaking any of math's commandments, get an idea of the error in our model by looking at the error in prediction quality, for each observation, for the subset of our models trees which didn't have that observation in the bootstrapped sample it was created from. Wow, I feel like I didn't explain that very well. But hopefully you get the picture.

That's about all I have for 
