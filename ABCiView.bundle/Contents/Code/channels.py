from config import *
from item import *

class Channels():
	@classmethod
	def GetList(self):
		html = HTML.ElementFromURL(Config.HTML_URL,
			cacheTime=Config.CHANNEL_CACHE)

		channels = []
		for li in html.xpath('//div[@id="subnav"]/div/ul[1]/li'):
			channel = Item()
			channel.id = li.xpath('./a/@href')[0].split('/')[-1]
			channel.path = li.xpath('./a/@href')[0]
			channel.thumb = Config.HTML_URL + li.xpath('./a/img/@src')[0]
			channel.title = li.xpath('./a/img/@title')[0]
			channels.append(channel)

		return channels

	@classmethod
	def GetEpisodes(self, channel_id):
		json = JSON.ObjectFromURL(Config.API_URL + 'channel/' + channel_id,
			cacheTime=Config.EPISODE_CACHE)

		episodes = []
		for c in json['carousels']:
			for ep in c['episodes']:
				episodes.append(Item.MapFromJson(ep))

		return episodes
