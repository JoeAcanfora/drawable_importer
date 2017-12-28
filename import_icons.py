import shutil
import os

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def move_to_res(old_location, new_location, name, content, atSize):

    size = ''
    if atSize == '@2x.png':
        size = xhdpi
    elif atSize == '@3x.png':
        size = xxhdpi
    elif atSize == '.png':
        size = hdpi
    else:
        print "ERROR YO"

    if name.startswith('_'):
        name = name[1:]

    new_name = new_location + size + ('/' + name + content.replace(atSize, '.png')).lower().replace('-', '_').replace(' ', '_')

    print "about to move from: " + old_location
    print "to: " + new_name
    # os.rename(old_location, new_name)
    shutil.copy(old_location, new_name)


def get_icons(root, name, new_location):

    contents = listdir_nohidden(root)
    for content in contents:
        print content
        content_path = root + '/' + content

        if (os.path.isfile(content_path)):
            if content.endswith('@2x.png'):
                move_to_res(content_path, new_location, name, content, '@2x.png')
            elif content.endswith('@3x.png'):
                move_to_res(content_path, new_location, name, content, '@3x.png')
            elif content.endswith('.png'):
                move_to_res(content_path, new_location, name, content, '.png')
        elif( os.path.isdir(content_path)):
            print "going deeper to " + content_path
            get_icons(content_path, content + "_", new_location)




#script =------------
new_location = '/Users/joeacanfora/StudioProjects/OutdoorAccess-Android/app/src/main/res'
# new_location = '/Users/joeacanfora/Desktop/oa-assets'
folder_location = '/Users/joeacanfora/Desktop/oa-assets/01__icons'


hdpi = '/drawable-hdpi'
xhdpi = '/drawable-xhdpi'
xxhdpi = '/drawable-xxhdpi'

if (not os.path.exists(new_location + hdpi)) :
    os.mkdir(new_location + hdpi)
    os.mkdir(new_location + xhdpi)
    os.mkdir(new_location + xxhdpi)




get_icons(folder_location, '', new_location)
