import os
import rdflib
import sys

class MetaDataExtractor(object):
	
	"""
	MetaData class returns s,p,o from the dataset
	
	"""
	
	def __init__(self, fname):
		self.fname = fname

	def get_metadata_tags(self):
		if os.path.exists(os.path.join('data/', self.fname)):
			print 'parsing contents from ' + self.fname + '...'
			
		else:
			print 'dataset does not exist - check for filename'

def main():
	test = MetaDataExtractor('sample.rdf').get_instances()

if __name__ == '__main__':
	main()

