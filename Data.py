

import math
import pylab
import numpy
import scipy.stats as stats

class data(object):
    def __init__(self, x_list):
        self.x_list = x_list
        self.n = len(self.x_list)
        self.sum = 0
        for x in self.x_list:
            self.sum += x
        self.sumsq = 0
        for x in self.x_list:
            self.sumsq += x**2
    
    def getList(self):
        return self.x_list
        
    def getNum(self):
        return self.n
    
    def getSum(self):
        return self.sum
    
    def getSqSum(self):
        return self.sumsq
    
    def addlist(self,List): 
        for a in List:
            self.x_list.append(a)
            self.sum += int(a)
            self.sumsq += int(a)**2
        self.n = len(self.x_list)
    
    def addlistY(self,List):
        for a in List:
            self.y_list.append(a)
            self.sumy += int(a)
            self.sumysq += int(a)**2
        self.ny = len(self.y_list)
    
    def clearlist(self):
        del self.x_list[:]  
        self.__init__(self.x_list)
    

    def mean(self):
        mean = self.sum/self.n
        return mean
    
    def Variance(self):
        Var = (self.sumsq/self.n) - (self.sum/self.n)**2
        return Var
        
    def VarianceY(self):
        Vary = (self.sumysq/self.ny) - (self.sumy/self.ny)**2
        return Vary
    
    def stdev(self):
        return math.sqrt(self.Variance())
    
    def stdevY(self):
        return math.sqrt(self.VarianceY())
        

    

    

    

                
    # def __str__(self):
    #     if self.nx >= self.ny:
    #         length = self.nx
    #     else:
    #         length = self.ny
    #     print('\tx:'+'\t\t'+'y:')
    #     output = ''
    #     for i in range(length):
    #         try:
    #             tab = '\t\t'
    #             if len(str(self.x_list[i])) >=4 and len(str(self.x_list[i])) < 8:
    #                 tab = '\t'
    #             elif len(str(self.x_list[i])) >=8:
    #                 tab = '|'
    #             output +='\t'+str(self.x_list[i])+tab+str(self.y_list[i])+'\n'
    #         except IndexError:
    #             if length == self.nx:
    #                 output += '\t'+str(self.x_list[i])+'\n'
    #             else:
    #                 output += '\t  '+tab+str(self.y_list[i])+'\n'
    #     return output
                


        
        
        
 
    
 
# import pandas    
# def read_csv(filename, form = 'd', column = None, column_as = 'x'):
#     """
#     Parameters
#     ----------
#     filename : A string which is the name and location of a csv file you 
#         want opened
#     form : The format which you want your data to be represented, optional
#         'l' = list (select a specific column), 'd' = dict, 
#         'p_df' = pandas dataframe, 'p_s' = pandas series. The default is 'd'.
#     column: A list, of which the contents are the string headers of the 
#         columns you want to extract. default is all of them
#     column_as : If you choose maximum two specific columns, then you can 
#         set these to be the values of x and y of class data. default of one list is x.
  
#     Returns
#     -------
#     The contents of the csv file in the chosen data format
#     """
#     with open(filename) as csvfile:
#         df = pandas.read_csv(csvfile)
#         headers = list(df.columns)
#         if column == None:
#             if form == 'd':
#                 csvdict = {}
#                 for name in headers:
#                     values = [] 
#                     for value in range(len(df[[name]])):
#                         values.append(df[name][[value]])
#                     csvdict[name] = values
#                 return csvdict
#             elif form == 'p_df':
#                 return df
#             elif form == 'p_s':
#                 if len(headers) > 1:
#                     raise TypeError('More than one column can\'t be represented in a series')
#                     return None
#                 else:
#                     return df
#             elif form == 'l':
#                 if len(headers) > 1:
#                     raise TypeError('More than one column can\'t be represented in a list')
#                     return None
#                 else:
#                     csvlist = []
#                     for value in range(len(df[headers])):
#                         csvlist.append(df[headers][[value]])  
#                     return csvlist
#             else:
#                 raise TypeError('Can\'t convert to that type of format yet')
#                 return None
        
#         else:
#             if type(column) == str:
                


# def test__read_csv_dict(filename):
#     csvdict = read_csv(filename)
#     print(csvdict.keys())
#     print(csvdict['Tempin (C)'][0])
# test__read_csv_dict('C:/Users/oscar/Google Drive/Python/Personal projects/CSV files/PWSFuentesRebato2020-10.csv')


        
        
        
        
        
      
