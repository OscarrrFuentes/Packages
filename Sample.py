# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:01:03 2020

@author: oscar
"""
from Data import data
import pylab
import math
import numpy
import scipy.stats as stats

class sample(data):
    def __init__(self, x):
        data.__init__(self, x)
    
    def distributeNorm(self):
        pylab.close()
        sigma = self.stdevX()
        mu = self.mean()
        xnorm = numpy.linspace(mu - 4*sigma, mu + 4*sigma, 200)
        pylab.plot(xnorm, stats.norm.pdf(xnorm, mu, sigma))
        pylab.show()
        print('X̄ ~ N('+str(mu)+','+str(round(sigma**2, 3))+')')
        
    def __str__(self):
        output = '\tx:\n'
        for i in range(self.nx):
            output+='\t'+str(self.x_list[i])+'\n'
        return output
    
    def hypothesis(self, h1, mu, p = 95, sigma = None):
        '''
        
        Parameters
        ----------
        h1 : String
            What do you want the alternative hypothesis to be
            Possible inputs: '!=', '>', '<'
        mu : Float
            What value are you testing against (population mean)
        p : float, 0<p<100, optional
            What do you want the confidence level to be, default = 95%
        sigma : Float, optional
            The sample standard deviation (if you know it)
            Default is None, assuming that the population variance is unknown

        Returns
        -------
        Boolean regarding the null hypothesis and a string statement describing the result

        '''
        freedom = self.n-1
        var_estimate = self.Variance()*(self.n/(self.n-1))
        s_mean = self.mean()
        a = 1-(p/100)
        t = None
        z = None
        error = ''
        if type(sigma) == float or type(sigma) == int:
            z = (s_mean-mu)/(sigma/(math.sqrt(self.n)))
            values = stats.norm.cdf([z], loc = mu, scale = sigma)
            p_val = 1-values[0]
        else:
            t = (s_mean-mu)/((math.sqrt(var_estimate))/(math.sqrt(self.n)))
            values = stats.t.cdf([t], freedom, loc = mu, scale = math.sqrt(var_estimate))
            p_val = 1-values[0]
        if h1 == '!=':
            if (p_val*2) <= a:
                answer, statement = False, 'There is sufficient evidence to reject the null hypothesis at the '+str(p)+'% confidence level'
            else:
                answer, statement = True, 'There is insufficient evidence to reject the null hypothesis at the '+str(p)+'% confidence level'
        elif h1 == '<' or h1 == '>':
            if p_val <= a:
                answer, statement = False, 'There is sufficient evidence to reject the null hypothesis at the '+str(p)+'% confidence level'
            else:
                answer, statement = True, 'There is insufficient evidence to reject the null hypothesis at the '+str(p)+'% confidence level'
        else:
            raise ValueError('The input for the alternative hypothesis was invalid')
        if answer:
            pmu = input('Input a new specific value of mu to find the probability of a Type II Error, otherwise press enter')
            if len(pmu)>0:
                pmu = float(pmu)
                if pmu < mu:
                    if t!= None:
                        T2_prob = stats.t.cdf([pmu], freedom, loc = mu, scale = math.sqrt(var_estimate))
                    else:
                        T2_prob = stats.norm.cdf([pmu], loc = mu, scale = sigma)
                else:
                    if t!= None:
                        T2_prob = 1 - stats.t.cdf([pmu], freedom, loc = mu, scale = math.sqrt(var_estimate))
                    else:
                        T2_prob = 1 - stats.norm.cdf([pmu], loc = mu, scale = sigma)
                error = 'The probability of a type II Error when the true mean = '+str(pmu)+'is: '+str(T2_prob)
        else:
            error = 'The probability of a type I Error is: '+str(round(a, 3))
        return statement +'\n'+error
        


