import numpy as np

class pcn:
	def __init__(self,input,target):
		self.input = np.insert(input,0,-1,axis=1)
		self.target = target
		self.w = np.random.rand(self.input.shape[1],target.shape[1])*0.1-0.05

	def renew(self,input,dif):
		self.w = self.w - self.t_rate*np.dot(input,dif)

	def train(self,t_rate,iter):
		self.t_rate = t_rate
		for i in range(iter):
			result = np.where(np.dot(self.input,self.w)>0,1,0)
			print("Iteration : ",i,"\n",self.w,"\nresult : \n",result,"\n")
			if not np.array_equal(target, result):
				self.renew(np.transpose(self.input),result-self.target)


input = np.array([[0,0],[0,1],[1,0],[1,1]])
target = np.array([[0],[1],[1],[1]])
p = pcn(input,target)
p.train(0.25,10)
