import os
import csv

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
		url_list = []
		domain_list = []
		file_ = os.path.join('./data/source_url/', self.fname)
		if os.path.exists(file_):
			# read contents of the file
			with open(file_, 'r') as dataset:
				content = csv.reader(dataset, delimiter='\t')
				for each_line in content:
					domain = each_line[3]
					resource_url = each_line[4]
					url_list.append(resource_url)
			return url_list
		else:
			print 'File does not exist'
			return False
		# read TSV/CSV file

	def download_from_url(self):
		pass
	

def main():
	test = Extractor('dataset.tsv')
	test.read_file()


if __name__ == '__main__':
	main()