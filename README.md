# AmazonWilsonScore

A website made using Python & Django that takes products on Amazon then uses Wilson Score Interval to prove which product is better based on the Amazon reviews as well as the output from the program.

**inspiration: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html**

I made this project because I like bionomial distrubitions and probability, so I wanted to leverage some of my knowledge and put it to work.

## Table of Contents

- [Website](#website)
- [Instructions](#instructions)
- [Wilson Score](#wilson-score)
  - [Formula in Python](#formula-in-python)
  - [How it is Used](#how-it-is-used)
    - [Interpretation of the Data Sets on Matplotlib](#interpretation-of-the-data-sets-on-matplotlib)
    - [Why Averaging Does Not Work](#why-averaging-does-not-work)

## Website

Website is here: placeholder

## Instructions

In the text-box, copy and paste mulitple Amazon ***product URLs (the front page of the product)*** and separate them with a **comma** `,`...
* ***Example***: url1, url2, url3
* ***Example of a product front page:*** https://www.amazon.com/Atomic-Habits-Proven-Build-Break/dp/0593189647/ref=tmm_pap_swatch_0?_encoding=UTF8&sr=8-1


![example](https://user-images.githubusercontent.com/27398502/228090923-1be5e504-984a-48c5-88e8-5912a3a98448.PNG)



## Wilson Score

The Wilson Score is a statistical method that can be used to determine the proportion of positive reviews for a product on Amazon. This method takes into account the total number of reviews, as well as the number of positive reviews, to provide a more accurate representation of the overall sentiment.

![image](https://user-images.githubusercontent.com/27398502/228088744-ef92adce-ec85-4aeb-a5f0-be5a70f52893.png)

* `p-hat` is the positive reviews out of total reviews
* `n` total number of positive and negative reviews
* `z`, in my case, is set to a default of `0.95` confidence

### Formula in Python

Here is the Wilson Score formula writtein in **Python**:

```python

def wilson_score(total_rating, review):
    #Amazon reviews are always out of 5
    constant = 5

    #sample size is total ratings
    n = int(total_rating.replace(',', ''))

    #p-hat or success is # of POSITIVE reviews; 
    x = float(review) / constant
    p = x

    z = 1.96 #uses a standard z-score of 95%
    deno = 1 + z**2/n
    nume = p + z**2/(2*n)

    deviation = cmath.sqrt((p*(1-p) / n) + (z**2 / (4*(n**2))))

    upper_bound = ((nume / deno) + ((z / deno) * deviation)) * 100
    lower_bound = ((nume / deno) - ((z / deno) * deviation)) * 100

    #rounding the numbers
    upper = round(upper_bound.real, 2)
    lower = round(lower_bound.real, 2)

    data_set.append([lower, upper])
    
```

Since this project uses Django, I have leveraged the Models() and the `total_rating` and `review` are values pertaining to the the URL(s) provided by the user. For more information, please check out the `def make_data()` function in the `calculate.py` script.

### How it is Used

In this case, when choosing **two or more different products from the same category** (i.e. two different types of TV's), the program will tell you which one is better by showing you a visual representation using Matplotlib. 

#### Interpretation of the Data Sets on Matplotlib

If a product has a high overall rating (e.g. 4.8 out of 5) and many total ratings, this suggests that the product is well-regarded by customers and has a high level of confidence that it will receive positive reviews. In this case, a confidence interval with a higher lower-bound and upper-bound range (e.g. 86 to 97) would provide a higher level of confidence that the true proportion of positive reviews is likely to be high.

On the other hand, a product with fewer total ratings and a lower overall rating may have a higher level of uncertainty surrounding the true proportion of positive reviews. In this case, a confidence interval with a lower lower-bound and upper-bound range (e.g. 61 to 71) may reflect a higher level of uncertainty and a wider range of possible outcomes for the proportion of positive reviews.

**So, with this additional information, it may be reasonable to suggest that the (86, 97) interval represents a more positive outcome than the (61, 71) interval.** However, please remember that confidence intervals are based on statistical estimates and are subject to uncertainty and potential sources of bias, so it's important to interpret the results with caution and in the context of the specific data and methods used to calculate them.

#### Why Averaging Does Not Work

Here is a citation from the paper above to describe why averaging does not work... "Average rating works fine if you always have a ton of ratings, but suppose item 1 has 2 positive ratings and 0 negative ratings. Suppose item 2 has 100 positive ratings and 1 negative rating. This algorithm [averaging algorithim] puts item two (tons of positive ratings) below item one (very few positive ratings)."



