# Pricing

The retail sales data (offline) of a store typically shows the price per unit (PPU), volume/quantity of sales, and profit earned for a SKU/product across stores in cities (states). One can investigate the demand curve which is essentially the price & quantity relationship across the states. The same is true for online data that is, e-commerce.
The retail or ecommerce data is utilized to forecast volume (daily/weekly) of sales as to optimize revenue or profit margin with respect to the price of product. This exercise is price optimization or the pricing problem, wherein one maximizes either revenue or margin while optimizing the price which is subject to various factors such as competition, customer behavior, etc..

---

In **econometrics**, a log-log model is a regression model where both the dependent and independent variables are transformed using [logarithms](https://github.com/ranja-sarkar/Demand_curve/blob/684bb0e5986de176d93a967285202dd213c20091/logmodels.pdf). This transformation allows for interpretation of coefficients as elasticities, representing the percentage change in the dependent variable for a 1% change in the independent variable. 

<img width="323" alt="11" src="https://github.com/user-attachments/assets/8c85df63-83e9-4367-b52e-d088a9070af6" />


One can use [linear model plot](https://seaborn.pydata.org/generated/seaborn.lmplot.html) or [regression plot](https://seaborn.pydata.org/generated/seaborn.regplot.html) depending on the use-case, to visualize the demand curve. However, a linear regression model hardly works for estimating price elasticity, due to the presence of several influential factors and their inter-dependence.  

-----

**Price elasticity** is determined from the demand curve. It is defined as the change in quantity (demand) of product with unit change in price of the product.  

**Interpreting [price elasticity](https://github.com/ranja-sarkar/Demand_curve/blob/2b47fd744ea460c895c949ea4ea9d69c0002fb9f/notebooks/Price_elasticity.ipynb)**

<img width="265" alt="55" src="https://github.com/user-attachments/assets/f300bfa5-4521-4c49-8528-2024dc008edd" />

# Python libraries

▶️ [PyMC](https://www.pymc.io/) is a probabilistic programming library to build [Bayesian](https://www.youtube.com/watch?v=5NMxiOGL39M) models for pricing, and fit them using Markov chain Monte Carlo (MCMC) sampling methods.

Repo: https://github.com/pymc-devs/pymc

<img width="461" alt="22" src="https://github.com/user-attachments/assets/753cbfa0-d337-42d1-b41a-78fc7a575f4c" />


Please [refer](https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/GLM_linear.html) for a Bayesian generalized linear model (GLM) using pymc.

---

The [primer paper of 2020](https://github.com/ranja-sarkar/ranja-sarkar.github.io/blob/bc92b06b81a180450295ec81e75927a704a7b283/_posts/assets/Springer%20Nature_2020.pdf) details about Bayesian Modeling. It outlines WAMBS - 'When to Worry and how to Avoid the Misuse of Bayesian Statistics', while discussing prior distribution types that can be fed into the model, variable selection methods, MCMC & non-MCMC based sampling to arrive at posterior distributions, and commonly used Bayesian software (opensource) programs. 

---

▶️ [Stan](https://mc-stan.org/users/interfaces/pystan) is a package for Bayesian Inference and [pystan](https://github.com/stan-dev/pystan) is a python interface to it.

<img width="548" alt="33" src="https://github.com/user-attachments/assets/7b03ef9a-b542-4321-b301-3059f52494c2" />


-----


▶️ [Pyro](https://github.com/pyro-ppl/pyro) is a programming package for (deep) probabilistic modeling with python and pytorch.

<img width="628" alt="11" src="https://github.com/user-attachments/assets/23756f4e-a607-4680-8870-abee88ee67fa" />

# References

1. [Bayesian Hierarchical Linear Regression with pyro](https://num.pyro.ai/en/stable/tutorials/bayesian_hierarchical_linear_regression.html)

2. [Hierarchical modeling with stan](https://github.com/widdowquinn/Teaching-Stan-Hierarchical-Modelling)

3. [Regression modeling wuth stan](https://mc-stan.org/docs/stan-users-guide/regression.html)

4. [Using pymc2](https://people.duke.edu/~ccc14/sta-663/PyMC2.html)

5. [Spike and slab with pymc](https://docs.liesel-project.org/en/v0.3.0/tutorials/md/06-pymc.html)

6. [Gibbs sampling in spike and slab](https://github.com/AsaCooperStickland/Spike_And_Slab)
   
# Marketing

It is essential to measure the impact of marketing efforts to understand to what extent a sensitive segment of customers are retained and by sensitive I mean, the ones who help generate the company's most revenue. 

Assessing the difference between statistical significance and practical significance is important while making effective business decisions, particularly in marketing. 

There are far more intricacies in understanding whether a certain marketing strategy is meaningful in enhancing the buying behavior of consumers than what a statistical test reveals. Practical significance considers whether the difference between two actions (effect size) is large enough to be meaningful and relevant in a real-world context.

---

The measurement of the business impact a marketing strategy generates in the long-term when compared to no effort taken becomes complex as the effect might get diluted over time. Drawing causal inference is therefore hard in the long-term. Allocating advertising budget and estimating its impact on business in the long-term requires modeling and optimization. 

The measure is the difference between the effect generated in the customers stimulated with marketing gimmick (test group) and those not stimulated (control group). The effect has binary outcomes (Y) - 1 when the customer receives the stimulus (factual) and 0 when the customer does not recieve the stimulus (counterfactual). The stimulus is a treatment. This is called measuring causal effect.

<img width="293" height="89" alt="ce" src="https://github.com/user-attachments/assets/6eac43ea-7322-4903-8182-930a3d2aab57" />






