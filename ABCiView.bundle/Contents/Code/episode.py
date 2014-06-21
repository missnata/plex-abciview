from config import *
from item import *

class Episode():
	@classmethod
	def GetById(self, episode_id):
		json = JSON.ObjectFromURL(Config.API_URL + 'programs/' + episode_id,
			cacheTime=Config.CONFIG_CACHE)

		return Item.MapFromJson(json)
