import json

class jsonLoader:
	
	def __init__(self, path):
		filename = path
		self.jsonContent = json.loads(open(filename).read())
		