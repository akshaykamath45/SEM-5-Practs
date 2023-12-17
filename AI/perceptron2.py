import numpy as np

l_pattern=np.array([
    [1,0,0],
    [1,0,0],
    [1,0,0],
    [1,1,1,]
]).reshape((1,12))

m_pattern=np.array([
   [1,0,1],
   [1,1,1],
   [1,0,1],
   [1,0,1] 
]).reshape((1,12))

class Perceptron:
    
    def __init__(self):
        self.weights=np.array([np.zeros(12)])
    
    def fit(self,inputs,labels,epoch=10):
        for _ in range(epoch):
            for i in range (len(inputs)):
                net_input=np.sum(inputs[i]*self.weights)
                output=1 if net_input>0 else 0
                delta_weight=0.5*(labels[i]-output)*inputs[i]
                self.weights+=delta_weight
        print(self.weights)
        
    def predict(self,inputs):
              net_input=np.sum(inputs*self.weights)       
              return 1 if net_input>0 else 0
        
    
perceptron=Perceptron()
perceptron.fit([l_pattern]*5+[m_pattern]*5,[1,1,1,1,1,0,0,0,0,0])  


                    
print(perceptron.predict(l_pattern))
print(perceptron.predict(m_pattern)) 