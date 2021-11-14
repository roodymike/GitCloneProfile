import requests
import json
import time
import os

username = input("Please provide the username of the repos to clone :- ")

result = requests.get('https://api.github.com/users/'+username.strip().lower()+'/repos?per_page=100&type=public&page=1')
if len(str(result.text)) > 2:
    i = 2
    repoDir = []
    repoNames = []
    repoData = result.json()

    while len(str(result.text)) > 2:
        result = requests.get('https://api.github.com/users/'+username.strip().lower()+'/repos?per_page=100&type=public&page='+str(i))
        i=i+1
        repoData = repoData + result.json()

    for repos in repoData:
        repoDir.append((repos["clone_url"]))
        repoNames.append((repos["name"]))

    choice = input("Total number of "+str(len(repoDir))+ " Repositories found. Do you want to clone all of them into "+os.getcwd()+"\repos ? \nPress \" Y \" for Yes or \" N \" for No :- ")
    if(choice == "Y" or choice == "Yes" or choice == "yes" or choice == "y"):
        print("Cloning may take some time please sit back. We will report you once done.")
        time.sleep(4)
        for i in range(0, len(repoDir)):
            os.system("git clone "+repoDir[i]+" ./repos/"+username.strip().lower()+"/"+repoNames[i])
    print("All Repos cloned!")

else:
    print("Invalid Username or no Repository present in current username")

print("Program exsited successfully")