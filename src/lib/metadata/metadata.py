import os
import rdflib
import sys
import xml.etree.ElementTree as ET

'''
-----------------------------------------
| Search dataset for the following tags |
-----------------------------------------

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

	def get_metadata(self):
		g = rdflib.Graph()
		file = os.path.join('data/', self.fname)
		if os.path.exists(file):
			print 'parsing contents from ' + self.fname + '...'
			'''
			RDF(S) datasets are XML files - parse tags from the list
			'''
			tree = ET.parse(file)
			root = tree.getroot()
			namespaces = {'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
			print root.findall('rdf:Description', namespaces)
			# print root.findall('rdf:Description')
			return root

			'''
			# querying the RDF dataset
			g.parse(file)
			qres = g.query(
				"""SELECT DISTINCT ?aname ?bname
				WHERE {
				?a foaf:knows ?b .
				?a foaf:name ?aname .
				?b foaf:name ?bname .
			}""")
		
			for row in qres:
			    print("%s knows %s" % row)
			'''
		else:
			print 'dataset does not exist - check for filename'

def main():
	test = MetaDataExtractor('sample.rdf').get_metadata()
	print test

if __name__ == '__main__':
	main()

