##github.com/thegrayninja
##

import requests
import json
from sigsci_auth import SigSciAuth, ApiHost, CorpName, SiteName

####
####
##ORDER OF OPERATIONS
#
#main()
#Menu()
#MenuSelection()  #branches to...
#	>ViewCorps()		#TODO Need to parse
#	>ViewSites()		#TODO Need to parse
#	>ViewOfflineAgents()	
#	>ViewOnlineAgents()
#	>ViewAgentInfo() 	#TODO currently not setup
#	> each above then points to selecting an environment
#		>ChooseSite()



#this is not currently used, but keeping just in case
def SaveToFile(DataToSave):
	FileName = raw_input("To save your document, please enter a filename: ")	
	SaveFile = open(FileName, "w")
	SaveFile.write(DataToSave)
	SaveFile.close()
	print ("Your Report has been saved as %s to the current directory.")


def ChooseSite():
	Loop = 1	
	while (Loop == 1):
		print ("Available Environments\n\n")
		print "Selection\tTask"
		print "-------------------------------------"
		print "1\t<friendlysitename>"
		print "2\t<friendlysitename>"
		print "3\t<friendlysitename>"
		ChosenSite = raw_input("\nWhich environment would you like to run reports against?\n> ")
		if (ChosenSite == 'q'):
			return 0;

		elif (ChosenSite == "1"):
			Loop = 0
			return "<sitename>"  #for url
			break;
		elif (ChosenSite == "2"):
			Loop = 0
			return "<sitename>"  #for url
			break;
		elif (ChosenSite == "3"):
			Loop = 0
			return "<sitename>"  #for url
			break;
		else:
			Loop = 1

	






def ViewOfflineAgents(MyHeader):
	SiteName = ChooseSite();

	Url = ApiHost + ('/corps/%s/sites/%s/agents' % (CorpName, SiteName))
	AgentsInfo = requests.get(Url, headers=MyHeader)

	TempAgentJson = open("temp_agent_list.json", "w")
	TempAgentJson.write(AgentsInfo.content)
	TempAgentJson.close()

	with open ("temp_agent_list.json", "r") as data_file:
		Data = json.load(data_file)
		Results = "HOSTNAME,STATUS,REMOTE_IP\n"
		Counter = 0
		for Agents in (Data["data"]):
			AgentName = (Data["data"][Counter]["agent.name"])
			AgentAlive = (Data["data"][Counter]["agent.status"])
			AgentRemoteIP = (Data["data"][Counter]["host.remote_addr"])
			if AgentAlive == "offline":
				AgentAlive = "AGENT IS OFFLINE!"
				Results = Results + "%s,%s,%s\n" % (AgentName, AgentAlive, AgentRemoteIP)
			Counter += 1
	
	return Results


def ViewOnlineAgents(MyHeader):

	SiteName = ChooseSite();

	Url = ApiHost + ('/corps/%s/sites/%s/agents' % (CorpName, SiteName))
	AgentsInfo = requests.get(Url, headers=MyHeader)

	TempAgentJson = open("temp_agent_list.json", "w")
	TempAgentJson.write(AgentsInfo.content)
	TempAgentJson.close()

	with open ("temp_agent_list.json", "r") as data_file:
		Data = json.load(data_file		)
		Results = "HOSTNAME,STATUS,REMOTE_IP\n"
		Counter = 0
		for Agents in (Data["data"]):
			AgentName = (Data["data"][Counter]["agent.name"])
			AgentAlive = (Data["data"][Counter]["agent.status"])
			if AgentAlive == "online":
				AgentRemoteIP = (Data["data"][Counter]["host.remote_addr"])
				Results = Results + "%s,%s,%s\n" % (AgentName, AgentAlive, AgentRemoteIP)
			Counter += 1
	#print Results
	#Data = AgentsInfo.json()
	
	return Results


def ViewSites(MyHeader):
	Url = ApiHost + ('/corps/%s/sites' % (CorpName))
	SitesInfo = requests.get(Url, headers=MyHeader)
	
	return SitesInfo.text


def ViewCorps(MyHeader):
	Url = ApiHost + ('/corps')
	SitesInfo = requests.get(Url, headers=MyHeader)

	return SitesInfo.text


def MenuSelection():
	Loop = 1
	while (Loop == 1):
		UserSelection = raw_input("> ")
		if (UserSelection == 'q'):
			return 0;
		try:
			UserSelection = int(UserSelection)
			if (UserSelection == 1):
				return ViewCorps(SigSciAuth())
			elif (UserSelection == 2):
				return ViewSites(SigSciAuth())
			elif (UserSelection == 3):
				#JsonResults = ViewAgents(SigSciAuth())
				return ViewOfflineAgents(SigSciAuth())
			elif (UserSelection == 4):
				#JsonResults = ViewAgents(SigSciAuth())
				return ViewOnlineAgents(SigSciAuth())
			elif (UserSelection == 5):
				print "Sorry, that feature is currently disabled. Try again"
				Loop = 1;
			else:
				print "Meh....Try again"
				Loop = 1;
				
		
		except:
			print "Meh....Try again"
			Loop = 1;



def Menu():
	print "Please make a selection\n\n"
	print "Selection\tTask"
	print "-------------------------------------"
	print "1\tView All Corp Accounts"
	print "2\tView All Sites"
	print "3\tView Offline Agents"
	print "4\tView Online Agents"
	print "5\tView Single Agent Information"
	print "\nq\tQuit\n\n"
	
	return (MenuSelection())


def RunAnotherTask():
	AnotherTaskResponse = raw_input("Want to run another task? (y/n): ")
	if (AnotherTaskResponse[0].lower()) == 'y':
		main()
	elif (AnotherTaskResponse[0].lower()) == 'n':
		print "\n\nThanks for using the SignalScience API!\nHave a nice day!\n\n"
		return False;
	else:
		RunAnotherTask()


def main():
	print "\n\nWelcome to the SignalScience API!\n\n"
	RunProgram = True
	while RunProgram:
		TaskResults = Menu()
		if (TaskResults == 0):
			return 0;
		else:
			print TaskResults
			RunProgram = RunAnotherTask()

	return 0
	

if __name__ == main():
	main()

