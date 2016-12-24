"""
Alexis Greenstreet (October 4, 2015) University of Wisconsin-Madison

This code is designed to convert the HDF5 files of the Million Song Dataset
to a CSV by extracting various song properties.

The script writes to a "SongCSV.csv" in the directory containing this script.

Please note that in the current form, this code only extracts the following
information from the HDF5 files:
AlbumID, AlbumName, ArtistID, ArtistLatitude, ArtistLocation,
ArtistLongitude, ArtistName, Danceability, Duration, KeySignature,
KeySignatureConfidence, SongID, Tempo, TimeSignature,
TimeSignatureConfidence, Title, and Year.

This file also requires the use of "hdf5_getters.py", written by
Thierry Bertin-Mahieux (2010) at Columbia University

Credit:
This HDF5 to CSV code makes use of the following example code provided
at the Million Song Dataset website 
(Home>Tutorial/Iterate Over All Songs, 
http://labrosa.ee.columbia.edu/millionsong/pages/iterate-over-all-songs),
Which gives users the following code to get all song titles:

import os
import glob
import hdf5_getters
def get_all_titles(basedir,ext='.h5') :
    titles = []
    for root, dirs, files in os.walk(basedir):
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            h5 = hdf5_getters.open_h5_file_read(f)
            titles.append( hdf5_getters.get_title(h5) )
            h5.close()
    return titles
"""

import sys
import os
import glob
import hdf5_getters
import re
import numpy as np


check=1
class Song:
    songCount = 0
    # songDictionary = {}

    def __init__(self, songID):
        self.id = songID
        Song.songCount += 1
        # Song.songDictionary[songID] = self

        self.albumName = None
        self.albumID = None
        self.artistID = None
        self.artistLatitude = None
        self.artistLocation = None
        self.artistLongitude = None
        self.artistName = None
        self.danceability = None
        self.duration = None
        self.genreList = []
        self.keySignature = None
        self.keySignatureConfidence = None
        self.lyrics = None
        self.popularity = None
        self.tempo = None
        self.timeSignature = None
        self.timeSignatureConfidence = None
        self.title = None
        self.year = None
        self.song_hotttnesss=None
        self.artist_hotttnesss=None
        self.artist_familiarity=None
        self.timbre0=None
        self.timbre1=None
        self.timbre2=None
        self.timbre3=None
        self.timbre4=None
        self.timbre5=None
        self.timbre6=None
        self.timbre7=None
        self.timbre8=None
        self.timbre9=None
        self.timbre10=None
        self.timbre11=None

    def displaySongCount(self):
        print "Total Song Count %i" % Song.songCount

    def displaySong(self):
        print "ID: %s" % self.id   


def main():
    outputFile1 = open('B.csv', 'w')
    csvRowString = ""

    #################################################
    #if you want to prompt the user for the order of attributes in the csv,
    #leave the prompt boolean set to True
    #else, set 'prompt' to False and set the order of attributes in the 'else'
    #clause
    prompt = False
    #################################################
    if prompt == True:
        while prompt:

            prompt = False

            csvAttributeString = raw_input("\n\nIn what order would you like the colums of the CSV file?\n" +
                "Please delineate with commas. The options are: " +
                "AlbumName, timbre0, AlbumID, ArtistID, ArtistLatitude, ArtistLocation, ArtistLongitude,"+
                " ArtistName, Danceability, Duration, KeySignature, KeySignatureConfidence, Tempo," +
                " SongID, TimeSignature, TimeSignatureConfidence, Title, and Year , song_hotttnesss, artist_hotttnesss, artist_familiarity.\n\n" +
                "For example, you may write \"Title, Tempo, Duration\"...\n\n" +
                "...or exit by typing 'exit'.\n\n")

            csvAttributeList = re.split('\W+', csvAttributeString)
            
            print csvAttributeList
#            print stop

            for i, v in enumerate(csvAttributeList):
                csvAttributeList[i] = csvAttributeList[i].lower()

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"


                if attribute == 'AlbumID'.lower():
                    csvRowString += 'AlbumID'
                elif attribute == 'timbre0'.lower():
                    csvRowString += 'timbre0'    
                elif attribute == 'AlbumName'.lower():
                    csvRowString += 'AlbumName'
                elif attribute == 'ArtistID'.lower():
                    csvRowString += 'ArtistID'
                elif attribute == 'ArtistLatitude'.lower():
                    csvRowString += 'ArtistLatitude'
                elif attribute == 'ArtistLocation'.lower():
                    csvRowString += 'ArtistLocation'
                elif attribute == 'ArtistLongitude'.lower():
                    csvRowString += 'ArtistLongitude'
                elif attribute == 'ArtistName'.lower():
                    csvRowString += 'ArtistName'
                elif attribute == 'Danceability'.lower():
                    csvRowString += 'Danceability'
                elif attribute == 'Duration'.lower():
                    csvRowString += 'Duration'
                elif attribute == 'KeySignature'.lower():
                    csvRowString += 'KeySignature'
                elif attribute == 'KeySignatureConfidence'.lower():
                    csvRowString += 'KeySignatureConfidence'
                elif attribute == 'SongID'.lower():
                    csvRowString += "SongID"
                elif attribute == 'Tempo'.lower():
                    csvRowString += 'Tempo'
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += 'TimeSignature'
                elif attribute == 'TimeSignatureConfidence'.lower():
                    csvRowString += 'TimeSignatureConfidence'
                elif attribute == 'Title'.lower():
                    csvRowString += 'Title'
                elif attribute == 'Year'.lower():
                    csvRowString += 'Year'
                elif attribute == 'song_hotttnesss'.lower():
                    csvRowString += 'song_hotttnesss'
                elif attribute == 'artist_hotttnesss'.lower():
                    csvRowString += 'artist_hotttnesss'
                elif attribute == 'artist_familiarity'.lower():
                    csvRowString += 'artist_familiarity'                
                elif attribute == 'Exit'.lower():
                    sys.exit()
                else:
                    prompt = True
                    print "=============="
                    print "I believe there has been an error with the input."
                    print "=============="
                    break

                csvRowString += ","

            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString);
            csvRowString = ""
    #else, if you want to hard code the order of the csv file and not prompt
    #the user, 
    else:
        #################################################
        #change the order of the csv file here
        #Default is to list all available attributes (in alphabetical order)
        csvRowString = ("SongID,AlbumID,AlbumName,ArtistID,ArtistLatitude,ArtistLocation,"+
            "ArtistLongitude,ArtistName,Danceability,Duration,KeySignature,"+
            "KeySignatureConfidence,Tempo,TimeSignature,TimeSignatureConfidence,"+
            "Title,Year,song_hotttnesss,artist_hotttnesss,artist_familiarity,timbre0,timbre1,timbre2,timbre3,timbre4,timbre5,timbre6,timbre7,timbre8,timbre9,timbre10,timbre11")
        #################################################

        csvAttributeList = re.split('\W+', csvRowString)
        for i, v in enumerate(csvAttributeList):
            csvAttributeList[i] = csvAttributeList[i].lower()
        outputFile1.write("SongNumber,");
        outputFile1.write(csvRowString + "\n");
        csvRowString = ""  

    #################################################


    #Set the basedir here, the root directory from which the search
    #for files stored in a (hierarchical data structure) will originate
    basedir = "." # "." As the default means the current directory
    ext = ".H5" #Set the extension here. H5 is the extension for HDF5 files.
    #################################################

    #FOR LOOP
    for root, dirs, files in os.walk(basedir):        
        files = glob.glob(os.path.join(root,'*'+ext))
        for f in files:
            print f

            songH5File = hdf5_getters.open_h5_file_read(f)
#            print songH5File
#            print songH5File.root.analysis.songs.cols.end_of_fade_in[0]
            #print songH5File.root.metadata.songs.cols.artist_hotttnesss[0]
            #print songH5File.root.metadata.songs.cols.song_hotttnesss[0]

##            print songH5File.root.analysis.songs.cols.audio_md5[0]
#            print songH5File.root.analysis.songs.cols.energy[0]
##            print songH5File.root.analysis.songs.cols.mode[0]
#            print songH5File.root.analysis.songs.cols.mode_confidence[0]
#            print songH5File.root.analysis.songs.cols.start_of_fade_out[0]
##            print songH5File.root.analysis.segments_loudness_start[songH5File.root.analysis.songs.cols.idx_segments_loudness_start[0]:]
#            
#            
##            print sum(songH5File.root.metadata.songs.cols.idx_artist_terms[0:])
#            print songH5File.root.metadata.songs.cols.idx_artist_terms[0:]
#            print np.array(songH5File.root.metadata.songs.nrows)
#            
#            timbre_str="[]"
            timbre_mean=np.array(['null','null','null','null','null','null','null','null','null','null','null','null'])
            try:
#                print hdf5_getters.get_artist_terms_freq(songH5File)
                test_timbre=hdf5_getters.get_segments_timbre(songH5File)
                #print test_timbre[0]
                #print test_timbre[1]
                #print test_timbre[2]                                
                a = np.array(test_timbre)
#                np.mean(a)
#                print np.mean(a, axis=0)
                timbre_mean=np.mean(a, axis=0)
                #print timbre_str
#                break
            except: 
                pass
            #print stop
            song = Song(str(hdf5_getters.get_song_id(songH5File)))

            testDanceability = hdf5_getters.get_danceability(songH5File)
            # print type(testDanceability)
            # print ("Here is the danceability: ") + str(testDanceability)

            song.artistID = str(hdf5_getters.get_artist_id(songH5File))
            song.albumID = str(hdf5_getters.get_release_7digitalid(songH5File))
            song.albumName = str(hdf5_getters.get_release(songH5File))
            song.artistLatitude = str(hdf5_getters.get_artist_latitude(songH5File))
            song.artistLocation = str(hdf5_getters.get_artist_location(songH5File))
            song.artistLongitude = str(hdf5_getters.get_artist_longitude(songH5File))
            song.artistName = str(hdf5_getters.get_artist_name(songH5File))
            song.danceability = str(hdf5_getters.get_danceability(songH5File))
            song.duration = str(hdf5_getters.get_duration(songH5File))
            # song.setGenreList()
            song.keySignature = str(hdf5_getters.get_key(songH5File))
            song.keySignatureConfidence = str(hdf5_getters.get_key_confidence(songH5File))
            # song.lyrics = None
            # song.popularity = None
            song.tempo = str(hdf5_getters.get_tempo(songH5File))
            song.timeSignature = str(hdf5_getters.get_time_signature(songH5File))
            song.timeSignatureConfidence = str(hdf5_getters.get_time_signature_confidence(songH5File))
            song.title = str(hdf5_getters.get_title(songH5File))
            song.year = str(hdf5_getters.get_year(songH5File))
            song.song_hotttnesss=str(songH5File.root.metadata.songs.cols.song_hotttnesss[0])
            song.artist_hotttnesss=str(songH5File.root.metadata.songs.cols.artist_hotttnesss[0])

            song.artist_familiarity=str(songH5File.root.metadata.songs.cols.artist_familiarity[0])
            song.timbre0=str(timbre_mean[0])           
            song.timbre1=str(timbre_mean[1])
            song.timbre2=str(timbre_mean[2])
            song.timbre3=str(timbre_mean[3])
            song.timbre4=str(timbre_mean[4])
            song.timbre5=str(timbre_mean[5])
            song.timbre6=str(timbre_mean[6])
            song.timbre7=str(timbre_mean[7])
            song.timbre8=str(timbre_mean[8])
            song.timbre9=str(timbre_mean[9])
            song.timbre10=str(timbre_mean[10])
            song.timbre11=str(timbre_mean[11])

            
            #GET timbre
            
#            print stop
            
            #print songH5File.root.metadata.songs.cols.artist_hotttnesss[0]
            #print songH5File.root.metadata.songs.cols.song_hotttnesss[0]

            #print song count
            csvRowString += str(song.songCount) + ","

            for attribute in csvAttributeList:
                # print "Here is the attribute: " + attribute + " \n"

                if attribute == 'AlbumID'.lower():
                    csvRowString += song.albumID
                elif attribute == 'AlbumName'.lower():
                    albumName = song.albumName
                    albumName = albumName.replace(',',"")
                    csvRowString += "\"" + albumName + "\""
                elif attribute == 'ArtistID'.lower():
                    csvRowString += "\"" + song.artistID + "\""
                elif attribute == 'ArtistLatitude'.lower():
                    latitude = song.artistLatitude
                    if latitude == 'nan':
                        latitude = ''
                    csvRowString += latitude
                elif attribute == 'ArtistLocation'.lower():
                    location = song.artistLocation
                    location = location.replace(',','')
                    csvRowString += "\"" + location + "\""
                elif attribute == 'ArtistLongitude'.lower():
                    longitude = song.artistLongitude
                    if longitude == 'nan':
                        longitude = ''
                    csvRowString += longitude                
                elif attribute == 'ArtistName'.lower():
                    csvRowString += "\"" + song.artistName + "\""                
                elif attribute == 'Danceability'.lower():
                    csvRowString += song.danceability
                elif attribute == 'Duration'.lower():
                    csvRowString += song.duration
                elif attribute == 'KeySignature'.lower():
                    csvRowString += song.keySignature
                elif attribute == 'KeySignatureConfidence'.lower():
                    # print "key sig conf: " + song.timeSignatureConfidence                                 
                    csvRowString += song.keySignatureConfidence
                elif attribute == 'SongID'.lower():
                    csvRowString += "\"" + song.id + "\""
                elif attribute == 'Tempo'.lower():
                    # print "Tempo: " + song.tempo
                    csvRowString += song.tempo
                elif attribute == 'TimeSignature'.lower():
                    csvRowString += song.timeSignature
                elif attribute == 'TimeSignatureConfidence'.lower():
                    # print "time sig conf: " + song.timeSignatureConfidence                                   
                    csvRowString += song.timeSignatureConfidence
                elif attribute == 'Title'.lower():
                    csvRowString += "\"" + song.title + "\""
                elif attribute == 'Year'.lower():
                    csvRowString += song.year
                elif attribute == 'song_hotttnesss'.lower():
                    csvRowString += song.song_hotttnesss
                elif attribute == 'artist_hotttnesss'.lower():
                    csvRowString += song.artist_hotttnesss
                elif attribute == 'artist_familiarity'.lower():
                    csvRowString += song.artist_familiarity    
                elif attribute == 'timbre0'.lower():
                    csvRowString += song.timbre0  
                elif attribute == 'timbre1'.lower():
                    csvRowString += song.timbre1                    
                elif attribute == 'timbre2'.lower():
                    csvRowString += song.timbre2
                elif attribute == 'timbre3'.lower():
                    csvRowString += song.timbre3
                elif attribute == 'timbre4'.lower():
                    csvRowString += song.timbre4
                elif attribute == 'timbre5'.lower():
                    csvRowString += song.timbre5
                elif attribute == 'timbre6'.lower():
                    csvRowString += song.timbre6
                elif attribute == 'timbre7'.lower():
                    csvRowString += song.timbre7                                                                            
                elif attribute == 'timbre8'.lower():
                    csvRowString += song.timbre8                    
                elif attribute == 'timbre9'.lower():
                    csvRowString += song.timbre9
                elif attribute == 'timbre10'.lower():
                    csvRowString += song.timbre10
                elif attribute == 'timbre11'.lower():
                    csvRowString += song.timbre11                                                                        
                else:
                    csvRowString += "Erm. This didn't work. Error. :( :(\n"

                csvRowString += ","

            #Remove the final comma from each row in the csv
            lastIndex = len(csvRowString)
            csvRowString = csvRowString[0:lastIndex-1]
            csvRowString += "\n"
            outputFile1.write(csvRowString)
            csvRowString = ""

            songH5File.close()

    outputFile1.close()
	
main()
