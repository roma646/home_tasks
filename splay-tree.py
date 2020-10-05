from Node import Node
from splay import *
import copy



def F(x, s):
	return (x + s) % 1000000001


def plus(i, tree):
	if find(tree, i).key == i:
		return tree
	else:
		tree = add(tree, Node(i))
		return tree


def minos(i, tree):
	if find(tree, i).key != i:
		return
	else:
		tree = remove(find(tree, i))
		return tree


def search(i, tree):
	if find(tree, i).key == i:
		return 'Found'
	else:
	 	return 'Not found' 


def sum_from_l_r(f_l, f_r, tree):
	tree_copy = copy.deepcopy(tree)
	tree_1, tree_2 = split(tree, f_l)
	tree_1_1, tree_1_2 = split(tree_2, f_r + 0.000001)
	return sum_all(tree_1_1), tree_copy





tree, ss = None, 0 
res = []
n = int(input())


for i in range(n):
	s = input()
	if s[0] == '+':
		if tree == None:
			tree = Node(F(int(s[2:]), ss))
		else:
			tree = plus(F(ss, int(s[2:])), tree)
	if s[0] == '-':
		if tree == None:
			continue
		else:
			tree = minos(F(ss, int(s[2:])), tree)
	if s[0] == '?':
		if tree == None:
			res.append('Not found')
		else:
			res.append(search(F(ss, int(s[2:])), tree))
	if s[0] == 's':
		if tree == None:
			res.append(0)
		else:
			s = s[2:]
			l,r = map(int, s.split())
			ss, tree = sum_from_l_r(F(l, ss), F(r, ss), tree)
			res.append(ss)

for i in res:
	print(i)

