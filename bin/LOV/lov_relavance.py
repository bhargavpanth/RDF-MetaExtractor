

class LinkedOpenVocabulary(object):
	
	"""
	LinkedOpenVocabulary
	* Given a vocab - returns a set of vocabs relavant by first degree seperation of LOV
	"""

	def __init__(self, vocab):
		self.vocab = vocab

		