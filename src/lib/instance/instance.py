import os
import rdflib
import sys

class InstanceExtractor(object):
	
	"""
	InstanceDataExtractor class returns objects from the dataset
	
	"""

	def __init__(self, fname):
		self.fname = fname


	def get_instances(self, num=5):
		# default number of instances are set to 5
		if os.path.exists(os.path.join('data/', self.fname)):
			print 'parsing contents from ' + self.fname + '...'
			content = ''
			graph = rdflib.Graph()
			with open(os.path.join('data/', self.fname)) as dataset:
				for contents in dataset:
					content += contents
					# append contents into a string

			graph.parse(data=content)
			output = []
			for sub, pred, obj in graph:
				if type(obj) == rdflib.term.Literal:
					print obj.encode('utf-8')
					output.append(obj.toPython())
				'''
				Subject type : rdflib.term.URIRef
				Predicate type : rdflib.term.URIRef
				Object type : rdflib.term.Literal
				'''
			return output[0:num]
		else:
			print 'dataset does not exist - check for filename'

def main():
	test = InstanceExtractor('udvietnamese.rdf').get_instances(10)
	print test

if __name__ == '__main__':
	main()