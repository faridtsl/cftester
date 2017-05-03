#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import subprocess
import sys

class bcolors:
	BOLD = '\033[1m'
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'+BOLD
	WARNING = '\033[93m'
	FAIL = '\033[91m'+BOLD
	ENDC = '\033[0m'
	UNDERLINE = '\033[4m'

with open('contest', 'r') as f:
    contest = f.readline()
ur = 'http://codeforces.com/contest/'+contest[:-1]+'/problem/'+sys.argv[1]
response = urllib2.urlopen(ur)
soup = BeautifulSoup(response)
html = response.read()
outs = []
ins = []
for l in soup.findAll('div', attrs={'class': re.compile("input$")}):
	ins.append(l.findChildren('pre')[0].text)
for l in soup.findAll('div', attrs={'class': re.compile("output$")}):
	outs.append(l.findChildren('pre')[0].text)


res = subprocess.Popen(["g++",sys.argv[1]+".cpp"],stdout=subprocess.PIPE)
res.communicate()
j = 0
print("OUT\t\t\t\tEXPECTED\t\t\tVERDICT")
for i in ins :
	p = subprocess.Popen(["./a.out"],stdout=subprocess.PIPE,stdin=subprocess.PIPE)
	res = p.communicate(i)[0]
	if outs[j] == res[:-1] :
		jd = bcolors.OKGREEN + "YES" + bcolors.ENDC
	else:
		jd = bcolors.FAIL + "NO" + bcolors.ENDC
	print(res[:-1]+"\t\t\t\t"+outs[j]+"\t\t\t\t"+jd)
	j+=1
