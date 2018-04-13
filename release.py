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
    command = "mvn --settings settings.xml --batch-mode release:prepare -DreleaseVersion="+ release_version
    return command

pom = parse("pom.xml")
itemlist = pom.getElementsByTagName("version")[0]

run_version = getText(itemlist.childNodes)
print(getText(itemlist.childNodes))

#test
os.environ["deploy_stage"] = "qa"

release_version = run_version.replace("-SNAPSHOT" , "")

print (os.environ["deploy_stage"])

if os.environ["deploy_stage"] == "qa":
    if "RC" not in release_version:
        release_version += "-RC1"
    # release_version = run_version.replace("-SNAPSHOT" , "")
    print (release_version)
    mvn_command = prepare_mvn_command(release_version)
    f= open("version.txt","w+")
    f.write(release_version)

    os.system("git remote set-url origin https://Sakith:SwmnT@#~12@github.org/maven-rel-test.git")
    os.system("git add -A")
    os.system("git commit -m \"update release version to  "+release_version+" \" ")

    os.system(mvn_command)

# if "SNAPSHOT" in run_version:
#     release_version = run_version.replace("-SNAPSHOT")
#     print ("fine")

# mvn --batch-mode -Dtag=my-proj-1.2 release:prepare -DreleaseVersion=1.2 -DdevelopmentVersion=2.0-SNAPSHOT