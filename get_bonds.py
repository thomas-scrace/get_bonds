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