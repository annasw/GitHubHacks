# Script to access my github and check whether i've
# contributed anything today.
#
# Works, although there's this weird thing where GitHub shows
# different figures when I'm logged in vs. logged out
# (weirdly, higher when I'm logged out) and I have no idea why.
# But we don't care; we just want 0 vs >0.

import requests

# Takes the name of a profile on GitHub as a parameter.
# Returns a Boolean that is
# True if that person has contributed something to GitHub today,
# False otherwise (or if the profile doesn't exist)
def hasContributedToday(profile_name):
	try:
		r = requests.get('https://github.com/'+profile_name)
		rVal = r.text.rfind('x="-39" y="72"')
		s = r.text[rVal + 42]
		return s>0
	except:
		return False

# checks my profile.
if __name__ == '__main__':
	print hasContributedToday('jsperlingwhite')