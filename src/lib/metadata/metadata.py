import os
import rdflib
import sys

'''
Dct: title
Dct: subject
dcterms:description
Dcterms: descriptor
Dcterms: subject
dct:title
dct:description
dct:creator
dct:publisher
dct:license
dcat:keyword
dcat:theme

rdfs:comment
rdf:Description

Void: Dataset
Void: sparlqlEndpoint
Void: urilookupendpoint

Dataid:dataset properties
dataid:identifierScheme
dataid:dataDescription
dataid:similarData

void:vocabulary

dublinCore: Description
dublinCore: Identifier
dublinCore: Publisher (Required?)
dublinCore: Subject
dublinCore: Title
dublinCore: Type (gives the nature of the resource)

Skos: related
Skos: topConceptOf

'''

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

