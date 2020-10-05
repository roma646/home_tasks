def set_parent(child, parent):
	if child != None:
		child.parent = parent

def add(root, v):
	if root == None:
		return v
	if root.key <= v.key:
		if root.right == None:
			root.right = v
			keep_parent(root)
			v = splay(v)
			return v
		else:
			add(root.right, v)
	else:
		if root.left == None:
			root.left = v
			keep_parent(root)
			splay(v)
			return v
		else:
			add(root.left, v)
	return v


def keep_parent(v):
	set_parent(v.left, v)
	set_parent(v.right, v)


def rotate(parent, child):

	gparent = parent.parent
	if gparent != None:
		if gparent.left == parent:
			gparent.left = child
		else:
			gparent.right = child

	if parent.left == child:
		parent.left = child.right
		child.right = parent
	else:
		parent.right = child.left
		child.left = parent
	keep_parent(parent)
	keep_parent(child)
	child.parent = gparent


			
def splay(v):
	if v == None:
		return None

	p = v.parent
	if p == None:
		return v

	g = p.parent
	if g == None:
		rotate(p, v)
		return v

	if g.left == p:
		if p.left == v:
			rotate(g, p)
			rotate(p, v)
			return splay(v)
		if p.right == v:
			rotate(p, v)
			rotate(g, v)
			return splay(v)

	if g.right == p:
		if p.right == v:
			rotate(g, p)
			rotate(p, v)
			return splay(v)
		if p.left == v:
			rotate(p, v)
			rotate(g, v)
			return splay(v)


def find(v, key):
	if v == None:
		return None
	if v.key == key:
		return splay(v)
	if v.key < key:
		if v.right != None:
			return find(v.right, key)
		else:
			return splay(v)
	else:
		if v.left != None:
			return find(v.left, key)
		else:
			return splay(v)


def split(root, key):
	u = find(root, key)
	u = splay(u)
	if u == None:
		return None, None

	if u.key >= key:
		root_1 = u.left
		if root_1 != None:
			root_1.parent = None
		u.left = None
		return root_1, u
	else:
		root_2 = u.right
		if root_2 != None:
			root_2.parent = None
		u.right = None
		return u, root_2


def max_in_tree(root):
	if root.right != None:
		return max_in_tree(root.right)
	else:
		return root


def merge(root_1, root_2):
	root_1 = splay(max_in_tree(root_1))
	if root_1.right == None:
		root_1.right = root_2
		root_2.parent = root_1
		return root_1
	else:
		print('Ошибка, уже есть правый сын')


def remove(u):
	u = splay(u)
	if (u.left != None) and (u.right != None):
		u.left.parent = None
		u.right.parent = None 
		return merge(u.left, u.right)
	elif (u.left == None) and (u.right != None):
		u.right.parent = None
		return u.right
	elif (u.left != None) and (u.right == None):
		u.left.parent = None
		return u.left
	return None


def sum_all(tree):
	if tree == None:
		return 0
	s = 0
	s += tree.key
	s += sum_all(tree.right)
	s += sum_all(tree.left)
	return s

