from config import *
from programs import *
from channels import *
from categories import *
from item import *
from episode import *

VIDEO_PREFIX = '/video/naabciview'

def Start():
    Plugin.AddViewGroup('List', viewMode='List', mediaType='items')
    Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')


@handler(VIDEO_PREFIX, L('Title'), art=Config.ART, thumb=Config.ICON)
def MainMenu():
    oc = ObjectContainer(view_group='InfoList')

    for category in Categories.GetList():
        oc.add(DirectoryObject(key=Callback(CategoriesEpisodeMenu, category_id=category.id), title=category.title))

    oc.add(DirectoryObject(key=Callback(ProgramsMenu), title='Programs'))
    oc.add(DirectoryObject(key=Callback(ChannelsMenu), title='Channels'))
    return oc


@route(VIDEO_PREFIX + '/programs')
def ProgramsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for program in Programs.GetList():
        oc.add(DirectoryObject(key=Callback(ProgramEpisodeMenu, program_name=program.title), title=program.title))

    return oc

@route(VIDEO_PREFIX + '/program/{program_name}')
def ProgramEpisodeMenu(program_name):
    rtmp_url = Video.GetRTMPUrl()

    oc = ObjectContainer(view_group='InfoList')

    for ep in Programs.GetEpisodes(program_name):
        oc.add(GetVideo(rtmp_url))

    return oc

@route(VIDEO_PREFIX + '/channels')
def ChannelsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for channel in Channels.GetList():
        oc.add(DirectoryObject(key=Callback(ChannelEpisodeMenu, channel_id=channel.id), title=channel.title, thumb=channel.thumb))

    return oc

@route(VIDEO_PREFIX + '/channel/{channel_id}')
def ChannelEpisodeMenu(channel_id):
    rtmp_url = Video.GetRTMPUrl()

    oc = ObjectContainer(view_group='InfoList')

    for ep in Channels.GetEpisodes(channel_id):
        oc.add(GetVideo(rtmp_url))

    return oc

@route(VIDEO_PREFIX + '/category/{category_id}')
def CategoriesEpisodeMenu(category_id):
    token = Config.AUTH_TOKEN()

    oc = ObjectContainer(view_group='InfoList')

    for ep in Categories.GetEpisodes(category_id):
        oc.add(GetVideo(token, ep.id, ep.path, ep.title, ep.duration, ep.thumb))

    return oc

@route(VIDEO_PREFIX + '/episode/play')
def GetVideo(token, episode_id, path, title, duration, thumb, include_container=False):
    call_args = {
        "token": token,
        "episode_id": episode_id,
        "path": path,
        "title": title,
        "duration": duration,
        "thumb": thumb,
        "include_container": True
    }

    video = VideoClipObject(
        key = Callback(GetVideo, **call_args),
        rating_key = episode_id,
        title = title,
        duration = int(duration),
        thumb = thumb,
        items = [
            MediaObject(
                parts = [
                    PartObject(
                        key = GetRTMPVideo(token, path)
                    )
                ]
            )
        ]
    )

    if include_container:
        return ObjectContainer(objects=[video])
    else:
        return video

@indirect
def GetRTMPVideo(token, path):
    html = HTML.ElementFromURL(Config.HTML_URL + path,
        cacheTime=Config.CONFIG_CACHE)

    el = html.xpath('//div[@class="video-wrapper-position"]/script/text()')[0]

    for pair in el.split(','):
        if pair.split(':"')[0] == '"mediaPath"':
            video_path = pair.split(':"')[1][:-5].replace('\\', '')
            Log('**LOG*** ' + Config.CLIP_PATH() + video_path)
            return RTMPVideoURL(
                url = Config.RTMP_URL + '?auth=' + token,
                clip = Config.CLIP_PATH() + video_path,
                swf_url = Config.SWF_URL)
