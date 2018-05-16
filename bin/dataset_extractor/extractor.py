import os


class Extractor(object):
	
	"""
	docstring for Extractor
	"""
	
	def __init__(self, fname):
		# asking for file name only - not the file path
		# ensure appropriate messages are set to the user 
		self.fname = fname

	def read_file(self):
		# file path exists
		if os.path.exists(os.path('./data/source_url', self.fname)):
			# read contents of the file
			pass
		# read TSV/CSV file
		