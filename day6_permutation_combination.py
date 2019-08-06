from itertools import permutations

def permutation(string, dict):
	dict[string] = []
	for itr in range(len(string)):
		value = string[:itr] + string[itr+1::]
		dict[string].append(value)
		if len(value) > 0:
			result = permutation(value, dict)
	return dict

string = '459'
dict = {}
result_permutation = permutation(string, dict)
result_permutation = result_permutation.keys()
result_permutation.sort(key=len, reverse=True)
print(result_permutation)
result_combination = list(permutations(list(string)))
print(result_combination)