from config import *
from item import *

class Categories():
	@classmethod
	def GetList(self):
		html = HTML.ElementFromURL(Config.HTML_URL,
			cacheTime=Config.CATEGORY_CACHE)

		categories = []
		for li in html.xpath('//ul[@id="subnav-categories"]/li/ul/li'):
			category = Item()
			category.id = li.xpath('./a/@href')[0].split('/')[-1]
			category.path = li.xpath('./a/@href')[0]
			category.thumb = 'icon-' + category.path.replace('/category/','') + '.png'
			category.title = li.xpath('./a/text()')[0]
			categories.append(category)

		return categories

	@classmethod
	def GetEpisodes(self, id):
		json = JSON.ObjectFromURL(Config.API_URL + 'category/' + id + '/all?sort=date',
			cacheTime=Config.EPISODE_CACHE)

		episodes = []
		for c in json['carousels']:
			for ep in c['episodes']:
				episodes.append(Item.MapFromJson(ep))

		return episodes
