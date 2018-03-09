#=======================================================================================
# Imports
#=======================================================================================

import os

#=======================================================================================
# Library
#=======================================================================================

#==========================================================
class BaseFile(object):
	
	#=============================
	"""Base Class for various types of fileobjects as recognized by filesystems."""
	#=============================
	
	def __init__(self, path):
		self.path = path
		self.existed = self.exists # Determines whether this file existed at the time of instantiation.
		
	@property
	def parentDir(self):
		return Dir(os.path.dirname(self.path))

	@property
	def lastModified(self):
		return int(os.path.getmtime(self.path))

	@property
	def secondsSinceLastModification(self):
		return int(time.time()) - int(self.lastModified)

	@property
	def exists(self):
		return os.path.exists(self.path)
	
class MakeableFile(BaseFile):
	
	#=============================
	"""Extension of BaseFile with file making checks and 'make' as an interface stub. For subclassing."""
	#=============================
	
	def __init__(self, path, make=False, makeDirs=False):
		super().__init__(path)
		if not self.parentDir.exists:
			self.makeDirs()
		if not self.exists and make:
			self.make()
	def make(self):
		# Should probably throw UnimplementedError or something.
		pass#OVERRIDE
	def makeDirs(self):
		os.makedirs(self.parentDir.path)

#==========================================================
class File(MakeableFile):
	
	#=============================
	"""Basic file wrapper.
	Abstracts away basic operations such as read, write, etc."""
	#TODO: Make file operations safer and failures more verbose with some checks & exceptions.
	#=============================
	
	def __init__(self, path, make=False, makeDirs=False):
		super().__init__(path)
	
	def write(self, data):
		with open(self.path, "w") as fileHandler:
			fileHandler.write(data)

	def read(self):
		with open(self.path, "r") as fileHandler:
			return fileHandler.read()

	def remove(self):
			os.remove(self.path)

	def make(self):
		"""Write empty file to make sure it exists."""
		self.write("")

#==========================================================
class Dir(BaseFile):
	
	#=============================
	"""Represents a directory on the filesystem."""
	#=============================
	
	def __init__(self, path, make=False, makeDirs=False):
		super().__init__(path)
	
	def remove(self, nonEmpty=False):
		"""Remove directory from the filesystem. Only supports empty directories as of now."""
		if nonEmpty:
			pass#NOTE: Not implemented yet, as this part needs some careful deliberation first.
			#shutil.rmtree(self.path)
		else:
			os.rmdir(self.path)
	
	@property
	def fileNames(self):
		"""Returns a list of the names of all files in the directory."""
		return os.listdir(self.path)
	
	@property
	def filePaths(self):
		"""Returns a list of absolute paths of all files in the directory."""
		filePaths = []
		for fileName in self.fileNames:
			filePaths.append(os.path.join(self.path, fileName))
		return filePaths
	
	@property
	def files(self):
		"""Returns a list of File or Dir objects of all files or dirs in the directory."""
		pass#TODO
	
	def make(self):
		os.mkdir(self.path)