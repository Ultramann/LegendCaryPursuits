Title: Regressing to Regressions
Date: 2015-8-02 08:18
Modified: 2015-8-02 08:36
Category: Blog
Tags: galvanize, data science
Slug: regressing-to-regressions
Authors: Cary Goltermann
Summary: Regressions and some of the lovely things that go along with them. 

I just realize that it has been very nearly two weeks since I last posted anything. This fact alone is, at least, partially indicative of how little time I have left after working on the on the course material every day. But this is a good thing; because, while these past two weeks have been very hard and fast hitting, there has been an insane amount of growth in my data science knowledge during this very short time period. I think that the best thing for me to do is give a quick summary of the models that I learned about in the last fortnight. This specific post will cover linear and logistic regressions. Eventually I will write about more complex models and will hopefully link them here and possibly here.

Disclaimer: though I learned quite a lot about the following models (though they are simple regressions), I think that one of the most powerful things that I learned was how deep my ignorance with regards to them goes. Just to make an unnecessarily colorful analogy:
>I feel like a gangster who previously only had a small pistol but recently got my hands on an arsenal of weapons. Do I feel more powerful? DAMN STRAIGHT I DO! But realistically I don't have the experience to know what situations call for what weapon yet. And because of that I'm more than likely to bring a couple of AKs to some knife fights, and surely plenty of knives to some RPG ones as well.  
<div style="text-align: center"><h4>"Knife" Fight</h4><img src="/images/knife_fight.png" style="height: 350px"></div>

With all that in mind. Here's my, poor, to be sure, description of the regression models that we learned two weeks ago.
### Linear Regression
Linear regression is, without a doubt, the great-great-great-grandfather of all prediction models. However, with it's age it shows it's simplicity. Basically linear regression is trying to answer the question, if we have data with $\textit{p}$ features, then how can we choose weights $\beta_{p}$ such that the quantity $RSS = \sum\limits_{i\in N} (y_i - \hat{y}_i)^2$, where $\textit{N}$ is the set of observations, is minimized, where $$\hat{y} = \beta_{0} + \beta_{1}x_{1} + \beta_{2}x_{2} + \cdots + \beta_{p}x_{p}.$$
Intuitively this means find a line (in p-space) such that the average square distance of each observation, $y_i$ from its predicted value $\hat{y}_i$ is minimized.

So that's pretty cool, until you realize that the assumptions of the model include additive separability, linearity (duh), and [homoscedasticity](https://en.wikipedia.org/wiki/Homoscedasticity) (whatever that means) and that very few situations in the world match up with any, much less all, of these assumptions. With that in mind, there are situations where, if you consider a ton of interaction terms (read: features multiplied by other features), that your linear model could overfit your data. One way to combat overfitting, a pervasive problem in model, of your training data is by introducing some sort of regularization term (this concept has some sort of analog in basically all of the models that I know of (read: all 5), so try and be concerned with the basic idea of regularization rather than the implementation for linear regression) to temper the effects of the fitting process.

In the linear regression sphere we have two fairly simple regularization options, Ridge and the Lasso (they're about as cool as they sound). Basically the idea is that, for each coefficient $\beta$ you impose a penality $\|\beta\|_2$ or $\|\beta\|$, for ridge and lasso respectively, scaled by some factor $\lambda$, called the tuning parameter, on the RSS. So the value you try to minimize is $$\sum\limits_{i\in N} \Big(y_i - \beta_0 - \sum\limits_{j=1}^p \beta_{j}x_{ij}\Big)^2 = RSS + \lambda \sum\limits_{j=1}^p \beta_j^2.$$
I was told to think of these regularization methods as penalizing the coefficients, by some factor $\lambda$, for being too big. 

Alright, that section took me way too long to write, so now I'm going to move on.
### Logistic Regression
Logistic regressions try to solve the problem of binary classification, whereby you are trying to determine which of two classes a particular data point belongs to. The linear regression falls short in this application because the only two values that any data point can take on are 0 and 1 (this is true of any model in the classification paradigm). Basically what we try to do is use the function: $$p(X) = \frac{e^{\beta X}}{1+e^{\beta X}},$$ where $\textit{X}$ is the matrix of our data and $\beta$ is the vector of our coefficients for each feature. This is called the logistic, or sigmoid, function, what is important about it is that it is bound by the interval (0, 1). The following graphs show the comparison of applying a linear and a logistic regression to binary classified data.
<div style="text-align: center"><h4>Linear vs Logistic Regression</h4><img src="/images/linear_v_log.tiff" style="height: 250px"></div>
You can see that the only two values a data point, displayed as a yellow dot, can take on are 0 and 1, and that the linear model is well out of its league when it comes to predicting data of this nature's value.

The basic idea of a logistic regression is almost identical to that of the linear regression. Minimize the sum of square distances between the predicted and actual.

### Thoughts About Regression
To maintain the analogy of models as weapons, I want to make it clear that, in and of themselves, these regressions are the sharpened spoons in the modeling arsenal. From what I understand, they can serve a very useful purpose when combined with other more powerful models, but by themselves, it's very unlikely that you are going to achieve a high level of predictive capability from these guys (I'll try to come back and update this post when/if I find a place to use these models in the future).

### Notes
Quickly, personal stuff. One of the reasons that contributed to my lack of time to post in the last couple of weeks was that one of my best friends got married last weekend, Eugene Wan, whose blog can be found [here](http://eugenewan.com). In addition, I had the honor of officiating his wedding. So I can now put, and don't doubt that I will, professional wedding officiant on my résumé.

In other news, I have barely worked out in the last two weeks. I'm going to try and get back on that horse. We'll see how it goes. I'll be at Galvalize pretty early tomorrow so maybe that rowing sesh that I wanted to do last post, and never happened, will finally reach fruition.
