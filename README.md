[MC] Server updater
===================

It's a small and simple script to update your vanilla Minecraft server to the latest version/snapshot !
(snapshot.py is a version with no option, to download auto the latest snapshot)

### How to use
To run, it need option :
- -r or --release if you want it to download the latest stable release
- -s or --snapshot if you want it to download the latest snapshot
- You can also add --jarpath='YourPathHere' but it's wip

### Configuration
You can configure different paths in variables :
- 'versionsFile' (line 23) is the path to the 'versions.json' local file
- 'JarPath' (line 24) is the path to where you want to put downloaded jar files

### Requirements
- [Python][] 3
- [docopt][Docopt]

[Docopt]: http://github.com/gocopt/docopt (Github: docopt: docopt)
[Python]: http://python.org/ (Python)