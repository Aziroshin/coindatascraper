import os
import configargparse
import argparse
import configparser
from lib.configutils import ConfigSetup, ConfigFile

class Defaults(object):
	def __init__(self):
		self.scraperConfigDirPath = os.path.normpath(os.path.join(\
			os.path.expanduser("~"), ".config", "coindatascraper"))
		self.scraperConfigFilePath = os.path.normpath(\
			os.path.join(self.scraperConfigDirPath, "coindatascraper.conf"))
		self.apiConfigDirPath = os.path.normpath(os.path.join(self.scraperConfigDirPath, "apis"))
		self.dbHost = "localhost"
		self.dbPort = "5432"
		self.dbName = ""
	
class ScraperConfigSetup(ConfigSetup):
	def setUp(self):
		defaults=Defaults()
		self.parser.add("--api-config-dir", default=defaults.apiConfigDirPath,\
			help="Directory containing the config files for the APIs to scrape from.")
		self.parser.add("--dbhost", default=defaults.dbHost,\
			help="Host address for the database server.")
		self.parser.add("--dbport", default=defaults.dbPort,\
			help="Port for the database server.")
		self.parser.add("--dbname", default=defaults.dbName,\
			help="Database name.")
		self.parser.add("--dbuser",\
			help="Login user name for the database.")
		self.parser.add("--dbpassword",\
			help="Login password for the database. DO NOT use the command line argument if at all"
				" possible, but put it in a config file instead.")

class ApiConfigFile(ConfigFile):
	def setUp(self):
		self.config["connection"]["address"] = ""
		self.config["connection"]["port"] = ""
		self.config["authentication"]["secret"] = ""