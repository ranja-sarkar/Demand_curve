# Pricing

The retail sales data (offline) of a store typically shows the price per unit (PPU), volume/quantity of sales, and profit earned for a SKU/product across stores in cities (states). One can investigate the demand curve which is essentially the price & quantity relationship across the states. The same is true for online data that is, e-commerce.
The retail or ecommerce data is utilized to forecast volume (daily/weekly) of sales as to optimize revenue or profit margin with respect to the price of product. This exercise is price optimization or the pricing problem, wherein one maximizes either revenue or margin while optimizing the price which is subject to various factors such as competition, customer behavior, etc..

---

In **econometrics**, a log-log model is a regression model where both the dependent and independent variables are transformed using logarithms. This transformation allows for interpretation of coefficients as elasticities, representing the percentage change in the dependent variable for a 1% change in the independent variable. 

<img width="323" alt="11" src="https://github.com/user-attachments/assets/8c85df63-83e9-4367-b52e-d088a9070af6" />


One can use [linear model plot](https://seaborn.pydata.org/generated/seaborn.lmplot.html) or [regression plot](https://seaborn.pydata.org/generated/seaborn.regplot.html) depending on the use-case, to visualize the demand curve. However, a linear regression model hardly works for estimating price elasticity, due to the presence of several influential factors and their inter-dependence.  

-----

**Price elasticity** is determined from the demand curve and is defined as the **change in quantity** or demand of product with **unit change in price** of the product.  

**Interpreting price elasticity :-**

<img width="265" alt="55" src="https://github.com/user-attachments/assets/f300bfa5-4521-4c49-8528-2024dc008edd" />

Follow the notebook for a demo of **price elasticity**: https://github.com/ranja-sarkar/Demand_curve/blob/main/notebooks/Price_elasticity.ipynb

Follow the notebook for a demo of **dynamic pricing of SKU** to increase revenue: https://github.com/ranja-sarkar/Demand_curve/blob/main/notebooks/Dynamic_pricing.ipynb

-------


▶️ **PyMC** is a probabilistic programming python library to build Bayesian models and fit them using Markov chain Monte Carlo (MCMC) sampling methods: https://www.pymc.io/

Repo: https://github.com/pymc-devs/pymc

<img width="461" alt="22" src="https://github.com/user-attachments/assets/753cbfa0-d337-42d1-b41a-78fc7a575f4c" />

**How Bayes Theorem (Bayesian Inference) works?** 

https://www.youtube.com/watch?v=5NMxiOGL39M


**Bayesian GLM (Linear Regression) in PyMC:** https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/GLM_linear.html

For a simple demo of **Bayesian linear model** with single regressor dataset: https://github.com/ranja-sarkar/Demand_curve/blob/main/notebooks/Bayesian.ipynb


**The following Nature paper (2020) details about Bayesian Modeling.** It outlines WAMBS - 'When to Worry and how to Avoid the Misuse of Bayesian Statistics' while discussing prior distribution types that can be fed into the model, variable selection methods, MCMC & non-MCMC based sampling to arrive at posterior distributions, and commonly used Bayesian software (open-source) programs. 

https://github.com/ranja-sarkar/stats/blob/main/papers/Springer%20Nature_2020.pdf

**Pooled and hierarchical models using PyMC2:** https://people.duke.edu/~ccc14/sta-663/PyMC2.html

**Gibbs sampling to get sample from posterior with 'spike and slab' or Gaussian priors:** https://github.com/AsaCooperStickland/Spike_And_Slab

**Spike and Slab model with pymc**: https://docs.liesel-project.org/en/v0.3.0/tutorials/md/06-pymc.html

------

▶️ **Stan** is package for Bayesian Inference and **pystan** is a python interface to it.

https://mc-stan.org/users/interfaces/pystan

Repo: https://github.com/stan-dev/pystan

<img width="548" alt="33" src="https://github.com/user-attachments/assets/7b03ef9a-b542-4321-b301-3059f52494c2" />


Regression models with stan: https://mc-stan.org/docs/stan-users-guide/regression.html

**How Bayesian Inference works**: https://www.youtube.com/watch?v=5NMxiOGL39M&t=1s


**Bayesian (multilevel) hierarchical modeling:** https://github.com/widdowquinn/Teaching-Stan-Hierarchical-Modelling

**About unpooled, pooled, and partial-pooled models:** https://widdowquinn.github.io/Teaching-Stan-Hierarchical-Modelling/

-----


▶️ **Pyro** (python & pytorch) is a package for (deep) probabilistic programming/modeling.

**Bayesian Hierarchical Linear Regression with pyro:** https://num.pyro.ai/en/stable/tutorials/bayesian_hierarchical_linear_regression.html

**About pyro**: https://github.com/pyro-ppl/pyro

<img width="628" alt="11" src="https://github.com/user-attachments/assets/23756f4e-a607-4680-8870-abee88ee67fa" />

# Marketing


