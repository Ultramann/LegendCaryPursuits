Title: Over the River and Through the...Forest
Date: 2015-8-30 23:18
Modified: 2015-8-09 14:09
Category: Blog
Tags: galvanize, data science
Slug: boosting
Authors: Cary Goltermann
Summary: Gradient boosting, Ada-boosting, here-a-boosting, there-a-boosting!

Holy crap it's been quite a while since I've written a post. Take that as a testament to the fact that I've been rather busy. Though arguably I've had the time to write some posts, so I don't really have any excuse. 

Either way, I think that one thing that was deterring me from writing more posts was how long the previous ones have taken me. Considering that I'm going to try and employ some brevity as I start my posting cycle back up, so if this and all subsequent posts seem to be lacking in comparison to the ones I've written previously, you know why that is the case...if you read this sentence.

Now that we've talked about [decision trees](|filename|./screw_your_parameters.md) and one, very good, improvement you can make on them, [random forests](|filename|./random_forest.md); we're going to talk about another general strategy, similar to bagging, that can be used to improve the accuracy of a model. Boosting! Yes it's as cool as it sounds.

### Boosting
Boosting builds off the idea of decision trees via aggregation, but in a way that is decidedly different from that used in the random forest algorithm. I'll first try to explain what the process it goes through is, then I'll present the mathematical algorithm; I know this is unlike me since, in case you haven't noticed yet, I like me my maths, but I found reading the algorithm in math the first time through so hopefully this order of presentation will facilitate a more quickly catalyzed understanding.

Talk about the algorithm...
