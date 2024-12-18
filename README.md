# Retail Data

The retail sales data of a store typically shows the price per unit - PPU, volume of sales, and profit earned across stores in cities of states (region/country). One can investigate the **demand curve** (price & quantity relationship) of a product across states. Demand curves can be used either for an individual consumer or for all consumers in a particular market (market demand curve).

<img width="359" alt="image" src="https://github.com/ranja-sarkar/SuperStoreSales/assets/101544669/97913eca-24db-4065-a946-81d3b651767f">

The retail data is utilized to forecast (daily/weekly) sales or volume as well as to optimize revenue or profit margin wrt the price of product. This exercise is price optimization (pricing problem) wherein one maximizes either revenue or margin while optimizing the price which is subject to various factors such as competition, customer behavior, etc..

<img width="227" alt="image" src="https://github.com/ranja-sarkar/SuperStoreSales/assets/101544669/9c591eea-1b8a-4859-ab67-7250ed081a67">

One can use Linear Model plot (multiple relationships) or Regression plot (single relationship) depending on the use-case to create the demand curve. However, a **linear regression model hardly works for price elasticity** and optimization, where price elasticity is the change in product quantity demanded or aupplied with unit change in price of the product. 

**Interpreting price elasticity**

<img width="265" alt="55" src="https://github.com/user-attachments/assets/f300bfa5-4521-4c49-8528-2024dc008edd" />


▶️ **PyMC** is a probabilistic programming python library to build Bayesian models and fit them using Markov chain Monte Carlo (MCMC) sampling methods: https://www.pymc.io/

Repo: https://github.com/pymc-devs/pymc

<img width="461" alt="22" src="https://github.com/user-attachments/assets/753cbfa0-d337-42d1-b41a-78fc7a575f4c" />


**Bayesian GLM (Linear Regression) in PyMC:** https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/GLM_linear.html

The following Nature paper (2020) details about Bayesian Modeling. It outlines WAMBS - 'When to Worry and how to Avoid the Misuse of Bayesian Statistics' while discussing prior distribution types that can be fed into the model, variable selection methods, MCMC & non-MCMC based sampling to arrive at posterior distributions, and commonly used Bayesian software (open-source) programs. 

https://github.com/ranja-sarkar/stats/blob/main/papers/Springer%20Nature_2020.pdf


**Gibbs sampling to get sample from posterior with 'spike and slab' or Gaussian priors:** https://github.com/AsaCooperStickland/Spike_And_Slab

**Spike and Slab model with pymc**: https://docs.liesel-project.org/en/v0.3.0/tutorials/md/06-pymc.html


▶️ **Stan** is package for Bayesian Inference and **pystan** is a python interface to it.

https://mc-stan.org/users/interfaces/pystan

Repo: https://github.com/stan-dev/pystan

<img width="548" alt="33" src="https://github.com/user-attachments/assets/7b03ef9a-b542-4321-b301-3059f52494c2" />


Regression models with stan: https://mc-stan.org/docs/stan-users-guide/regression.html

**How Bayesian Inference works**: https://www.youtube.com/watch?v=5NMxiOGL39M&t=1s


**Bayesian (multilevel) hierarchical modeling:** https://github.com/widdowquinn/Teaching-Stan-Hierarchical-Modelling

**About unpooled, pooled, and partial-pooled models:** https://widdowquinn.github.io/Teaching-Stan-Hierarchical-Modelling/

▶️ **Pyro** (python & pytorch) is a package for (deep) probabilistic programming/modeling.

**Bayesian Hierarchical Linear Regression with pyro:** https://num.pyro.ai/en/stable/tutorials/bayesian_hierarchical_linear_regression.html

**About pyro**: https://github.com/pyro-ppl/pyro

<img width="628" alt="11" src="https://github.com/user-attachments/assets/23756f4e-a607-4680-8870-abee88ee67fa" />


