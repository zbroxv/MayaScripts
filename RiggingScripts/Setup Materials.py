import maya.cmds as mc

substancePrefix = 'MimicLowPolyUVs_'
filePath = 'C:\Users\zachw\Downloads\Mimic\Textures'

allMats = mc.ls(materials=True)
numMats = len(allMats)

# mapTypes: string BaseColor, Metallic, Roughness
def InputMap(mapType):
    # Create texture file node network
    curTextureNode = mc.shadingNode('file', asTexture=True, isColorManaged=True)
    curPlaceNode = mc.shadingNode('place2dTexture', asUtility=True)
    mc.connectAttr(curPlaceNode+'.coverage', curTextureNode+'.coverage')
    mc.connectAttr(curPlaceNode+'.translateFrame', curTextureNode+'.translateFrame')
    mc.connectAttr(curPlaceNode+'.rotateFrame', curTextureNode+'.rotateFrame')
    mc.connectAttr(curPlaceNode+'.mirrorU', curTextureNode+'.mirrorU')
    mc.connectAttr(curPlaceNode+'.mirrorV', curTextureNode+'.mirrorV')
    mc.connectAttr(curPlaceNode+'.stagger', curTextureNode+'.stagger')
    mc.connectAttr(curPlaceNode+'.wrapU', curTextureNode+'.wrapU')
    mc.connectAttr(curPlaceNode+'.wrapV', curTextureNode+'.wrapV')
    mc.connectAttr(curPlaceNode+'.repeatUV', curTextureNode+'.repeatUV')
    mc.connectAttr(curPlaceNode+'.offset', curTextureNode+'.offset')
    mc.connectAttr(curPlaceNode+'.rotateUV', curTextureNode+'.rotateUV')
    mc.connectAttr(curPlaceNode+'.noiseUV', curTextureNode+'.noiseUV')
    mc.connectAttr(curPlaceNode+'.vertexUvOne', curTextureNode+'.vertexUvOne')
    mc.connectAttr(curPlaceNode+'.vertexUvTwo', curTextureNode+'.vertexUvTwo')
    mc.connectAttr(curPlaceNode+'.vertexUvThree', curTextureNode+'.vertexUvThree')
    mc.connectAttr(curPlaceNode+'.vertexCameraOne', curTextureNode+'.vertexCameraOne')
    mc.connectAttr(curPlaceNode+'.outUV', curTextureNode+'.uv')
    mc.connectAttr(curPlaceNode+'.outUvFilterSize', curTextureNode+'.uvFilterSize')
    # connects texture file network to material
    if mapType == 'BaseColor':
        mc.connectAttr(curTextureNode+'.outColor', matName+'.baseColor')
        mc.setAttr(curTextureNode+'.fileTextureName', filePath+'\\'+substancePrefix+matName+"_BaseColor.png", type='string')
        mc.setAttr(curTextureNode+'.colorSpace', 'sRGB', type='string')
        mc.setAttr(curTextureNode+'.alphaIsLuminance', False)
    if mapType == 'Metallic':
        mc.connectAttr(curTextureNode + '.outAlpha', matName + '.metalness')
        mc.setAttr(curTextureNode + '.fileTextureName', filePath + '\\' + substancePrefix + matName + "_Metallic.png",
                   type='string')
        mc.setAttr(curTextureNode + '.colorSpace', 'Raw', type='string')
        mc.setAttr(curTextureNode + '.alphaIsLuminance', True)
    if mapType == 'Roughness':
        mc.connectAttr(curTextureNode + '.outAlpha', matName + '.specularRoughness')
        mc.setAttr(curTextureNode + '.fileTextureName', filePath + '\\' + substancePrefix + matName + "_Roughness.png",
                   type='string')
        mc.setAttr(curTextureNode + '.colorSpace', 'Raw', type='string')
        mc.setAttr(curTextureNode + '.alphaIsLuminance', True)


for i in range(0, numMats):
    matName = allMats[i]
    if matName == 'lambert1' or matName == 'standardSurface1' or matName == 'particleCloud1':
        continue
    else:
        InputMap('BaseColor')
        InputMap('Metallic')
        InputMap('Roughness')
