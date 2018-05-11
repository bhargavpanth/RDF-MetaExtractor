import os
import rdflib
import sys

class MetaDataExtractor(object):
	
	"""
	MetaData class returns s,p,o from the dataset
	
	"""
	
	def __init__(self, fname):
		self.fname = fname

	def parse_tags(self):
		
		if os.path.exists(os.path.join('data/', self.fname)):
			print 'parsing contents from ' + self.fname + '...'
			content = '' 
			with open(os.path.join('data/', self.fname)) as dataset:
				for contents in dataset:
					# append contents into a string

					
			graph = rdflib.Graph()
			graph.parse(data=dataset)
			output = []
			for s, p, o in graph:
				if type(o) == rdflib.term.Literal:
					output.append(o.toPython())
			print ', '.join(output)

		else:
			print 'dataset does not exist - check for filename'

def main():
	test = MetaDataExtractor('sample.rdf').parse_tags()

if __name__ == '__main__':
	main()

