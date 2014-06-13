import commands
import os

def removerepo(reponame):
    os.chdir('..')
    os.system('rm -rf ' + reponame)

def initrepo(reponame, username, password):
    os.system('mkdir ' + reponame)
    os.chdir(reponame)
    os.system('git init')
    os.system('touch README')
    os.system('git add README')
    os.system('git commit -m "init"')
    os.system('git remote add origin https://'+username+':'+password+'@gitlab-test.forgeservicelab.fi/'+username+'/' + reponame + '.git')
    os.system('git push -u origin master')

