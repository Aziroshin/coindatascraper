#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#=======================================================================================
# Imports
#=======================================================================================

import psycopg2

#=======================================================================================
# Library
#=======================================================================================

class Database(object):
	
	#=============================
	"""Represents database access and operations; holds the DB handler and convenience methods."""
	#=============================
	
	def __init__(self, host, port, dbName, user, password):
		self.handler = psycopg2.connect(host=host, dbname=dbName, port=port, user=user, )
		self.cursor = self.handler.cursor()
	def 
