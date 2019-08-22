import utils

class Tile:
	def __init__(self, value=None):
		self.value = value

class Row:
	def __init__(self):
		self.tiles = []

	def add_tile(self, tile):
		self.tiles.append(tile)

	def add_all_tiles(self, grid, row):
		for column in range(Grid.MAX_COLS):
			self.add_tile(grid.get_tile(row, column))

class Column:
	def __init__(self):
		self.tiles = []

	def add_tile(self, tile):
		self.tiles.append(tile)

	def add_all_tiles(self, grid, column):
		for row in range(Grid.MAX_ROWS):
			self.add_tile(grid.get_tile(row, column))

class Grid:
	MAX_COLS = 3
	MAX_ROWS = 3
	MAX_TILES = MAX_COLS * MAX_ROWS
	def __init__(self):
		self.tiles = []
		for row in range(MAX_ROWS):
			r = []
			for col in range(MAX_COLS):
				r.append(Tile())
			self.tiles.append(r)

	def init_with_string_config(self, config_str):
		# split it via \n
		rows_str = config_str.split('\n')
		for row in len(rows_str):
			row_str = rows_str[row]
			for col in range(MAX_COLS):
				# get the char at that position
				val = row_str[col]
				if val.isdigit():
					value = int(val)
					tile = self.get_tile(col, row)
					tile.value = value


	# TODO: create an iterator for all_tiles
	def all_tiles(self):
		tiles = []
		for row in range(MAX_ROWS):
			for col in range(MAX_COLS):
				tiles.append(self.get_tiles(col, row))
		return tiles

	def get_tile(self, col, row):
		assert(col >= 0 and col < MAX_COLS and row >= 0 and row < MAX_ROWS)
		return self.tiles[row][col]

	def is_complete(self):
		tiles = self.get_tiles()
		return utils.is_complete(tiles)

	def is_in_error(self):
		tiles = self.get_tiles()
		return utils.is_in_error(tiles)