def get_bonds(hi, lo=1):
	'''Return the set of combinations of numbers from lo to hi that sum to hi.'''
	if hi < 1 or hi < lo: return set()
	if lo < 1: lo = 1
	nums = [n for n in range(hi + 1) if n not in xrange(lo)]
	cands = [[num] for num in nums]
	results = [[hi]]
	while len(max(results, key=len)) != (hi / lo):
		tmp_cands = tuple(cands)
		for num in nums:
			for cand in tmp_cands:
				if sum(cand, num) == hi:
					cands.remove(cand)
					result = cand + [num]
					result.sort()
					results.append(result)
				elif sum(cand, num) < hi and (len(cand) + 1) < (hi / lo):
					new_cand = cand[:] + [num]
					new_cand.sort()
					if new_cand not in cands: cands.append(new_cand)
	return set(tuple(result) for result in results)

def test_get_bonds():
	#regression:
	assert get_bonds(2, 0) == set([(2,), (1, 1)])
	assert get_bonds(6, 2) == set([(2, 4), (3, 3), (6, ), (2, 2, 2)])
	assert get_bonds(5, 0) == set([(1, 1, 3), (1, 4), (1, 2, 2), (5,), (2, 3), (1, 1, 1, 2), (1, 1, 1, 1, 1)])
	assert get_bonds(10, 0) == set([(2, 3, 5), (1, 1, 1, 7), (1, 1, 1, 1, 1, 1, 1, 1, 2), (2, 8), (1, 1, 1, 1, 1, 1, 1, 3), (1, 4, 5), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (1, 1, 1, 2, 2, 3), (2, 2, 2, 2, 2), (1, 1, 2, 2, 2, 2), (3, 7), (1, 1, 1, 1, 1, 1, 2, 2), (1, 1, 1, 2, 5), (1, 3, 3, 3), (1, 1, 2, 3, 3), (5, 5), (1, 1, 8), (1, 1, 1, 1, 1, 1, 4), (3, 3, 4), (1, 1, 3, 5), (2, 4, 4), (1, 1, 1, 1, 3, 3), (1, 1, 1, 1, 2, 4), (2, 2, 3, 3), (1, 2, 2, 2, 3), (1, 2, 2, 5), (1, 9), (2, 2, 2, 4), (1, 1, 1, 1, 1, 5), (4, 6), (1, 1, 1, 1, 2, 2, 2), (1, 2, 3, 4), (10,), (1, 3, 6), (1, 2, 7), (2, 2, 6), (1, 1, 1, 3, 4), (1, 1, 2, 2, 4), (1, 1, 4, 4), (1, 1, 1, 1, 6), (1, 1, 2, 6), (1, 1, 1, 1, 1, 2, 3)])
	assert get_bonds(10, 5) == set([(5, 5), (10,)])
	assert ((2,) * 10) in get_bonds(20, 2)
	#unit:
	for i in range(20):
		for j in range(20):
			for bond in get_bonds(i, j):
				assert sum(bond) == i
	print 'tests pass'

test_get_bonds()

print get_bonds(30, 1)