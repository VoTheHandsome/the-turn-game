# Basic RPG game
# Made by VoTheHandsome on 4th of June 2021.

import random
import sys

#Game values
totalturns = 50 #how much turns are made
coinsperlevel = 25 #how much coins is given for a lv.1 enemy
upgradecost = 15 #how much it costs to upgrade a weapon
upgradelevel = 5 #how much level is added during an upgrade
additionalupgrade = 25 #how much HP is added to enemies on different levels
normalDamage = 5 #how much normal enemies damage
additionaldamage = 5 #how much damage is added to enemies based on levels

#Special values
debugFeatures = 0 #debug features - add coins, skip attacks, etc

#Award values
attused = 0 #How much time was attacking used
upgrused = 0 #How much time was upgrading used
buyused = 0 #How much time was buying used
healused = 0 #How much time was buying used

rules1 = """
The Rules / How To Play

In this game, you have 50 turns and try to not die. 
In each turn, you can do one of the four actions: 
attack, upgrade, buy or heal.

ATTACKING
To attack, type "a" on a new turn. Both the player and
you have an amount of health, which depends on factors 
like enemy level or previous attacks. You have a choice 
to either attack or upgrade your armor. Once you're done,
the enemy will choose what to do. Level 1s can only attack,
but level 2 and 3 enemies can upgrade armor. If you win,
"""

rules2 = """
UPGRADING
You can pay 5 coins to upgrade your current weapon. Once
upgraded, it will deal 5 more damage to the enemy. You
can only upgrade a weapon twice.

BUYING
There are 5 weapons in the game. By default, you have a 
Wooden Sword, however you can buy better weapons like
a pistol, a minigun or even a lazer gun! Each weapon
costs coins. While a pistol costs 20 coins, the lazer
gun costs 200.
"""

rules3 = """
HEALING
Necessary after almost every match. For 5 coins, will
make player's HP level 100.

AWARDS
There are 5 awards in the game.
Hunter - attack 20 or more times.
Upgrader - upgrade all of your guns.
Shopoholic - buy every gun.
Doctor - heal 20 or more times.
Madman - get every award possible (and get a message!)
"""

rules4 = """
NOTES AND TIPS
-Enemies get harder the farther you go, so remember
to upgrade and buy new guns!
-It is a good practice to defend at first, then 
attack. Your armor level saves!
-There is a bug that when you buy a gun, the game
will say that you're out of coins even though 
you aren't. It's alright and will be fixed!

Happy playing!
"""

class Weapons:

	sword = {

		"name":"Sword",
		"dmg":10,
		"price":0,
		"ul":0
		
	}

	pistol = {
		
		"name":"Pistol",
		"dmg":15,
		"price":20,
		"ul":0
		
	}
	automatic = {

		"name":"Automatic Gun",
		"dmg":25,
		"price":50,
		"ul":0
		
	}
	minigun = {

		"name":"Minigun",
		"dmg":40,
		"price":100,
		"ul":0
		
	}
	lazer = {

		"name":"Lazer Gun",
		"dmg":50,
		"price":200,
		"ul":0
		
	}


#Player values
coins = 0
weapons = 1
inventory = [Weapons.sword]
health = 100
armor = 20
bestWeapon = Weapons.sword
bestWeaponID = 0
#I don't specify the turns here!

#Game

i = 1
print("===========BEGINNING OF GAME===========")

yn = input("Would you like to see the rules / how to play? (Y/N): ")

if yn.lower() == "y":
	print(rules1)
	input("Press ENTER to continue")
	print(rules2)
	input("Press ENTER to continue")
	print(rules3)
	input("Press ENTER to continue")
	print(rules4)
	input("Press ENTER to start the game")

print("You have been given a Wooden Sword and 20 armor!")
while i < totalturns + 1:
	if i < 1:
		input("ERROR: 0 or negative amount of turns. Press ENTER to quit the game.")
		sys.exit()
	print("===========Turn {}===========".format(i))
	print("HEALTH: {} | COINS: {} | ARMOR: {} | WEAPON: {}".format(health, coins, armor, bestWeapon["name"].upper()))
	choice = input("What do you want to do? (Attack / Upgrade / Buy / Heal): ")
	if choice.lower() == "attack" or choice.lower() == "a":
		print("===========ATTACK===========")
		attused += 1
		print("You have chosen: Attack")
		lvl = random.randrange(1,3)
		enemyHP = 80
		enemyDmg = normalDamage
		enemyArmor = 0
		if lvl == 2:
			enemyDmg = enemyDmg + additionaldamage
			enemyHP = 100 
		elif lvl == 3:
			enemyDmg = enemyDmg + additionaldamage + additionaldamage
			enemyHP = 120 
		print("A level {} enemy appeared!".format(lvl))
		
		while enemyHP > 0 and health > 0:
			print("Enemy has " + str(enemyHP) + " HP and you have " + str(health) + " HP")
			choic = input("Defend or attack? (D/A): ")
			if choic.lower() == "defend" or choic.lower() == "d":
				boost = random.randrange(1, 15)
				armor = armor + boost
				print("You defend and now your armor protection level is {}!".format(armor))
			elif choic.lower() == "attack" or choic.lower() == "a":
				#legacy attack system

				#damage = bestWeapon["damage"]
				#enemyHP = enemyHP - damage
				
				#new attack system

				damage = bestWeapon["dmg"]  #damage of best weapon
				enemyArmorCent = enemyArmor / 100	#find out 1/100 of the enemy armor
				enemyArmorCent += 1
				dmgReal = int(damage / enemyArmorCent)	#the real damage. it takes armor into account
				enemyHP = enemyHP - dmgReal	#damage
				print("You have dealt {} damage and enemy now has {} HP!".format(dmgReal, enemyHP))
			elif choic.lower() == "skipattackdebug":
				if debugFeatures == 1:
					print("Skipped attack, enemy's health is now 0")
					enemyHP = 0
				else:
					print("Debug Features is not on. Enable it using the debugFeatures value.")
			else:
				print("That's not a valid command. You are skipping this move!")
				i = i - 1
			if lvl == 1:
				enemymove = 1
			else:
				enemymove = random.randrange(1, lvl)
			if enemymove == 1:
				armorCent = armor / 100
				armorCent = armorCent + 1
				enemyDmgReal = int(enemyDmg / armorCent)
				health = health - enemyDmgReal
				print("The enemy has dealt you {} damage and now you have {} HP!".format(enemyDmgReal, health))
			elif enemymove == 2 or enemymove == 3:
				boost = random.randrange(1, 15)
				enemyArmor = enemyArmor + boost
				print("The enemy defends and now its armor protection level is {}!".format(enemyArmor))
			print("============NEW MOVE============")
		print("============END OF BATTLE============")
		if health <= 0:
			print("You died!")
			input("Press ENTER to exit the game.")
			sys.exit()
		else:
			print("You won the battle and get {} coins!".format(lvl * 20))
			normalDamage += 5
			coins += 20
	elif choice.lower() == "u" or choice.lower() == "upgrade":
		print("===========UPGRADE===========")
		upgrused += 1
		if coins > upgradecost - 1:
			if bestWeapon["ul"] != 2:
				bestWeapon["dmg"] += upgradelevel
				coins = coins - upgradecost
				print("Your {} has been upgraded by {} and now it deals {} damage!".format(bestWeapon["name"], upgradelevel, bestWeapon["dmg"]))
			else:
				print("Your weapon is already upgraded twice!")
		else:
			print("Not enough coins (you need {})! You will skip this turn.".format(upgradecost))
			i = i - 1
			upgrused -= 1
	elif choice.lower() == "b" or choice.lower() == "buy":
		print("===========BUY===========")
		buyused += 1
		if bestWeaponID == 0:
			if coins >= Weapons.pistol["price"]:
				bestWeapon = Weapons.pistol
				bestWeaponID = 1
				coins = coins - Weapons.pistol["price"]
				print("You have just bought a Pistol for {} coins and now you have {} coins.".format(Weapons.pistol["price"], coins))
			elif coins < Weapons.pistol["price"]:
				print("You do not have enough coins. You will skip this turn.")
				i = i - 1
				buyused -= 1
		###############################################################
		if bestWeaponID == 1:
			a = Weapons.automatic
			if coins >= a["price"]:
				bestWeapon = a
				bestWeaponID = 2
				coins = coins - a["price"]
				print("You have just bought an Automatic Gun for {} coins and now you have {} coins.".format(a["price"], coins))
			elif coins < a["price"]:
				print("You do not have enough coins. You will skip this turn.")
				i = i - 1
				buyused -= 1
		###############################################################
		if bestWeaponID == 2:
			a = Weapons.minigun
			if coins >= a["price"]:
				bestWeapon = a
				bestWeaponID = 3
				coins = coins - a["price"]
				print("You have just bought a Minigun for {} coins and now you have {} coins.".format(a["price"], coins))
			elif coins < a["price"]:
				print("You do not have enough coins. You will skip this turn.")
				i = i - 1
				buyused -= 1
		###############################################################
		if bestWeaponID == 3:
			a = Weapons.lazer
			if coins >= a["price"]:
				bestWeapon = a
				bestWeaponID = 4
				coins = coins - a["price"]
				print("You have just bought a Lazer Gun for {} coins and now you have {} coins.".format(a["price"], coins))
			elif coins < a["price"]:
				print("You do not have enough coins. You will skip this turn.")
				i = i - 1
				buyused -= 1
		###############################################################
		if bestWeaponID == 4:
			print("You already have the best gun. You will skip this turn.")
			i = i - 1
			buyused -= 1
	elif choice.lower() == "h" or choice.lower() == "heal":
		print("===========HEAL===========")
		healused += 1
		if coins >= 5:
			coins = coins - 5
			health = 100
			print("Successfully healed for 5 coins! You now have 100 HP and {} coins.".format(coins))
		else:
			print("You don't have enough coins. You will skip this turn.")
			i = i - 1
			healused -= 1
	elif choice.lower() == "addcoinsdebug":
		cho = input("How much coins to add? 999999 coins will be added if string provided is not a number. - ")
		if type(cho) == int:
			coins += cho
			print("{} coins were added".format(cho))
		else:
			coins += 999999
			print("Not an integer, added 999999 coins instead.")
	else:
		i = i - 1
		print("Not a valid option.")
	i += 1
print("============END OF GAME============")
print("You Won!")
print("============STATISTICS============")
print("Last Gun: " + bestWeapon["name"])
print("Coins: " + str(coins))
print("Health: " + str(health))
print("Armor " + str(armor))
print("============AWARDS============")
if healused > 19:
	print("DOCTOR: Heal 20 or more times.")
if attused > 19:
	print("HUNTER: Attack 20 or more times.")
if buyused == 4:
	print("SHOPOHOLIC: Use the shop until you got the best gun.")
if upgrused > 9:
	print("UPGRADER: Upgraded all of your guns twice.")
if healused > 19 and attused > 19 and buyused == 4 and upgrused > 9:
	print("MADMAN: Got every award in the game. Thank you for playing! -VoTheHandsome")
input("Press ENTER to close the game.")
