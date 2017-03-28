# Script to access my github and check whether i've
# contributed anything today.
#
# What's here so far works, although there's this really weird inconsistency
# where GitHub's count for my contributions changes when I'm logged out and refresh the page.
# it also sometimes spawns an extra day square that disappears when i refresh.
# get your shit together git.
# 
# But we don't care; we just want to check 0 vs >0.

import requests
import os

# Takes the name of a profile on GitHub as a parameter.
# Returns a Boolean that is
# True if that person has contributed something to GitHub today,
# False otherwise (or if the profile doesn't exist)
def hasContributedToday(profile_name):
	try:
		r = requests.get('https://github.com/'+profile_name)
		rVal = r.text.rfind('rect class="day"')
		
		# int to change from unicode to int
		s = int(r.text[rVal + 81])
		return int(s)>0
	except:
		return False

# returns a list of the Euler problems uploaded to my github
# as a list of strings, where the strings are the titles
# of the files
def currentEulers():
	try:
		r = requests.get('https://github.com/jsperlingwhite/Project-Euler')
		t = r.text
		results = []
		subString = 'title="euler'
		currIndex = t.find(subString)
		while currIndex>-1:
			newString = ''
			currIndex+=7
			while t[currIndex]!='"':
				newString = newString + t[currIndex].encode('ascii','replace')
				currIndex+=1
			results.append(newString)
			currIndex = t.find(subString, currIndex)
		return results
	except:
		print "currentEulers() has malfunctioned"

# accesses the projecteuler directory and
# finds the next projecteuler solution i haven't uploaded yet
# returns the name of the chosen file (a .py file in the directory
# that isn't on GitHub)
# returns "!" if choices is empty (i.e. everything is already online)
#
# maybe it should do more work -- return all relevant files in a list?
def getNextEuler():
	try:
		os.chdir('euler\\complete')
		# all files in the folder
		eulers = os.listdir('C:\Users\Jesse\python\euler\complete')
		# just the .py's
		pyFiles = [x for x in eulers if x[-2:]=='py']
		# now take out the ones already online
		currs = currentEulers()
		choices = [x for x in pyFiles if x not in currs]
		if len(choices) == 0: return "!"
		return choices[0]

	except:
		print "something has gone wrong"
		print "you have meddled with forces beyond your comprehension"

def main():
	print hasContributedToday('jsperlingwhite')

# checks my profile.
if __name__ == '__main__': main()
