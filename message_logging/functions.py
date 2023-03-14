scriptLog = []
def log_messages(message:str, messageType: str = "Info", printMessage: bool = True):
	global scriptLog
	scriptLog.append({"type": messageType, "log":message})
	if printMessage == True:
		print(message)

def emptyScriptLog():
	global scriptLog
	scriptLog = []

def getErrorCount():
	errorCount = 0
	for message in scriptLog:
		if message["type"] == "Error":
			errorCount +=1
	
	return errorCount

def getScriptLogString():
	scriptLogString = '' 
	for logEntry in scriptLog:
		if logEntry['type'] == 'Info':
			scriptLogString += logEntry["log"]+"\n"	
		else:
			scriptLogString += logEntry["type"] +': '+ logEntry["log"]+"\n"	

	return scriptLogString