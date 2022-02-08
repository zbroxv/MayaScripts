from os import walk

groupsPath = '/groups/unfamiliar/publish/previs/assets'

directories = []

for (dirpath, dirnames, filenames) in walk(groupsPath):
    directories.extend(dirnames)
    break
    
for dir in directories:
    print(dir)
    f = []
    for (dirpath, dirnames, filenames) in walk(groupsPath + '/' + dir):
        f.extend(filenames)
        if len(f) > 0:
            print("file: " + f[0])
        break
