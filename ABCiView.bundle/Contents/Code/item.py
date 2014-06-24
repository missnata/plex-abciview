class Item(object):
	def __init__(self):
		self.id = ''
		self.path = ''
		self.thumb = ''
		self.title = ''


	@classmethod
	def MapFromJson(self, json):
		item = Item()

		if json.get('episodeHouseNumber'):
			item.id = json.get('episodeHouseNumber')

		if json.get('href'):
			item.path = json.get('href')

		if json.get('thumbnail'):
			item.thumb = json.get('thumbnail')

		if json.get('title'):
			item.title = json.get('seriesTitle') + ' ' + json.get('title')
		else:
			item.title = json.get('seriesTitle')

		# working around an issue with programs that have '.' in their title
		item.title = item.title.replace('.',':')

		return item
