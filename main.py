import requests, time, os

hit = 0
bad = 0
os.system(f'title Roblox To Discord By (...)#4953 ^| Hits: {hit} ^| Bad: {bad} ^')
print("[1] Singe Lookup\n[2] Mass Lookup\n")
choice = input(">>> ")

def scheck(userid):
  global hit, bad
  r = requests.get(f"https://verify.nezto.re/api/reverse/{userid}")
  if r.status_code == 200:
    discordid = r.json()[0]['discordId']
    robloxname = requests.get(f"https://users.roblox.com/v1/users/{userid}").json()['name']
    print(f"Username: {robloxname}\nDiscord ID: {discordid}")
    hit += 1
    os.system(f'title Roblox To Discord By (...)#4953 ^| Hits: {hit} ^| Bad: {bad} ^')
    input("\nPress any key to exit\n")
  else:
    bad += 1
    os.system(f'title Roblox To Discord By (...)#4953 ^| Hits: {hit} ^| Bad: {bad} ^')
    input("This user does not have their discord linked\n\nPress any key to exit\n")
    
def bcheck(fileinput, savehits):
  global hit, bad
  file = open(f"{fileinput}", 'r')
  t = time.localtime()
  current_time = time.strftime("%H,%M,%S", t)
  while True:
    time.sleep(2)
    userid = file.readline().strip()
    if not userid:
      input("\nFinished!\nPress any key to exit!\n")
    r = requests.get(f"https://verify.nezto.re/api/reverse/{userid}")
    if r.status_code == 200:
      discordid = r.json()[0]['discordId']
      robloxname = requests.get(f"https://users.roblox.com/v1/users/{userid}").json()['name']
      print(f"Roblox Username: {robloxname}\nDiscord ID: {discordid}\n")
      hit += 1
      os.system(f'title Roblox To Discord By (...)#4953 ^| Hits: {hit} ^| Bad: {bad} ^')
      if savehits == "y":
        open(f"results/{current_time}.txt", "a").write(f"Username: {robloxname}\nDiscord ID: {discordid}\n\n")
    else:
      bad += 1
      os.system(f'title Roblox To Discord By (...)#4953 ^| Hits: {hit} ^| Bad: {bad} ^')

if choice == "1":
  userid = input("Enter Roblox Userid: ")
  os.system('cls')
  scheck(userid)

if choice == '2':
  fileinput = input("Enter File Name: ")
  savehits = input("Save hits?\ny/n: ")
  os.system('cls')
  bcheck(fileinput, savehits)
