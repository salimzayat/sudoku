class Board:
	MAX_ROWS = 9
	MAX_COLS = 9
	MAX_GRIDS = 9
	ROWS_PER_GRID = 3
	COLS_PER_GRID = 3
	GRIDS_PER_GRID_ROW = 3
	GRIDS_PER_GRID_COL = 3

	def __init__(self, initial_state_str):
		# TODO: parse the initial string
		self.grids = []
		for i in range(MAX_GRIDS):
			self.grids.append(Grid())
		# great, now parse the initial state_str into grid sections
		grid_rows_split = initial_state_str.split('\n')
		grid_rows = []
		# prune out any invalid rows
		for grid_row in grid_rows_split:
			if len(grid_row) != COLS_PER_GRID * GRIDS_PER_GRID_ROW:
				continue
			grid_rows.append(grid_row)

		

		

	def get_column(self, idx):
		if (idx >= 0 and idx < MAX_COLS):
			# create a new Column
			column = Column()
			for i in 