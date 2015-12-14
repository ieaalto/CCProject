import random

class Markov:
    
    def __init__(self, order=2, a=0.0):
        self.order = order
        self.a = a
        self.count = {}
        self.total = {}
        self.P = {}
        
    def learn(self, data):
        for i in range(len(data)-self.order):
            k = tuple(data[i : i +self.order])
            g = data[i + self.order]
            
            if k not in self.count: self.count[k] = {}      
            self.count[k][g] = 1 if g not in self.count[k] else self.count[k][g]+1
            self.total[k] = 1 if k not in self.total else self.total[k]+1                
        
        for k in self.count.keys():
            for g in self.count[k]:
                if k not in self.P : self.P[k] = {}
                self.P[k][g] = self.count[k][g]/float(self.total[k])
                
        self.reset()
                
    
    def evaluate(self, data, a = "NaN"):
        
        a = a if a != "NaN" else self.a    
        p = 0.0        

        for i in range(len(data)-self.order):
             k = tuple(data[i:i+self.order])
             g = data[i+self.order]
             
             total = self.total[k] if k in self.total else 1
             count = self.count[k][g] if k in self.count and g in self.count[k] else 0
             
             p += (count + a)/(total + a)  
             
        return p/len(data)
             
    def generate(self, n):
        
        k = tuple(self.previous)
        output = list(k)
        
        for i in range(n):
            p_remaining = 1.0
            for g in self.P[k]:
                if random.uniform(0.0, 1.0) <= self.P[k][g]/p_remaining:
                    output.append(g)
                    k_list = list(k)[1:]
                    k_list.append(g)
                    k = tuple(k_list)
                    break
                p_remaining -= self.P[k][g]
                    
        return output
        
    def reset(self):
        self.previous = list(random.choice(list(self.P.keys())))
    
    def generate_one(self):
        k = tuple(self.previous)
        p_remaining = 1.0
        for g in self.P[k]:
            if random.uniform(0.0, 1.0) <= self.P[k][g]/p_remaining:
                self.previous = self.previous[1:]
                self.previous.append(g)
                return g
            p_remaining -= self.P[k][g]
                
    
        
    
             
        