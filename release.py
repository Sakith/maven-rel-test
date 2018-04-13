from xml.dom.minidom import parse, parseString
import os
from subprocess import call


release_version = None
run_version = None

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

def prepare_mvn_command(release_version):
    command = "$M2_HOME/mvn --settings settings.xml --batch-mode release:prepare -DreleaseVersion="+ release_version
    return command

pom = parse("pom.xml")
itemlist = pom.getElementsByTagName("version")[0]

run_version = getText(itemlist.childNodes)
print(getText(itemlist.childNodes))

#test
# os.environ["deploy_stage"] = "qa"



print (os.environ["deploy_stage"])

if os.environ["deploy_stage"] == "qa":
    release_version = run_version.replace("-SNAPSHOT" , "")
    if "RC" not in release_version:
        release_version += "-RC1"
    # release_version = run_version.replace("-SNAPSHOT" , "")
    print (release_version)
    mvn_command = prepare_mvn_command(release_version)
    f= open("version.txt","w+")
    f.write(release_version)

    os.system("git remote set-url origin https://Sakith:F6LJeyCD90@github.com/sakith/maven-rel-test.git")
    os.system("git add -A")
    os.system("git commit -m \"update release version to  "+release_version+" \" ")

    os.system(mvn_command)

elif os.environ["deploy_stage"] == "prod":
    print ("prod release activating.....!")
    if "RC" in run_version:
        release_version = run_version.split("-")[0]
    print (release_version)
    mvn_command = prepare_mvn_command(release_version)
    f= open("version.txt","w+")
    f.write(release_version)

    os.system("git remote set-url origin https://Sakith:F6LJeyCD90@github.com/sakith/maven-rel-test.git")
    os.system("git add -A")
    os.system("git commit -m \"update release version to  "+release_version+" \" ")

    os.system(mvn_command)

