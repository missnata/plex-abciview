from config import *
from item import *

class Collections():
	@classmethod
	def GetList(self):
		collections = []

		collection = Item()
		collection.id = 334
		collection.thumb = 'icon-new.png'
		collection.title = L('RecentTitle')
		collections.append(collection)

		collection = Item()
		collection.id = 333
		collection.thumb = 'icon-old.png'
		collection.title = L('LastChanceTitle')
		collections.append(collection)

		return collections

	@classmethod
	def GetEpisodes(self, id):
		url = Config.EPISODE_LIST_URL % ('collection', id)
		json = JSON.ObjectFromURL(url, cacheTime=Config.EPISODE_CACHE)

		episodes = []
		for ep in json['episodes']:
			episodes.append(Item.MapFromJson(ep))

		return episodes
