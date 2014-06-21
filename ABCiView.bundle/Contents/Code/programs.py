from config import *
from item import *

class Programs():
	@classmethod
	def GetList(self):
		json = JSON.ObjectFromURL(Config.PROGRAMS_URL,
			cacheTime=Config.PROGRAM_CACHE)

		programs = []
		for p in json:
			program = Item()
			#program.path = li.xpath('./a/@href')[0]
			#program.thumb = Config.HTML_URL + li.xpath('./a/img/@src')[0]
			program.title = p
			programs.append(program)

		return programs

	@classmethod
	def GetEpisodes(self, program_name):
		json = JSON.ObjectFromURL(Config.PROGRAM_EPISODES_URL + program_name,
			cacheTime=Config.EPISODE_CACHE)

		episodes = []
		for ep in json:
			episodes.append(Item.MapFromJson(ep))

		return episodes
