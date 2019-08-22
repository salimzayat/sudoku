def is_complete(tiles):
	possible values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert(len(tiles) == len(possible_values))
	for tile in tiles:
		val = tile.value
		if val == None:
			return False
		
		if val in possible_values:
			possible_values.remove(val)
		else:
			return False
	return (len(possible_values) == 0)

def is_in_error(tiles):
	possible values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	assert(len(tiles) == len(possible_values))
	for tile in tiles:
		val = tile.value
		if val == None:
			return False
		
		if val in possible_values:
			possible_values.remove(val)
		else:
			return True
	return (len(possible_values) != 0)