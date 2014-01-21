"""
Create projectors, unproject the texture and then reproject it on the model to transfer
the texture from one object to another similar, but with different UVs

"""


import os


class td_transfertChannels(object):
    def __init__(self):
        self.listCameras    = ['Front', 'Left', 'Rear', 'Right', 'Top', 'Bottom']
        self.prefixName     = 'td_Projection'


    def createProjectors(self):
        ''' Create the projectors based on the camera specified in self.listCameras '''
        for camera in self.listCameras:
            mari.actions.get('/Mari/Canvas/Camera/Camera ' + camera).trigger()
            mari.actions.get('/Mari/Canvas/Projection/Create Projector').trigger()
            projector = mari.projectors.current()
            name = 'td_Projection' + camera
            # name = mari.utils.getUniqueName('td_Projection' + camera, mari.projectors.names())
            if name in mari.projectors.names():
                mari.projectors.remove(name)

            projector.setName(name)
            projector.setSize(4096, 4096)
            projector.setUseShader('Current Shader')
            # projector.setLightingMode( projector.FULL)
            # projector.setDepthProjectionMode( projector.THROUGH)
            projector.setImportPath( mari.resources.path(mari.resources.USER) + "/transfert/" + name + "_$CHANNEL.png") 
            projector.setExportPath( mari.resources.path(mari.resources.USER) + "/transfert/" + name + "_$CHANNEL.png") 


    def unProject(self):
        ''' Save to the disk the projectors specified in self.listCameras '''
        for projectorName in self.listCameras:
            projector = mari.projectors.get(self.prefixName + projectorName)
            projector.unproject()


    def reProject(self):
        ''' Project the projectors specified in self.listCameras '''
        for projectorName in self.listCameras:
            projector = mari.projectors.get(self.prefixName + projectorName)
            projector.project()


