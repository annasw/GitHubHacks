# GithubHacks
My attempts to make GitHub work better for me. So far this is just a script to try to ensure that my grid of little squares turns green.

My script will eventually do the following:
1. Check whether I have uploaded anything to GitHub today (and if so do nothing further);
2. Check which ProjectEuler solutions I've uploaded to my GitHub;
3. Get a list of ProjectEuler (.py) solutions in the directory on my computer;
4. Compare the two to get a list of solutions on my computer but not GitHub, and pick one;
5. Upload it to GitHub...
6. Preferably with whatever associated files (.txt, e.g.) it needs to work;
7. And do all this checking once a day, whether as a Daemon (or the Windows equivalent) or through some process that executes the script once a day.

So far I have functionality for 1-4.

(5) is going to be tricky; I'm not sure if the requests module has the functionality to let me upload files to GitHub, and if not I'll have to find a different module for it.

(6) is also going to be a little tricky, mostly because my local projecteuler folder is pretty disorganized. I'll probably rename the relevant non-.py files to have the name of the euler problem, which should make it pretty trivial.

(7) is weird. I don't have an approach to this, despite quite a bit of research. Annoyingly, there are tons of Daemon implementations for Unix/Linux systems, but none that I can find (except weird built-in Windows ones) for the OS that 91.76% of all computers users run. But I'm sure it's out there.
