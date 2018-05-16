import urllib
import requests
import pprint
import os


class VocabularyProfiler(object):
	
	"""

	VocabularyProfiler class -
	* Query Apache Jena Fuseki for vocabularies used (namespace)
	* From the list of vocabularies obtained - apply a simple statistical model 
	to count and classify the vocabularies ( eg. given below )
	
	Given dataset A -> (find the list of vocabularies used)
			  		-> Label the vocabularies with the given class
			  		-> Apply frequency distribution on vocabularies
			  		-> Assign lower scores to higher frequency vocabulary
			  		-> Assign higher score to lower frequency/unique vocabulary
			  		-> Convert scores into confidence values
	
	---------------------
	|		Input		|
	---------------------
	| * SPARQL End point|
	| * Dataset label 	|
	---------------------
	
	-----------------------------------------
	|				Output				    |
	-----------------------------------------
	|* pairs [Vocabulary - confidence score]|
	-----------------------------------------


	Note - Dataset labels are used to build a statistical model.
	Establish statistical relationship between label/class of the dataset to the vocabulary set used.
	
	* Metadata vocabs such as DCAT/DCTERMS/VOID might be present in almost all the datasets
	* Unique datasets talking about specific concepts are the identifier

	"""

	def __init__(self, sparql_end_point, dataset_label):
		self.url = sparql_end_point
		self.label = dataset_label


	def query_sparql_for_vocab(self):
		# query to find the set of IRI / vocabs
		
		query = """
				select distinct ?ns where {
					[] ?p [] .
					bind( replace( str(?p), "(#|/)[^#/]*$", "$1" ) as ?ns )
				}
				"""
		'''
		query = """
				SELECT DISTINCT ?ns
				WHERE { 
   					?class ?label ?description.
   					BIND(REPLACE(str(?class), "(#|/)[^#/]*$", "$1") AS ?ns)
   					Filter(isURI(?class))
				}
				"""
		'''
		try:
			response = requests.post(self.url, data={'query': query})
		except Exception as e:
			raise
		else:
			res = response.json()
			return res
		


	def query_sparql_for_class(self):
		# query to get unique classes
		query = """
				prefix owl: <http://www.w3.org/2002/07/owl#>
				prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

				SELECT DISTINCT ?class ?label ?description
				WHERE {
					?class a owl:Class.
  					OPTIONAL { ?class rdfs:label ?label}
  					OPTIONAL { ?class rdfs:comment ?description}
				}
				"""
		try:
			response = requests.post(self.url, data={'query': query})
		except Exception as e:
			raise
		else:
			res = response.json()
			return res



	def persistent_vocabulary_store(self, iri):
		'''
		* Create self.label labelled file and store the vocabulary IRIs in it
		* Do not replace/update the IRI/IRI-count 
		'''
		domain = self.label
		fname = os.path.join('./res/', domain)
		with open(fname, 'a') as file:
			file.write(iri + '\n')
		# file.close()




def main():
	test = VocabularyProfiler('http://localhost:3030/ds/sparql', 'test')
	res = test.query_sparql_for_vocab()
	# print test['results']['bindings']
	result_set = res['results']['bindings']
	for each_res in result_set:
		iri = each_res['ns']['value']
		test.persistent_vocabulary_store(iri)
	# pp = pprint.PrettyPrinter()
	# pp.pprint(test)


if __name__ == '__main__':
	main()
