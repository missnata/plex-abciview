class Item(object):
	def __init__(self):
		self.id = ''
		self.duration = 0
		self.path = ''
		self.publish_date = Datetime.ParseDate('1901-01-01 12:00:00')
		self.summary = ''
		self.thumb = ''
		self.title = ''


	@classmethod
	def MapFromJson(self, json):
		item = Item()

		if json.get('episodeHouseNumber'):
			item.id = json.get('episodeHouseNumber')

		if json.get('duration'):
			item.duration = int(json.get('duration')) * 1000

		if json.get('href'):
			item.path = json.get('href')

		if json.get('pubDate'):
			item.publish_date = Datetime.ParseDate(json.get('pubDate'))

		if json.get('description'):
			item.summary = json.get('description')

		if json.get('thumbnail'):
			item.thumb = json.get('thumbnail')

		if json.get('title'):
			item.title = json.get('seriesTitle') + ' ' + json.get('title')
		else:
			item.title = json.get('seriesTitle')

		return item
