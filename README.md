# Retail Data

The retail sales data of a store typically shows the price per unit - PPU, volume of sales, and profit earned across stores in cities of states (region/country). One can investigate the **demand curve** (price & quantity relationship) of a product across states. Demand curves can be used either for an individual consumer or for all consumers in a particular market (market demand curve).

<img width="359" alt="image" src="https://github.com/ranja-sarkar/SuperStoreSales/assets/101544669/97913eca-24db-4065-a946-81d3b651767f">

The data can eventually be utilized to forecast (daily/weekly) sales/volume as well as to optimize revenue or profit margin wrt the price of product. This exercise is price optimization (pricing problem) wherein one maximizes either revenue or margin while optimizing the price.

<img width="227" alt="image" src="https://github.com/ranja-sarkar/SuperStoreSales/assets/101544669/9c591eea-1b8a-4859-ab67-7250ed081a67">

One can use Linear Model plot (multiple relationships) or Regression plot (single relationship) depending on the use-case to create the demand curve. However, a **linear regression model hardly works for price elasticity** and optimization, where price elasticity is the change in product quantity demanded or aupplied with unit change in price of the product. 

**Bayesian GLM (Linear Regression) in PyMC:** https://www.pymc.io/projects/docs/en/stable/learn/core_notebooks/GLM_linear.html

**Gibbs sampling to get sample from posterior with 'spike and slab' or Gaussian priors:** https://github.com/AsaCooperStickland/Spike_And_Slab

