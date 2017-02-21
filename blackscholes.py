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
   
    value: Float
      Present value of the European call option]
    """
    
    from math import log, sqrt, exp
    from scipy import stats
    
    s0 = float(s0)
    d1 = (log(s0/ K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(s0/ K) + (r - 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    value = (s0 * stats.norm.cdf(d1, 0.0, 1.0)
            - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    
    # stats.norm.cdf -> Cumulative distribution function for normal distribution
    #
    
    return value

# Vega Function

def bsm_vega(S0, K, T, r, sigma):
    """
    Vega of european option in BSM Model. 
    
    Parameters
    ==========
    s0 : Float
        initial stock/index level
    K : Float
        strike price
    T : Float
        Maturity date (in year fractions)
    r : float
        constant risk-free short rate
    sigma : float 
        volatility factor in diffusion term
    Returns
    =======
    vega : Float
        Partial derivative of BSM formula with respect to sigma, i.e. Vega
    """
    
    from math import log, sqrt
    from scipy import stats
    
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T / (sigma * sqrt(T))
    vega = S0 * stats.normcdf(d1, 0.0, 1.0) * sqrt(T)
    return vega
              
# Implied volatility function

def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it = 100):
    """ 
    Implied volatility of European call option in BSM model
    
    Parameters
    ==========
    S0 : Float
        Initial stock/index level
    K : Float
        Strike Price
    T : Float
        Maturity Date (in year fractions)
    r : Float
        Constant risk-free short rate
    sigma_est : Float
        Estimate of impl. volatility
    it : integer
        Number of iterations
        
    Returns
    =======
    sigma_est : Float
        Numerically estimated implied volatility
    """
    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0)
                        / bsm_vega(S0, K, T, r, sigma_est))
    return sigma_est
         
          
          
          
        
