//github.com/thegrayninja
//work in progress

import requests
import json
from sigsci_auth import SigSciAuth, ApiHost, CorpName, SiteName



def ViewAgents(MyHeader):
	Url = ApiHost + ('/corps/%s/sites/%s/agents' % (CorpName, SiteName))
	AgentsInfo = requests.get(Url, headers=MyHeader)

	TempAgentJson = open("temp_agent_list.json", "w")
	TempAgentJson.write(AgentsInfo.content)
	TempAgentJson.close()

	with open ("temp_agent_list.json", "r") as data_file:
		Data = json.load(data_file		)
		Results = ""
		Counter = 0
		for Agents in (Data["data"]):
			AgentName = (Data["data"][Counter]["agent.name"])
			AgentAlive = (Data["data"][Counter]["agent.status"])
			if AgentAlive == "offline":
				AgentAlive = "AGENT IS OFFLINE!"
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
			return ViewAgents(SigSciAuth())
		elif (UserSelection == 4):
			print "Sorry, that feature is currently disabled. Try again"
			MenuSelection()
		else:
			print "Meh....Try again"
			MenuSelection()
		
	except:
		print "Meh....Try again"
		MenuSelection()



def Menu():
	print "Please make a selection\n\n"
	print "Selection\tTask"
	print "-------------------------------------"
	print "1\tView All Corp Accounts"
	print "2\tView All Sites"
	print "3\tView All Agents"
	print "4\tView Single Agent Information"
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
		print TaskResults
		RunProgram = RunAnotherTask()

	return 0
	

if __name__ == main():
	main()

