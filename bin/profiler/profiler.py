import urllib
import requests


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
				SELECT DISTINCT ?subject ?predicate ?object
				WHERE { 
					?subject ?predicate ?object
				}
				"""
		response = requests.post(self.url, data={'query': query})
		return response.json()


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
		response = requests.post(self.url, data={'query': query})
		return response.json()





def main():
	test = VocabularyProfiler('http://localhost:3030/ds/sparql', 'test').query_sparql_for_vocab()
	print test


if __name__ == '__main__':
	main()
