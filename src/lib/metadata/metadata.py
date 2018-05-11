import os
import rdflib

class MetaDataExtractor(object):
	"""
	docstring for MetaData
	"""
	def __init__(self, fname):
		self.fname = fname

	def parse_tags(self):
		if os.path('../../../data/', self.fname):
			# dataset exists
			print 'parsing contents from ' + self.fname + '...'
			with open(os.path('../../../data/', self.fname)) as dataset:
				for contents in dataset:
					print contents
					# append contents into a string
					# graph = rdflib.Graph()
					# graph.parse(data=dataset)
					# output = []
					# for s, p, o in graph:
					#     if type(o) == rdflib.term.Literal:
					#         output.append(o.toPython())
					# print ', '.join(output)
		else:
			print 'dataset does not exist - check for filename'

def main():
	pass

if __name__ == '__main__':
	main()

