import pylab as py

class balance(object):
    '''
    
    A single value which is the current bank balance
    
    '''
    
    def __init__(self, balance): #initialises the value
        self.balance = balance
    
    def __str__(self): #A user-friendly string showing current balance
        return 'Current balance: '+str(self.balance)
    
    def getBalance(self): #Returns only the value
        return self.balance
    
    def changeBalance(self, inp, inp1): 
        '''
        
        Parameters
        ----------
        inp : either "in" or "out".
        inp1 : How much money is being added or taken away.

        Changes the value of balance

        '''
        if inp == 'in':
            self.balance += inp1
        elif inp == 'out':
            self.balance -= inp1
        else:
            raise ValueError ('Sorry, I didnt get that. Please call the function again with either "in" or "out", then a value')




class income(object):
    def __init__(self, source, value): #initialises
        self.source = source
        self.value = value
    
    def getval(self): #returns the value
        return self.value
    
    def getsource(self): #returns the source of income
        return self.source
    
    def __str__(self): #A user-friendly statement of source and value
        return 'INCOME\nSource: '+self.source+'   Value: '+ str(self.value)
    
    def combine(self, other):
        '''
        Input: Another income variable
        Output: A new variable with combined sources and values added together
        
        '''
        
        newval = self.value+other.value
        newsource = self.source +' & '+other.source
        newinc = income(newsource, newval)
        return newinc
  
    
class outgoing(object):
    def __init__(self, source, value): #initialises
        self.source = source
        self.value = value

    def getval(self): #returns the value
        return self.value
    
    def getsource(self): #returns the source
        return self.source
    
    def __str__(self):
        return 'OUTGOING\nSource: '+self.source+'   Value: '+ str(self.value)
    
    def combine(self, other):
        '''
        Input: Another outgoing variable
        Output: A new variable with combined sources and values added together
        
        '''
        
        newval = self.value+other.value
        newsource = self.source +' & '+other.source
        newout = outgoing(newsource, newval)
        return newout
    
def project(bal, inc, out, n):
    '''
    Parameters:
        bal == a balance object
        inc == an income object
        out == an outgoing object
        n == the number of weeks the projection is for
    Output:
        Returns a value which is the final balance after n number of weeks with weekly income and outgoing values
    
    '''
    
    bal = bal.getBalance()
    inc = inc.getval()
    out = out.getval()
    newbal = 0
    try:
        newbal = bal + (inc - out)*n
    except:
        raise TypeError ('Use "balance", "income" and "outgoing" objects, followed by number of weeks')
    return newbal

def projectplot(bal, inc, out, n):
    '''
    Parameters:
        bal == a balance object
        inc == an income object
        out == an outgoing object
        n == the number of weeks the projection is for
    Output:
        Shows a plot for the weekly increase in balance over n number of weeks
        
    '''
    
    x = []
    y = []
    for num in range(n+1):
        x.append(num)
        y.append(project(bal, inc, out, num))
    py.figure()
    py.title('Balance Increase')
    py.xlabel('Weeks')
    py.ylabel('Balance')
    py.plot(x, y)
    py.annotate('FINAL BALANCE:\n      '+str(y[-1]), (x[-1],y[-1]))