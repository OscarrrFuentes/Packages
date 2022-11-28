# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 17:45:56 2020

@author: oscar
"""

from Data import data
import math
import pylab
import numpy
import scipy.stats as stats

class variables(data):
    def __init__(self, xlist, ylist):
        self.x = data(xlist)
        self.y = data(ylist)
        self.x_list = self.x.getList()
        self.y_list = self.y.getList()
        self.nx = self.x.getNum()
        self.ny = self.y.getNum()
        self.sumx = self.x.getSum()
        self.sumy = self.y.getSum()
        self.sumxsq = self.x.getSqSum()
        self.sumysq = self.y.getSqSum()
        self.sumxy = 0
        if self.nx == self.ny:
            for variable in range(self.nx):
                self.sumxy += self.x_list[variable]*self.y_list[variable]
    
    def updatesumxy(self):
        if self.nx == self.ny:
            self.sumxy = 0
            for i in range(self.nx):
                self.sumxy += self.x.x_list[i]*self.y.x_list[i]
        else:
            raise IndexError('Different amount of observations of x and y')

    def addListX(self, List):
        self.x.addlist(List)
        try:
            self.updatesumxy()
        except IndexError:
            pass
    
    def addListY(self, List):
        self.y.addlist(List)
        try:
            self.updatesumxy()
        except IndexError:
            pass
            
    def clearlistX(self):
        self.x.clearlist()
        
    def clearListY(self):
        self.y.clearlist()
    
    def meanX(self):
        return self.x.mean()

    def meanY(self):
        return self.y.mean()
    
    def VarX(self):
        return self.x.Variance()
    
    def VarY(self):
        return self.y.Variance()
    
    def stdevX(self):
        return self.x.stdev()
    
    def stdevY(self):
        return self.y.stdev()

    def find_r(self):
        if self.nx == self.ny:
            self.updatesumxy()
            top = float(self.sumxy-self.nx*self.meanX()*self.meanY())
            bottom = float(math.sqrt((self.sumxsq-self.nx*(self.meanX()**2))*(self.sumysq-self.ny*(self.meanY()**2))))
            r = top/bottom
            return r   
        else:
            raise IndexError('Different amount of variables in x and y')

    def plot(self, x_label = 'x', y_label = 'y', title = 'Plot', form = 'bo'):
        try:
            pylab.plot(self.x_list, self.y_list, form)
            pylab.title(title)
            pylab.xlabel(x_label)
            pylab.ylabel(y_label)
            pylab.show()
        except ValueError:
            print('Different amount of observations of x and y')

    def distribute(self, data = 'x'):
        if data == 'x':
            if self.nx <30:
                raise ValueError('Not enough values of x for CLT to apply')
            else:
                pylab.close()
                sigma = self.stdevX()
                xnorm = numpy.linspace(self.mean() - 3*sigma, self.mean() + 3*sigma, 100)
                pylab.plot(xnorm, stats.norm.pdf(xnorm, self.mean(), sigma))
                pylab.show()
        elif data == 'y':
            if self.ny <30:
                raise ValueError('Not enough values of y for CLT to apply')
            else:
                pylab.close()
                sigma = self.stdevY()
                ynorm = numpy.linspace(self.meanY() - 3*sigma, self.meanY() + 3*sigma, 100)
                pylab.plot(ynorm, stats.norm.pdf(ynorm, self.meanY(), sigma))
                pylab.show()
        elif data == 'both':
            if self.nx<30 or self.ny<30:
               raise ValueError('Check that both lists have more than 30 values for CLT to apply') 
            else:
                pylab.close()
                sigmax = self.stdevX()
                xnorm = numpy.linspace(self.mean() - 3*sigmax, self.mean() + 3*sigmax, 100)
                sigmay = self.stdevY()
                ynorm = numpy.linspace(self.meanY() - 3*sigmay, self.meanY() + 3*sigmay, 100)
                pylab.plot(xnorm, stats.norm.pdf(xnorm, self.mean(), sigmax), label = 'x')
                pylab.plot(ynorm, stats.norm.pdf(ynorm, self.meanY(), sigmay), label = 'y')
                pylab.legend(loc='best')
                pylab.show()
      
# pylab.plot(stats.norm.pdf(0, 1))   
# trial = variables([1, 2, 3, 4], [5, 4, 3, 2])
# trial.clearlistX()
# print(trial.x_list)