from urllib import request

class VocabularyProfiler(object):
	"""

	VocabularyProfiler class -
	* Query Apache Jena Fuseki for vocabularies used (namespace)
	* From the list of vocabularies obtained - apply a simple statistical model to count and classify the vocabularies ( eg. given below )
	
	Given dataset A -> (find the list of vocabularies used)
			  		-> Label the vocabularies with the given class
			  		-> Apply frequency distribution on vocabularies
			  		-> Assign lower scores to higher frequency vocabulary
			  		-> Assign higher score to lower frequency/unique vocabulary
			  		-> Convert scores into confidence values
	Input
	--------
	* URL
	* Query
	* Dataset Label

	Note - Dataset labels are used to build a statistical model. Establish statistical relationship between label/class of the dataset to the vocabulary set used

	* Metadata vocabs such as DCAT/DCTERMS/VOID might be present in almost all the datasets
	* Unique datasets talking about specific concepts are the identifier

	"""
	def __init__(self, arg):
		self.arg = arg

	
		