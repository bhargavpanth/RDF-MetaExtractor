import os
import rdflib
import sys
import xml.etree.ElementTree as ET
from io import StringIO

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
void:vocabulary

dataid:identifierScheme
dataid:dataDescription
dataid:similarData

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


	# list the namespaces in the RDF file
	def get_namespaces(self):
		namespaces = dict([node for _, node in ET.iterparse(os.path.join('data/', self.fname), events=['start-ns'])])
		return namespaces


	def get_metadata(self):
		g = rdflib.Graph()
		file = os.path.join('data/', self.fname)
		if os.path.exists(file):
			print 'parsing contents from ' + self.fname + '...'
			# RDF(S) datasets are XML files - parse tags from the list
			tree = ET.parse(file)
			root = tree.getroot()
			# list all namespaces to be checked - datasets with unconventional shorthands or names will induce warnings
			namespace_list = [{'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}, {'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#'}, {'skos' : 'http://www.w3.org/2008/05/skos#'}, {'dcat' : 'http://www.w3.org/ns/dcat#'}, {'dct' : 'http://purl.org/dc/terms/'}, {'dctype' : 'http://purl.org/dc/dcmitype/'}, {'dc'}, {'void'}, {'dataid'}, {'dbp' : 'http://dbpedia.org/ontology/'}, {'dbprop' : 'http://dbpedia.org/property/'}, {'foaf' : 'http://xmlns.com/foaf/0.1/'}]
			namespaces = {'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'}
			return root.findall('rdf:Description', namespaces)
		else:
			print 'dataset does not exist - check for filename'


def main():
	# test = MetaDataExtractor('sample.rdf').get_metadata()
	test = MetaDataExtractor('udvietnamese.rdf').get_namespaces()
	print test

if __name__ == '__main__':
	main()


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