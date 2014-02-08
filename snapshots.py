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

# variables
AWSJsonURL = "https://s3.amazonaws.com/Minecraft.Download/versions/versions.json"
AWSJsonFileRequest = urllib.request.urlopen(AWSJsonURL)
AWSJsonFile = AWSJsonFileRequest.read()
versionsFile = os.getcwd() + "/versions.json"

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
	print ("Downloading the latest version... \n")
	AWSJarURL = "https://s3.amazonaws.com/Minecraft.Download/versions/{0}/minecraft_server.{0}.jar".format(versionId)
	jarFile = "{0}/minecraft_server.{1}.jar".format(os.getcwd(), versionId)
	with urllib.request.urlopen(AWSJarURL) as response, open(jarFile, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	print ("Version {0} download as minecraft_server.{0}.jar \n".format(versionId))

# Script
# Is versions.json here ?
if not os.path.exists(versionsFile):
	print ("No versions.json, downloading it... \n")
	# If not, then download it from AWS and write it to versions.json
	DownloadJsonFile()
	print ("Downloaded ! \n")

print ("Checking for updates... \n")
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

	# Now download the latest .jar file
	DownloadJar(latestRemoteVersion)
else:
	print ("No need to update ! Yay !")