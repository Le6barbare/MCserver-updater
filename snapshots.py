#!/usr/bin/python3

# # # # # # # # # # # # # # # # # #
#       [MC] Server update        #
# Simple Minecraft server updater #
# # # # # # # # # # # # # # # # # #

'''
This script check the versions.json file from minecraft repository and download the latest (snapshot!) minecraft_server.jar.
'''

# import
import os
import urllib.request
import json
import shutil
from datetime import datetime

# variables
AWSJsonURL = "https://s3.amazonaws.com/Minecraft.Download/versions/versions.json" # Url to the 'version.json' official file
AWSJsonFileRequest = urllib.request.urlopen(AWSJsonURL)
AWSJsonFile = AWSJsonFileRequest.read()
versionsFile = os.getcwd() + "/versions.json" # Path to the 'versions.json' local file
JarPath = os.getcwd() # Path to where you want to put downloaded jar files

# functions
def DownloadJsonFile():
	'''
	Download and create/replace the local versions.json
	'''
	with open(versionsFile, 'wb') as localFile:
		localFile.write(AWSJsonFile)

def DownloadJar(versionId):
	'''
	Download the minecraft_server.jar of the version specified in parameter
	'''
	print ("[{0}] Downloading the latest version... \n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
	AWSJarURL = "https://s3.amazonaws.com/Minecraft.Download/versions/{0}/minecraft_server.{0}.jar".format(versionId)
	jarFile = "{0}/minecraft_server.{1}.jar".format(JarPath, versionId)
	with urllib.request.urlopen(AWSJarURL) as response, open(jarFile, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	print ("[{1}] Version {0} download as minecraft_server.{0}.jar \n".format(versionId, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

# Script
if not os.path.exists(versionsFile): # Is versions.json here ?
	print ("No versions.json, downloading it... \n")
	DownloadJsonFile() # If not, then download it from AWS and write it to versions.json
	print ("Downloaded ! \n")

print ("[{0}] Checking for updates... \n".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# Compare the two versions of versions.Json
with open(versionsFile, 'r') as localFile:
	localJson = json.load(localFile)
remoteJson = json.loads(AWSJsonFile.decode("utf8"))

latestLocalVersion = localJson["versions"][0]["id"]
latestRemoteVersion = remoteJson["versions"][0]["id"]

if latestLocalVersion != latestRemoteVersion:
	print ("versions.json is outdated ! Now updating... \n")
	# Needs to update the file
	DownloadJsonFile()
	print ("versions.json updated ! \n")
	DownloadJar(latestRemoteVersion) # Now download the latest .jar file
else:
	if os.path.exists("{0}/minecraft_server.{1}.jar".format(JarPath, latestLocalVersion)): # Is latest server.jar here ?
		print ("No need to update ! Yay !")
	else:
		print("minecraft_server.{0}.jar not found.".format(latestLocalVersion))
		DownloadJar(latestLocalVersion) # Download the latest .jar file