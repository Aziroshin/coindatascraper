#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#=======================================================================================
# Imports
#=======================================================================================
#==========================================================
#=============================

from lib.filemanagement import File
#from lib.configutils import *
#import lib.databasedriver
#from lib.scraperconfig import Defaults, ScraperConfigSetup, ApiConfigSetup
from lib.scraperconfig import Defaults, ScraperConfigSetup
from lib.debugging import dprint

#=======================================================================================
# Configuration
#=======================================================================================

defaults = Defaults()

#=======================================================================================
# Library
#=======================================================================================

#=======================================================================================
# Actions
#=======================================================================================

if __name__ == "__main__":
	
	#database = lib.databasedriver.Database(host="localhost", port=5432,\
	#	dbName="coindata", user="postgres", password="p00p00y00")
	
	#==========================================================
	# Config
	#==========================================================
	
	#=============================
	# Scraper
	#=============================
	
	# Get config
	config = ScraperConfigSetup(section="coindatascraper").getConfig(\
		configFilePath=defaults.scraperConfigFilePath,\
		make=True)
	
	# Check scraper config
	if config.dbuser == None or config.dbpassword == None:
		print(\
			"No database user or password are configured. Please configure them in the config file"
			" located at: {path}".format(path=config.config),\
			"\nFor further instructions, please consult --help.")
		
	#=============================
	# APIs
	#=============================
	
	