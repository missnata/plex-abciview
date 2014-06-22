from config import *
from item import *

class Collection():
	@classmethod
	def GetEpisodes(self, id):
		json = JSON.ObjectFromURL(Config.API_URL + 'collection/' + id,
			cacheTime=Config.EPISODE_CACHE)

		episodes = []
		for ep in json['episodes']:
			episodes.append(Item.MapFromJson(ep))

		return episodes
