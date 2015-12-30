import sys
import csv
import ConfigParser
import pymysql

def dbConnect(dbSettings):
	"""
	Connects to the database

	:param dbSettings: The settings of the database taken from the config file
	:type dbSettings: Dictionary
	"""
	dbConnection = pymysql.connect(
		host=dbSettings['host'],
        user=dbSettings['username'],
        passwd=dbSettings['password'],
        db=dbSettings['name']
    )
	return dbConnection

def dbInsert(dbSettings, output):
	"""
	Inserts the record into the database

	:param dbSettings: The settings of the database taken from the config file
	:type dbSettings: Dictionary

	:param output: The record that should be inserted in the format of 'column: value'
	:type output: Dictionary
	""" 
	# Open connection
	connection = dbConnect(dbSettings)
	cursor = connection.cursor()
	
	# Query parameters
	data = ', '.join(['%s'] * len(output))
	columns = ', '.join(output.keys())
	
	# Build query
	query = "INSERT INTO %s (%s) VALUES (%s)" % (dbSettings['tableName'], columns, data)
	
	# Execute query
	try:
		cursor.execute(query, output.values())
	except Exception, exception:
		# This requires better error handling
		print "Error inserting into the database. \n "
		exit()
	connection.commit()
	
	# Close connection
	cursor.close()
	connection.close()
	

def getConfig(section, option):
	"""
	Reads the config from the config file based on the section and option given.

	:param section: The section of the config file where the option resides.
	:type section: string

	:param option: The option that is to be retrieved from the config file. 
	:type option: string
	"""
	config = ConfigParser.ConfigParser()
	config.read('config.ini')
	return config.get(section, option)



# assign database section from config file
dbSettings = {'name' : None, 'host' : None, 'port' : None, 'username' : None, 'password' : None, 'tableName' : None}
for key, elem in dbSettings.items():
	dbSettings[key] = getConfig('Database', key)

inputFile =  getConfig('InputFiles', 'csv')
inputColumns = getConfig('InputFiles', 'columns').split(',')
outputDBFields = getConfig('OutputFormat', 'fields').split(',')

reader = {}
outputRow = {}
with open(inputFile, 'rt') as csvFile:
   	reader = csv.DictReader(csvFile)
   	for row in reader:
   		outputRow = {}
   		for column, field in zip(inputColumns,outputDBFields):
   			try: 
   				outputRow[field] = row[column]
   			except KeyError, e:
   				print str("The spelling of " + column + " in the config.ini file and the csv provided do not match. \n This may be due to trailing/leading spaces.")
   				exit()
   		dbInsert(dbSettings,outputRow)





