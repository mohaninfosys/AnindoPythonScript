import library
import config
import os
import time

# Get the current path of the file
currentPath = os.path.dirname(os.path.realpath(__file__))

# Get the file location of config file
configFile = config.config_path

# Load the config in config Object
configObj = library.jsonLoader(configFile).jsonContent

# Common method to build command from test cases
def generateCommand(caseObj):
    output = ''
    # basestring depricated in < 3
    try:
        basestring
    except NameError:
        basestring = str
    if 'method' in caseObj:
        command = []
        command.append(caseObj['method'])
        for args in caseObj['args']:
            if isinstance(args, basestring):
                command.append("\"" + str(args) + "\"") 
            elif isinstance(args, (float, int)):
                command.append(str(args)) 
            else:
                command.append(generateCommand(args))
        i = 0
        while i < len(command):
            if command[i] is not None:
                if i == 0:
                    output += str(command[i]) + "("
                elif i == len(command) - 1 :
                    output += str(command[i]) 
                else:
                    output += str(command[i]) + ","
            i += 1
        output += ")"
        print(output)
    elif 'config' in caseObj:
        output = "configObj"+caseObj['config']
    return output

# From config check which modules we need to test
for cases in configObj['cases']:
    # Find test cases for selected module
    for testCases in configObj['cases'][cases]:
        # Load test steps for test case
        caseFile = currentPath+"/cases/"+cases+"/"+testCases+".json"
        testObj = library.jsonLoader(caseFile).jsonContent
        # Execute testing steps in mentioned browsers
        for drivers in testObj['drivers']:
            #set the driver
            library.commonUtils.setdriver(drivers)
            stepCount = 1
            for testCaseStep in testObj['cases']:
                #generate command
                command = generateCommand(testCaseStep)
                #print(str(stepCount) + " : " + command)
                eval(command)
                stepCount += 1