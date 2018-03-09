import configargparse
import copy
from lib.filemanagement import File, Dir
from lib.debugging import dprint

class ConfigFile(File):
	
	def __init__(self, path, make=False):
		super().__init__(path, make)
		self.config = configparser.ConfigParser()
		self.setUp()
		if not self.exists and make:
			self.make()
	
	def setUp(self):
		"""Method to override with config file setup."""
		pass
	
	def addOption(self, category, name, default):
		"""Add a configuration option to the config."""
		self.config[category][name] = default
	
	def write(self):
		"""Write the configuration to the file."""
		with open(self.path) as configFile:
			self.config.write(configFile)
	
	def read(self):
		"""Read configuration from the file."""
		self.config.read(self.path)
	
	def make(self):
		"""Create the configuration file."""
		self.write()

class ConfigDir(Dir):
	def __init__(self, path, make=False, makeDirs=False):
		super().__init__(self, make, makeDirs)

class ConfigSetup(object):
	
	def __init__(self, defaultConfigFilePaths=[], section="main"):
		self.section = section
		self.parser = configargparse.ArgParser(\
			default_config_files=defaultConfigFilePaths,\
			formatter_class=configargparse.ArgumentDefaultsHelpFormatter)
		
		# The config parameter names can be overriden in subclasses.
		self.configConfigOptionName = "config" # For easy reference on the Namespace object.
		self.shortConfigParameter = "-c" # short command line parameter
		
		self.setUp()
	
	@property
	def longConfigParameter(self):
		"""Config option name prepended with '--': This is the command line parameter equivalent."""
		return "--{0}".format(self.configConfigOptionName)
	
	def setUp(self):
		"""Override with your config setup."""
		pass
	
	def getConfig(self, configFilePath=None, make=False):
		"""Return a config object with the values resolved as set up."""
		
		if not configFilePath == None:
			
			# Make sure config file exists.
			# This is not a configparser file, but a configargparse file. Thus,
			# we don't use ConfigFile, but File, treating it as a generic file.
			configFile = File(configFilePath, make=make, makeDirs=make)
			
			# Add config file path option to command line parameters.
			self.parser.add(self.shortConfigParameter, self.longConfigParameter, is_config_file=True,\
				default=configFilePath)
	
			# Get config. #NOTE: Code duplication.
			config = self.parser.parse_args()
			
			# If the file didn't exist before we created it, fill it with our current configuration.
			if make and not configFile.existed:
				
				# Get a version of config without config attribute for conf file initialization.
				configForFileInit = copy.copy(config)
				delattr(configForFileInit, "config")
				
				# Write config file.
				# Add a header at the top for consistency with the configparse based API config files.
				self.parser.write_config_file(\
					configForFileInit,\
					[getattr(config, self.configConfigOptionName)])
				# Add a section at the top for consistency with the configparse based API config files.
				configFile.write("[{section}]\n{body}".format(section=self.section, body=configFile.read()))
		else:
			# Get config. #NOTE: Code duplication.
			config = self.parser.parse_args()
		
		return config