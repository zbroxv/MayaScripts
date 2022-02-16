import os
import shutil

groupsPath = '/users/animation/zmw42/Desktop/testAssets'

directories = next(os.walk(groupsPath), (None, None, []))[1]

#rename directories with the previs_previs_ mistake
for dir in directories:
    if dir.find('previs_previs_') > -1:
        newDir = dir[7:]
        #if new directory already exists, delete the old one
        if os.path.isdir(groupsPath + '/' + newDir):
            shutil.rmtree(groupsPath + '/' + dir)
        #other wise just rename the old directory
        else:
            os.rename(groupsPath + '/' + dir, groupsPath + '/' + newDir)

#rename files with the previs_previs_ mistake and the _mesh mistake
for dir in directories:
    files = next(os.walk(groupsPath + '/' + dir), (None, None, []))[2]
    if len(files) > 0:
        newFile = files[0]
        if newFile.find('previs_previs_') > -1:
            newFile = newFile[7:]
        index = newFile.find('_mesh')
        if index > -1:
            newFile = newFile[:index] + '.usd'
            print(newFile)
        if newFile != files[0]:
            os.rename(groupsPath + '/' + dir + '/' + files[0], groupsPath + '/' + dir + '/' + newFile)

            
            
            
            
            
            
            
            
            
           
import os
import shutil

filePath = '/users/animation/zmw42/Desktop/allAssets.txt'
groupsPath = '/users/animation/zmw42/Desktop/testAssets'

f = open(filePath, "w")
assetString = "#usda 1.0\n\n\n"

directories = next(walk(groupsPath), (None, None, []))[1]
for dir in directories:
    files = next(walk(groupsPath + '/' + dir), (None, None, []))[2]
    if len(files) > 0:
        assetPath = groupsPath + '/' + dir + '/' + files[0]
        usdRef = "def \"" + dir + "\" (\n    prepend references = @" + assetPath + "@\n)\n{\n}\n\n"
        assetString = assetString + usdRef
        
f.write(assetString)
print(assetString)
f.close












import os
import shutil

publishPath = '/groups/unfamiliar/publish/layout/clusters'
groupsPath = '/groups/unfamiliar/publish/previs/assets'
listPath = '/users/animation/zmw42/Desktop/assetLists'

clusterlists = [[], [], []]

assetLists = next(os.walk(listPath), (None, None, []))[2]
for i in range(len(assetLists)):
    clusterlists[0].append(assetLists[i].strip('.txt'))
    clusterlists[2].append("#usda 1.0\n\n\n")
    f = open(listPath + '/' + assetLists[i], 'r')
    items = f.readlines()
    for x in range(len(items)):
        items[x] = items[x].strip('\n')
    clusterlists[1].append(items)
    f.close()
    
assetString = "#usda 1.0\n\n\n"

directories = next(os.walk(groupsPath), (None, None, []))[1]
for dir in directories:
    files = next(os.walk(groupsPath + '/' + dir), (None, None, []))[2]
    if len(files) > 0:
        filename = files[0]
        i = 0
        foundCluster = False
        for clusterName in clusterlists[i]:
            for object in clusterlists[1][i]:
                object = 'previs_' + object + '.usd'
                if filename == object:
                    foundCluster = True
                    assetPath = groupsPath + '/' + dir + '/' + filename
                    usdRef = "def \"" + dir + "\" (\n    prepend references = @" + assetPath + "@\n)\n{\n}\n\n"
                    clusterlists[2][i] = clusterlists[2][i] + usdRef
                    break
            if foundCluster == True:
                break
            i += 1
        
print(clusterlists[0])
print(clusterlists[1])
print(clusterlists[2])

for x in range(len(clusterlists[0])):
    print(clusterlists[0][x])
    f = open(publishPath + '/' + clusterlists[0][x] + '.usda', "w")
    f.write(clusterlists[2][x])
    f.close
    
f = open(listPath + '/' + 'test.txt', "w")
f.write("bs")
f.close














import maya.cmds as mc
import os

groupsPath = '/groups/unfamiliar/publish/previs/assets'

directories = next(os.walk(groupsPath), (None, None, []))[1]
for dir in directories:
    files = next(os.walk(groupsPath + '/' + dir), (None, None, []))[2]
    if len(files) > 0:
        filename = files[0]
        print(filename)
        cmds.file(groupsPath + '/' + dir + '/' + filename, i = True)
        
import maya.cmds as mc
meshes = mc.ls(sl = True)
for mesh in meshes:
    mc.select(mesh)
    name = mesh
    if name.find('previs_previs_') > -1:
        name = name[7:]
    index = name.find('_mesh')
    if index > -1:
        name = name[:index]
    shader = mc.shadingNode('usdPreviewSurface', asShader = True, n = name + '_mat')
    mc.sets(renderable = True, noSurfaceShader = True, n = name + '_mat' + 'SG', empty = True)
    mc.connectAttr(name + '_mat' + '.outColor', name  + '_mat' + 'SG' + '.surfaceShader')
    mc.select(mesh)
    mc.hyperShade(a = shader)

import maya.cmds as mc
import os
meshes = mc.ls(sl = True)
for mesh in meshes:
    mc.select(mesh)
    name = mesh
    if name.find('previs_previs_') > -1:
        name = name[7:]
    index = name.find('_mesh')
    if index > -1:
        name = name[:index]
    filename = groupsPath + '/' + name + '/' + name + '.usd'
    mc.rename(mesh, name + '_mesh')
    os.remove(filename)
    cmds.mayaUSDExport(
                file = filename,
                selection=True,
                defaultUSDFormat='usda',
                defaultMeshScheme='none',
                convertMaterialsTo='UsdPreviewSurface'
            )
