class Config():
	## artwork in Contents/Resources folder
	ART  = 'art-default.jpg'
	ICON = 'icon-default.jpg'

	CONFIG_CACHE = 86400000
	CATEGORY_CACHE = 86400000
	CHANNEL_CACHE = 86400000
	PROGRAM_CACHE = 300000
	EPISODE_CACHE = 300000

	HTML_URL = 'http://iview.abc.net.au/'
	API_URL = 'http://iview.abc.net.au/api/'

	IVIEW_NS = {'a': 'http://www.abc.net.au/iView/Services/iViewHandshaker'}

	CONFIG_URL = 'http://www.abc.net.au/iview/xml/config.xml'
	CONFIG_XML = XML.ElementFromURL(CONFIG_URL, cacheTime=CONFIG_CACHE)

	AUTH_URL = CONFIG_XML.xpath('/config/param[@name="auth"]/@value')[0]
	AUTH_XML = XML.ElementFromURL(AUTH_URL)

	RTMP_URL = CONFIG_XML.xpath('/config/param[@name="server_streaming"]/@value')[0]

	SWF_URL = 'http://www.abc.net.au/iview/images/iview.jpg'

	PROGRAMS_URL = API_URL + 'search/programs'
	PROGRAM_EPISODES_URL = API_URL + 'search?keyword='

	@classmethod
	def CLIP_PATH(self):
		path = self.AUTH_XML.xpath('//a:path/text()', namespaces=self.IVIEW_NS)[0]
		return 'mp4:flash/' + path

	@classmethod
	def AUTH_TOKEN(self):
		xml = XML.ElementFromURL(self.AUTH_URL)
		token = xml.xpath('//a:token/text()', namespaces=self.IVIEW_NS)[0]
		return token
