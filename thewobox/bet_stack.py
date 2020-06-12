

from stack import stack

class BET():
	class Node():
		def __init__(self, value):
			self.value = value
			self.left = None
			self.right = None

	def __init__(self, exp):
		self.exp = exp
		self.S = stack()

	def InOrderT(self, t):
		if t is not None:
			self.InOrderT(t.left)
			print(f"value ::::: {t.value}")
			self.InOrderT(t.right)

	def isOp(self, c):
		if c == '+' or c == '-' or c == '*' or c == '/' or c == '^':
			return True
		else:
			return False

	def buildTree(self):
		for c in self.exp:
			if not self.isOp(c):
				t = self.Node(c)
				self.S.push(t)
			else:
				t = self.Node(c)
				t1 = self.S.pop()
				t2 = self.S.pop()
				t.right = t1
				t.left = t2
				self.S.push(t)
		t = self.S.pop()
		self.InOrderT(t)



ex = BET("ab+ef*g*-")
ex.buildTree()