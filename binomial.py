import numpy as np
def binomial_py(strike):
  """
  Binomial option pricing via looping
  
  Parameters
  ===========
  strike: Float
    Strike price of the European call option
  """
  # LOOP 1 Index Levels
  s = np.zeros((M + 1, M + 1), dtype = np.float64)
  # Index level array
  s[0,0] = S0
  z1 = 0
  for j in xrange(1, M + 1, 1):
    z1 = z1 + 1
    for i in xrange(z1 + 1):
      S[i, j] = S[0,0] * (u**j) * (d ** (i * 2))
  # Loop 2 - Inner Values
  iv = np.zeros((M+1, M+1), dtype = np.float64)
    # inner value array
  z2 = 0
  for j in xrange(0, M + 1, 1):
    for i in xrange(z2 + 1):
      iv[i, j] = max(S[i, j] - strike, 0)
    z2 = z2 + 1
  # Loop 3 = Valuation
  pv  = np.zeros((M + 1, M + 1), dtype = np.float64)
  # present value array
  pv[:, M] = iv[:, M] #initialize last time point
  z3 = M + 1
  for j in xrange(M - 1, -1, -1):
    z3 = z3 - 1
    for i in xrange(z3):
      pv[i,j] = (q * pv[i, j + 1] + (1 - q) * pv[i + 1, j+1]) * df
  return pv[0,0]
