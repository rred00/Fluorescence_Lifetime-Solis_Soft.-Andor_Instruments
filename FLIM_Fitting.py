#!/usr/bin/env python
# coding: utf-8

# In[1]:


## to fit the pixel-wise, creating a class 

class Fitting:
    def __init__(self, delay):
        self.delay = delay  # time bin width (s)

    # Single Exponential decay function 
    def expo_decay(self, t, A, tau, B,center):
        y=np.zeros_like(t)
        m=(t>= center)
        return A * np.exp(-(t[m]-center)/tau)
        
    ## Bi-exponential decay fucntion
    def expo_decay(self, t, A1,A2, tau1,tau2, B,center):
         y=np.zeros_like(t)
         m=(t>= center)
         return A1* np.exp(-(t[m]-center)/tau1)+ A2 * np.exp(-(t[m]-center)/tau2)
    

    # IRF function (Gaussian) 
    def irf_func(self, Nt, delay, center, width):
        irf_t = np.arange(Nt) * delay
        irf = np.exp(-0.5 * ((irf_t - center)/width)**2) 
        irf /= irf.sum()
        return irf

    # Convolved model for single exponential decay can be replaced by the bi-exponential
    def model_01(self, t, A, tau, B,center,width):
        decay = self.expo_decay(t, A, tau, B,center)
        irf = self.irf_func(len(t), delay, center, width )
        conv = fftconvolve(decay, irf, mode="full")[:len(t)]
        return conv+B

    # Single pixel fitting 
    def fit_pixel(self, t, decay_curve,p0,bound):
        try:
            popt, _ = curve_fit(self.model_01, t, decay_curve,
                                p0,
                                bounds=bound)
            return popt  # (A, tau, B,center,width, center)
        except RuntimeError:
            return [np.nan, np.nan, np.nan]


# In[ ]:




