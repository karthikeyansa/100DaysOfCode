def find_path(graph, start, end, path): 
	path.append(start)
	if start == end: 
		return path 
	for node in graph[start]: 
		if node not in path: 
			newpath = find_path(graph, node, end, path) 
		if newpath: 
			return newpath 
		return None

graph = { 
	'a' : ['c'], 
	'b' : ['d'], 
	'c' : ['e'], 
	'd' : ['a', 'd'], 
	'e' : ['b', 'c'] 
} 
print(find_path(graph, 'd', 'c', [])) 
