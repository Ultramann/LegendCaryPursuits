Title: If You Thought Boosting Was Sweet in Mario Kart... 
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
Boosting builds off the idea of decision trees via aggregation, but in a way that is decidedly different from that used in the random forest algorithm. I'll first try to explain what the process it goes through is, then I'll present the mathematical algorithm; I know this is unlike me since, in case you haven't noticed yet, I like me my maths, but I found reading the algorithm in math the first time difficult so hopefully this order of presentation will facilitate a more quickly catalyzed understanding.

Boosting starts similarly to random forest. Build a tree. Now, unlike in random forest where you just repeated that first step a ton of times, you build another tree, a single tree, but this tree is built to try and model the residuals that exist from the first tree. Aka, make a tree that is fit to the errors from the first tree. Then you sum the results of those two trees, call it your current model, and make a third tree fit to the residuals from current model. Lather, rinse, repeat.

At first glance this method seemed pretty cool to me; we're taking a weak learner, the decision tree, and building on it with more weak learners, to make a model that predicts much better than any one of those individual trees could by themselves by literally fitting the error out of the model. I'm sure there's a project runway joke in here somewhere... However, I want to make clear that this method is extraordinarily susceptible to overfitting your data. Because... well I'm going to let you think about that one for a second.

Per the usual, we use a form of regularization to combat overfitting. In this paradigm this looks like scaling the how much the tree's that fit the residuals contribute to the model. This scaling factor is called the shrinkage parameter. The other, very important, way that we decrease overfitting is by not added the full tree from each subsequential residual fit. The other way is by not adding up a bunch of trees that are fully fit to the residuals, but instead stumps of those potential trees each time. In this way we can make a model that learns slowly and in turn is more tuned to the signal in the data as opposed to the noise in the data.

#### Math Time
Here's that entire process again, but mostly in math...YAY MATH!

 1)  Start with the null model, $\hat{f}(x) = 0$, such that $r_i = y_i$ $\forall i$ observations in the training data.

 2)  1) Fit a tree stump $\hat{f}^b$ with $d$ splits to the training data and current residuals ($X, r_i$).
     2) Update your model $\hat{f}$ by added on the stump scaled by the shrinkage parameter:
        $$ \hat{f}(x) + \lambda \hat{f}^b(x) \to \hat{f}(x) $$
