############## IMPORTS ##############
import os
import mutagen
from mutagen.mp3 import MP3
from mutagen.flac import FLAC

############# VARIABLES #############
red      = "\033[1;31m"
green    = "\033[1;32m"
yellow   = "\033[1;33m"
no_color = "\033[0m"
f_path   = "C:\\Users\\Christos\\Desktop\\TEST\\"

############# FUNCTIONS #############
def match_keys(dict, search):
    return [key for key, value in dict.items() if any(search in s for s in value)]

############### CODE ################
for f_name in os.listdir(f_path):
    music_file_path = f_path + f_name
    file            = mutagen.File(music_file_path)
    f_type          = type(file)
    # print(type(file))

    if f_type == mutagen.mp3.MP3:
        m_file = MP3(music_file_path)
    elif f_type == mutagen.flac.FLAC:
        m_file = FLAC(music_file_path)
    else:
        print(f"{yellow}File type {type} not supported...{no_color}")

    # print(m_file.tags.pprint())
        
    # if "COMM::eng" in m_file:
    #     print("YES")

    # try:
    #     comment = m_file["COMM::eng"]
    #     print(comment)
    #     # m_file.delete(sdf)
    #     # m_file.save()
    # except:
    #     print(f"{yellow}No ID3 tag{no_color}")

    print(type(m_file.tags))
    print([key for key, value in m_file.items()])
    # aa = match_keys(m_file, "PMEDIA")
    # print(aa)

    print(f"{green}Done{no_color}")
    
    
    # for key in m_file.tags:
    #     # print(value)
    #     print(key)
        
    print("===============")