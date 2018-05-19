import os
import errno
import csv
import urllib2

class Extractor(object):
	
	"""
	docstring for Extractor
	"""
	
	def __init__(self, fname):
		# asking for file name only - not the file path
		# ensure appropriate messages are set to the user 
		self.fname = fname



	def read_file(self):
		# file path exists
		url_list = []
		domain_list = []
		file_ = os.path.join('./data/source_url/', self.fname)
		if os.path.exists(file_):
			# read contents of the file
			with open(file_, 'r') as dataset:
				content = csv.reader(dataset, delimiter='\t')
				for each_line in content:
					domain = each_line[3]
					resource_url = each_line[4]
					url_list.append(resource_url)
			return url_list, domain
		else:
			print 'File does not exist'
			return False
		# read TSV/CSV file



	def download_from_url(self, url_):
		if type(url_) is list:
			# iterate over the list
			for each_url in url_:
				self.__request(each_url)

		elif type(url_) is str:
			# hit a request
			pass

		else:
			print 'invalid parameter passed as URL - type must be str'



	def __request(self, url):
		response = urllib2.urlopen(url)




	def save_to_folder(self, folder_path):
		if os.path.exists(folder_path):
			# path exists
			pass
			
		else:
			# ask if that path needs to be created
			print 'Create ' + folder_path + ' path ? [y/n]'
			ip = raw_input()
			if ip == 'y' or 'Y':
				try:
					os.makedirs(folder_path)
				except OSError as e:
					if e.errno != errno.EEXIST:
						raise
				else:
					# directory created
					print 'Directory created...'
					pass
			elif ip == 'n' or 'N':
				# resort to default path to store the content
				# exit for now
				print 'Cannot store contents to the given directory'
				break




def main():
	test = Extractor('dataset.tsv')
	test.read_file()


if __name__ == '__main__':
	main()