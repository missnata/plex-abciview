from config import *
from collection import *
from programs import *
from channels import *
from categories import *
from item import *

VIDEO_PREFIX = '/video/abciview'

def Start():
    Plugin.AddViewGroup('List', viewMode='List', mediaType='items')
    Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')


@handler(VIDEO_PREFIX, L('Title'), art=Config.ART, thumb=Config.ICON)
def MainMenu():
    oc = ObjectContainer(view_group='InfoList')

    oc.add(DirectoryObject(
        key=Callback(CollectionsMenu, id=334), title=L('RecentTitle'), thumb=R('icon-new.png')))
    oc.add(DirectoryObject(
        key=Callback(CollectionsMenu, id=333), title=L('LastChanceTitle'), thumb=R('icon-old.png')))

    for category in Categories.GetList():
        oc.add(DirectoryObject(
            key=Callback(CategoriesEpisodeMenu, category_id=category.id),
            title=category.title,
            thumb=R(category.thumb)))

    oc.add(DirectoryObject(
        key=Callback(ProgramsMenu), title=L('ProgramsTitle'), thumb=R('icon-programs.png')))
    oc.add(DirectoryObject(
        key=Callback(ChannelsMenu), title=L('ChannelsTitle'), thumb=R('icon-channels.png')))
    return oc


@route(VIDEO_PREFIX + '/collection/{id}')
def CollectionsMenu(id):
    oc = ObjectContainer(view_group='InfoList')

    for ep in Collection.GetEpisodes(id):
        oc.add(GetVideo(ep.path, ep.title, ep.duration, ep.thumb))

    return oc

@route(VIDEO_PREFIX + '/programs')
def ProgramsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for program in Programs.GetList():
        oc.add(DirectoryObject(key=Callback(ProgramEpisodeMenu, program_name=program.title), title=program.title))

    return oc

@route(VIDEO_PREFIX + '/program/{program_name}')
def ProgramEpisodeMenu(program_name):
    oc = ObjectContainer(view_group='InfoList')

    for ep in Programs.GetEpisodes(program_name):
        oc.add(GetVideo(ep.path, ep.title, ep.duration, ep.thumb))

    return oc

@route(VIDEO_PREFIX + '/channels')
def ChannelsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for channel in Channels.GetList():
        oc.add(DirectoryObject(key=Callback(ChannelEpisodeMenu, channel_id=channel.id), title=channel.title, thumb=channel.thumb))

    return oc

@route(VIDEO_PREFIX + '/channel/{channel_id}')
def ChannelEpisodeMenu(channel_id):
    oc = ObjectContainer(view_group='InfoList')

    for ep in Channels.GetEpisodes(channel_id):
        oc.add(GetVideo(ep.path, ep.title, ep.duration, ep.thumb))

    return oc

@route(VIDEO_PREFIX + '/category/{category_id}')
def CategoriesEpisodeMenu(category_id):
    oc = ObjectContainer(view_group='InfoList')

    for ep in Categories.GetEpisodes(category_id):
        oc.add(GetVideo(ep.path, ep.title, ep.duration, ep.thumb))

    return oc

@route(VIDEO_PREFIX + '/episode/play')
def GetVideo(path, title, duration, thumb):
    return EpisodeObject(
        title = title,
        duration = int(duration),
        thumb = thumb,
        url = Config.API_URL + path
    )
