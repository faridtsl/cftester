#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import subprocess
import sys

class bcolors:
	UNDERLINE = '\033[4m'
	BOLD = '\033[1m'+UNDERLINE
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'+BOLD
	WARNING = '\033[93m'+BOLD
	FAIL = '\033[91m'+BOLD
	ENDC = '\033[0m'

with open('contest', 'r') as f:
    contest = f.readline()
ur = 'http://codeforces.com/contest/'+contest[:-1]+'/problem/'+sys.argv[1]
response = urllib2.urlopen(ur)
soup = BeautifulSoup(response)
html = response.read()
outs = []
ins = []
for l in soup.findAll('div', attrs={'class': re.compile("input$")}):
	txt = ''
	for c in l.findChildren('pre')[0].contents:
		if str(c) == '<br />':
			c = "\n"
		txt = txt + str(c)
	ins.append(txt)
for l in soup.findAll('div', attrs={'class': re.compile("output$")}):
	txt = ''
	for c in l.findChildren('pre')[0].contents:
		if str(c) == '<br />':
			c = "\n"
		txt = txt + str(c)
	outs.append(txt[:-1])

res = subprocess.Popen(["g++",sys.argv[1]+".cpp"],stdout=subprocess.PIPE)
res.communicate()
j = 0
for i in ins :
	print(bcolors.WARNING+"Test Case " + str(j+1)+bcolors.ENDC)
	p = subprocess.Popen(["./a.out"],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	res = p.communicate(i)[0]
	if outs[j] == res[:-1] :
		jd = bcolors.OKGREEN + "YES" + bcolors.ENDC
	else:
		jd = bcolors.FAIL + "NO" + bcolors.ENDC
	print(bcolors.BOLD+"Input :"+bcolors.ENDC)
	print(i)
	print(bcolors.BOLD+"Output :"+bcolors.ENDC)
	print(res)
	print(bcolors.BOLD+"Expected Output :"+bcolors.ENDC)
	print(outs[j] + "\n")
	print("Verdict : " + jd)
	print("\n==========================================\n")
	j+=1
