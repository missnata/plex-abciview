from config import *
from collections import *
from categories import *
from channels import *
from programs import *
from item import *

VIDEO_PREFIX = '/video/abciview'

def Start():
    Plugin.AddViewGroup('List', viewMode='List', mediaType='items')
    Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')


@handler(VIDEO_PREFIX, L('Title'), art=Config.ART, thumb=Config.ICON)
def MainMenu():
    oc = ObjectContainer(view_group='InfoList')

    for collection in Collections.GetList():
        oc.add(DirectoryObject(
            key=Callback(CollectionsEpisodeMenu, id=collection.id),
            title=collection.title,
            thumb=R(collection.thumb)))

    for category in Categories.GetList():
        oc.add(DirectoryObject(
            key=Callback(CategoriesEpisodeMenu, id=category.id),
            title=category.title,
            thumb=R(category.thumb)))

    oc.add(DirectoryObject(
        key=Callback(ChannelsMenu), title=L('ChannelsTitle'), thumb=R('icon-channels.png')))
    oc.add(DirectoryObject(
        key=Callback(ProgramsMenu), title=L('ProgramsTitle'), thumb=R('icon-programs.png')))

    return oc


@route(VIDEO_PREFIX + '/channels')
def ChannelsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for channel in Channels.GetList():
        oc.add(DirectoryObject(key=Callback(ChannelEpisodeMenu, id=channel.id), title=channel.title, thumb=channel.thumb))

    return oc

@route(VIDEO_PREFIX + '/programs')
def ProgramsMenu():
    oc = ObjectContainer(view_group='InfoList')

    for program in Programs.GetList():
        oc.add(DirectoryObject(key=Callback(ProgramEpisodeMenu, program_name=program.title), title=program.title))

    return oc


@route(VIDEO_PREFIX + '/collection/{id}')
def CollectionsEpisodeMenu(id):
    return EpisodeMenu(Collections.GetEpisodes(id))

@route(VIDEO_PREFIX + '/category/{id}')
def CategoriesEpisodeMenu(id):
    return EpisodeMenu(Categories.GetEpisodes(id))

@route(VIDEO_PREFIX + '/channel/{id}')
def ChannelEpisodeMenu(id):
    return EpisodeMenu(Channels.GetEpisodes(id))

@route(VIDEO_PREFIX + '/program/{program_name}')
def ProgramEpisodeMenu(program_name):
    return EpisodeMenu(Programs.GetEpisodes(program_name))


@route(VIDEO_PREFIX + '/episode/play')
def GetVideo(path, title, thumb):
    return EpisodeObject(
        title = title,
        thumb = thumb,
        url = Config.API_URL + path
    )


def EpisodeMenu(episode_list):
    oc = ObjectContainer(view_group='InfoList')

    for ep in episode_list:
        oc.add(GetVideo(ep.path, ep.title, ep.thumb))

    return oc
