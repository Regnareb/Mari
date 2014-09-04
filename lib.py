import mari
import logging
logger = logging.getLogger(__name__)



def createChannels(listChannels, geometry=None, imageSize=4096, imageDepth=8):
    """Create channels on a specific geometry from a list of names.
    If no geometry is specified, it will take the current geometry"""
    channelResult = []
    geometry = setGeometry(geometry)
    for channelName in listChannels:
        logger.debug('Channel Name: %s', channelName)
        channel = setChannel(channelName, geometry)
        if not channel:
            logger.info('Channel %s do not exist. Creating it.', channelName)
            channel = geometry.createChannel(channelName, imageSize, imageSize, imageDepth)
        channelResult.append(channel)
    return channelResult


def createGroupLayers(listLayers, channel=None, geometry=None):
    """Create layers in the specific channel of a geometry
    If no channel/geometry is specified, it will take the current channel on the current geometry"""
    geometry = setGeometry(geometry)
    channel = setChannel(channel, geometry)

    if geometry and channel:
        for layer in listLayers:
            channel.createGroupLayer(layer)
    else:
        logger.warning("Couldn't create a layer, no channel or geometry found.")


def setGeometry(geometry=None):
    """Return the Geometry object from a string name, or the current one if nothing is specified"""
    if not geometry:
        return mari.geo.current()
    elif isinstance(geometry, basestring):
        return mari.geo.find(geometry)
    elif isinstance(geometry, mari.GeoEntity):
        return geometry
    else:
        logger.warning("No geometry found. Return None")
        return None


def setChannel(channel=None, geometry=None):
    """Return the Channel object from a string name, or the current one if nothing is specified
    Use the current Geometry if no one is specified"""
    geometry = setGeometry(geometry)

    if not channel:
        return geometry.currentChannel()
    elif isinstance(channel, basestring):
        return geometry.findChannel(channel)
    # elif isinstance(channel, mari.Channel):
    #     return channel
    else:
        logger.warning("No channel found. Return None")
        return channel
