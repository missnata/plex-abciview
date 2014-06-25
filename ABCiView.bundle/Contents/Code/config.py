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

	EPISODE_LIST_URL = 'http://iview.abc.net.au/api/%s/%s?sort=date'

	PROGRAMS_URL = API_URL + 'search/programs'
	PROGRAM_EPISODES_URL = API_URL + 'search?keyword='
