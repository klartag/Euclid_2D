import itertools
import numpy as np
import collections
from collections import Counter
from os.path import dirname, abspath
from pathlib import Path
from typing import Generic, TypeVar
BASE_PATH = Path(dirname(abspath(__file__)))

K = TypeVar('K')
V = TypeVar('V')

class Bijection(Generic[K, V]):
	"""
	A dictionary for a one-to-one mapping, allowing finding the inverse of every value.
	"""
	forward: dict[K, V]
	back: dict[V, K]

	def __init__(self, forward: dict[K, V] | None = None, back: dict[V, K] | None = None):
		self.forward = forward or {}
		self.back = back or {}
	
	def rev(self) -> 'Bijection[V, K]':
		"""
		Returns the reverse bijection, mapping values to keys.
		"""
		return Bijection(self.back, self.forward)

	def backward(self, v: V) -> K:
		return self.back[v]
	
	def contains_value(self, v: V) -> bool:
		"""
		Checks if the given value is in the image of the bijection.
		"""
		return v in self.back

	def __getitem__(self, k: K):
		return self.forward[k]
	
	def __setitem__(self, k: K, v: V):
		assert v not in self.back, f'Attempted to use the target value {v} twice, for the keys {self.back[v]} and {k}.'
		if k in self.forward:
			del self.back[self.forward[k]]
		self.forward[k] = v
		self.back[v] = k

	def __delitem__(self, k: K):
		v = self.forward[k]
		del self.forward[k]
		del self.back[v]

	def __contains__(self, key: K) -> bool:
		return key in self.forward
	
	def __len__(self) -> int:
		return len(self.forward)
	
	def __repr__(self) -> str:
		return repr(self.forward)

	def __str__(self) -> str:
		return str(self.forward)
	
	def clone(self) -> 'Bijection[K, V]':
		return Bijection(dict(self.forward), dict(self.back))
	

	


# v is a list of dictionaries
# we check if they are consistent, and if they are, we return their union
# if there is a tuple in the union, we also check that its elements are assigned values
def dict_union(v: list[dict[K, V] | None]) -> dict[K, V] | None:
	"""
	Merges a list of dictionaries into a single dictionary if they match, and returns None if they don't.
	"""
	if any(x is None for x in v):
		return None
	
	res = {}
	for d in v:
		if d is None:
			return None

		for key, value in d.items():
			if key in res and res[key] != value:
				return None
			else:
				res[key] = value
	return None if dict_bad(res) else res

def dict_union_simple(*v: dict[K, V] | None) -> dict[K, V] | None:
	"""
	Merges a list of dictionaries into a single dictionary if they match, and returns None if they don't.
	"""
	if any(x is None for x in v):
		return None
	
	res = {}
	for d in v:
		if d is None:
			return None

		for key, value in d.items():
			if key in res and res[key] != value:
				return None
			else:
				res[key] = value
	return res

# gets two lists of dicts, goes over the cross-product
# and returns a list of the unions of all consistent pairs
def dicts_cross_product(v: list[dict[K, V]], w: list[dict[K, V]]) -> list[dict[K, V]]:
	res = []
	for x in v:
		for y in w:
			d = dict_union([x,y])
			if d is not None:
				res.append(d)
	return res

# gets a list of dictionaries, and one more key and value
# tries to add it to all of them
def dicts_add_key_value(v, key, value):
	if isinstance(key, int) and (not isinstance(value, int) or key != value): 
		v.clear()
		return
	res = []
	to_add = {key: value}
	for dic in v:
		dic_updated = dict_union([dic, to_add])
		if dic_updated is not None:
			res.append(dic_updated)
	v.clear()
	v.extend(res)

# gets two sets. If the style is "onto", returns all onto dictionaries source to target
# If the style is "one-to-one", returns all one-to-one dictionaries source to target
def get_dicts_sets(source, target, style="onto"):
	dics = []
	if style == "onto":
		target = list(target)
		if len(source) < len(target):
			return []
		for combo in itertools.combinations(source, len(target)):
			for perm in itertools.permutations(combo):
				mapping = {}
				for i in range(len(target)):
					mapping[perm[i]] = target[i]
				if not dict_bad(mapping):
					dics.append(mapping)
	elif style == "one-to-one":
		source = list(source)
		if len(source) > len(target):
			return []
		for combo in itertools.combinations(target, len(source)):
			for perm in itertools.permutations(combo):
				mapping = {}
				for i in range(len(source)):
					mapping[source[i]] = perm[i]
				if not dict_bad(mapping):
					dics.append(mapping)
	return dics

# checks if a dictionary contains a tuple, and a member of the tuple too
# remember: we only apply dicts to rules (their assumptions and conclusions)
def dict_bad(my_dict):
	if my_dict is None:
		return True
	for key in my_dict.keys():
		if isinstance(key, tuple): 
			for element in key:
				if element in my_dict: 
					return True	
		elif isinstance(key, int): 
			if (not isinstance(my_dict[key], int)) or my_dict[key] != key:
				return True
	return False

# append_dict_list(res,a1,b1,a2,b2) creates a dictionary 
# from a1 to b1, adds from a2 to b2 etc., unless there are contradictions
def append_dict_lists(res, *list_pairs):
	if any(len(a) != len(b) for a, b in zip(list_pairs[::2], list_pairs[1::2])):
		return
	dic = {}
	for a, b in zip(list_pairs[::2], list_pairs[1::2]):
		for key, value in zip(a, b):
			if key in dic and dic[key] != value:
				return
			if isinstance(key, int) and (not isinstance(value, int) or key != value): 
				return
			if isinstance(key, tuple) and len(key) == 1:
				key = key[0]
			if isinstance(value, tuple) and len(value) == 1:
				value = key[0]
			dic[key] = value
	if not dict_bad(dic):
		res.append(dic)

# maps a tuple to a letter, a letter to a tuple
# but tuple to tuple -- goes down to points
def append_dict_lists_v3(res, *list_pairs):
	dic = {}
	for a, b in zip(list_pairs[::2], list_pairs[1::2]):
		if len(a) > 1 and len(b) > 1:
			if len(a) != len(b):
				return
			for key, value in zip(a, b):
				if key in dic:
					if dic[key] != value:
						return
					if isinstance(key, int) and (not isinstance(value, int) or key != value): 
						return
				else:
					key1 = key[0] if (isinstance(key, tuple) and len(key) == 1) else key
					value1 = value[0] if (isinstance(value, tuple) and len(value) == 1) else value
					dic[key1] = value1
		else:
			if a in dic:
				if dic[a] != b:
					return
				if isinstance(a, int) and (not isinstance(b, int) or a != b): 
					return
			else:
				key1 = a[0] if (isinstance(a, tuple) and len(a) == 1) else a
				value1 = b[0] if (isinstance(b, tuple) and len(b) == 1) else b
				dic[key1] = value1
	if not dict_bad(dic):
		res.append(dic)

# a variant for the previous function, used from angle or length
def append_dict_lists_v2(res, list1, list2):
	dic = {}
	for idx in range(2):
		for a, b in zip(list1[idx], list2[idx]):
			if isinstance(a,(str,int)) or isinstance(b,(str,int)):
				key = a 
				value = b 
				if key in dic and dic[key] != value:
					return
				if isinstance(key, int) and (not isinstance(value, int) or key != value): 
					return
				key1 = key[0] if (isinstance(key, tuple) and len(key) == 1) else key
				value1 = value[0] if (isinstance(value, tuple) and len(value) == 1) else value
				dic[key1] = value1
			else:
				for key, value in zip(a, b):
					if key in dic and dic[key] != value:
						return
					if isinstance(key, int) and (not isinstance(value, int) or key != value): 
						return
					key1 = key[0] if (isinstance(key, tuple) and len(key) == 1) else key
					value1 = value[0] if (isinstance(value, tuple) and len(value) == 1) else value
					dic[key1] = value1
	if not dict_bad(dic):
		res.append(dic)

# gets two lists of strings, checks if one is a permutation of the other.
# If it is, we return a list of all such permutations
def is_perm(v, w):
	if len(v) != len(w) or sorted(v) != sorted(w):
		return None
	res = []
	perms = itertools.permutations(list(range(len(v))))
	for sigma in perms:
		if [v[i] for i in sigma] == w:
			res.append(sigma)
	return res

# checks if lists 1 embeds monotone-increasingly in list2 
def is_increasing_embedding(list1, list2):
	i, j = 0, 0
	while i < len(list1) and j < len(list2):
		if list1[i] == list2[j]:
			i += 1
		j += 1
	return i == len(list1)

# checks if lists 1 embeds monotonically -- either increasing or decreasing -- in list2 
def is_monotonic_embedding(list1, list2):
	if is_increasing_embedding(list1,list2):
		return True
	if is_increasing_embedding(list1,list(reversed(list2))):
		return True
	return False

# checks if lists 1 embeds cyclically, orientation preserving, in list2 
def is_cyclic_oriented_embedding(list1, list2):
	for i in range(len(list2)):
		rotated_list2 = list2[i:] + list2[:i]
		if is_increasing_embedding(list1, rotated_list2):
			return True
	return False

# checks if lists 1 embeds cyclically, in both orientations, in list2 
def is_cyclic_embedding(list1, list2):
	if is_cyclic_oriented_embedding(list1,list2):
		return True
	if is_cyclic_oriented_embedding(list1,list(reversed(list2))):
		return True
	return False

def softmax(x):
	e_x = np.exp(x - np.max(x))
	return e_x / e_x.sum(axis=0)

# method for removing adjacent duplicates from a list
def remove_duplicates(v):
	i = 0
	while (i < len(v)-1):
		if v[i] == v[i+1]:
			del v[i+1]
			i -= 1
		i += 1

# method for removing cylically-adjacent duplicates from a list
def remove_duplicates_cyclic(v):
	if len(v) <= 2:
		return
	if v[0] == v[-1]:
		del v[-1]
		remove_duplicates_cyclic(v)
	else:
		remove_duplicates(v)

# gets two pairs of lists representing an equation u[0][0] + u[0][1] + ... = u[1][0] + u[1][1] + ...
# some of the u[i][j] are variables, some are integer numbers
# checks if u follows from v
def equation_follows(u, v):
	# quick preliminary check
	if (u == v):
		return True
	
	# gets the ints 
	ints_lhs_u = sum(x for x in u[0] if isinstance(x, int))
	ints_lhs_v = sum(x for x in v[0] if isinstance(x, int))
	ints_rhs_u = sum(x for x in u[1] if isinstance(x, int))
	ints_rhs_v = sum(x for x in v[1] if isinstance(x, int))
	diff_u = ints_rhs_u - ints_lhs_u
	diff_v = ints_rhs_v - ints_lhs_v
	if abs(diff_u) != abs(diff_v):
		return False

	# get the non-ints 
	lhs_u = Counter(x for x in u[0] if not isinstance(x, int)) 
	rhs_u = Counter(x for x in u[1] if not isinstance(x, int))  
	rhs_v = Counter(x for x in v[1] if not isinstance(x, int))  
	lhs_v = Counter(x for x in v[0] if not isinstance(x, int))  

	# move everything to RHS/LHS for u, so that numerical value would be non-negative  
	if diff_u == 0:
		try1_u = rhs_u.copy()
		try2_u = lhs_u 
		try1_u.subtract(lhs_u)
		try2_u.subtract(rhs_u)
		final1_u = {k: v for k, v in try1_u.items() if v != 0}
		final2_u = {k: v for k, v in try2_u.items() if v != 0}
		total_v = rhs_v
		total_v.subtract(lhs_v)
	elif (diff_u > 0):
		total_u = rhs_u 
		total_u.subtract(lhs_u)
		total_u[diff_u] = 1
		final_u = {k: v for k, v in total_u.items() if v != 0}
	else:
		total_u = lhs_u
		total_u.subtract(rhs_u)
		total_u[-diff_u] = 1
		final_u = {k: v for k, v in total_u.items() if v != 0}	 

	if (diff_v > 0):
		total_v = rhs_v
		total_v.subtract(lhs_v)
		total_v[diff_v] = 1
	elif (diff_v < 0):
		total_v = lhs_v
		total_v.subtract(rhs_v)
		total_v[-diff_v] = 1
	final_v = {k: v for k, v in total_v.items() if v != 0}

	if diff_u == 0:
		return final_v == final1_u or final_v == final2_u
	else:
		return final_v == final_u