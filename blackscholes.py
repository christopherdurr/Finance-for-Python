#
# Valuation of European Call Options in Black-Scholes-Merton Model
# Including Vega Function and implied volatility Estimation
# bsm_functions.py
#

# Analytical Black-Scholes-Merton (BSM) Formula

def bsm_call_value(S0, K, T, r, sigma):
    """
    Valuation of European call option in BSM model.
    
    Parameters
    ==========
    s0 : Float
      initial stock/index level
    K : Float
      Strike Price
    T: Float
      Constant risk-free short rate
    sigma: Float
      Volatility Factor in Diffusion Term
      
    Returns
    =======
    
 df
    value: Float
      Present value of the European call option]
    """
