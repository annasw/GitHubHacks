# Script to access my github and check whether i've
# contributed anything today.
#
# Works, although there's this really weird inconsistency
# where GitHub's count for my contributions changes when I'm logged out and refresh the page.
# it also sometimes spawns an extra day square that disappears when i refresh.
# get your shit together git.
# 
# But we don't care; we just want to check 0 vs >0.

import requests

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

# debugging method. takes a profile name and
# returns # of contributions today
def numContributionsToday(profile):
	try:
		r = requests.get('https://github.com/'+profile)
		rVal = r.text.rfind('x="-39" y="72"')
		s = r.text[rVal + 42]
		return int(s)
	except:
		return "Not a real profile"

# checks my profile.
if __name__ == '__main__':
	print hasContributedToday('jsperlingwhite')
