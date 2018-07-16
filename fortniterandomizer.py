from microbit import *
import random


vbucks2 = 0 
location = ["Loot Lake", "Tilted Towers", "Pleasant Park", "Haunted Hills", "Snobby Shores", "Wailing Woods", "Paradise Palms", "Tomato Town", "Junk Junction", "Flush Factory", "Fatal Fields", "Lazy Links", "Salty Springs", "Retail Row", "Greasy Grove", "Shifty Shafts", "Risky Reels", "Lucky Landing", "Lonely Lodge"]
coordinatenletter = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
coordinatencijfer = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
weapon = ["Yellow SCAR", "Purple SCAR", "Blue AR", "Green AR", "Gray AR", "Purple Tactical-Submachine gun", "Blue Tactical-Submachine gun", "Green Tactical-Submachine gun", "Blue Silenced Submachine gun", "Green Silenced Submachine gun", "Gray Silenced Submachine gun", "Blue Pump Shotgun", "Green Pump Shotgun", "Gray Tactical Shotgun", "Green Tactical Shotgun", "Blue Tactical Shotgun", "Green Hunting Rifle", "Blue Hunting Rifle", "Yellow Bolt Sniper", "Purple Bolt Sniper", "Blue Bolt Sniper", "Purple Semi-Auto Sniper", "Yellow Semi-Auto Sniper", "Blue Burst AR", "Green Burst AR", "Gray Burst AR", "Purple Famas", "Yellow Famas", "Purple Scoped AR", "Blue Scoped AR", "Blue Drum Gun", "Green Drum Gun", "Purple Minigun", "Yellow Minigun", "Purple LMG", "Blue LMG", "Purple Thermal Scoped AR", "Yellow Thermal Scoped AR", "Yellow Heavy Shotgun", "Purple Heavy Shotgun", "Purple Dual Pistols", "Yellow Dual Pistols", "Purple Deagle", "Yellow Deagle", "Gray Pistol", "Green Pistol", "Blue Pistol", "Blue Revolver", "Green Revolver", "Gray Revolver", "Purple Supressed Pistol", "Yellow Supressed Pistol", "Blue RPG", "Purple RPG", "Yellow RPG", "Blue Grenade Launcher", "Purple Grenade Launcher", "Yellow Grenade Launcher"]
vbucks = [100, 500, 1000, 2000, 1500, 2800, 6500, 12000, 50, 150]
items = ["Whiplash", "Brite Gunner", "Raptor", "Raven", "Munitions Expert", "Survival Specialist", "Red Knight", "Skull Trooper", "Nog Ops"] 

inv = []



while True:
    if button_a.is_pressed() and not button_b.is_pressed():
        display.scroll("Go here!")
        sleep (1000)
        display.scroll(random.choice(location))
    if button_b.is_pressed() and not button_a.is_pressed():
        gekozenwapen = (random.choice(weapon))
        display.scroll("Your next weapon!")
        sleep (1000)
        display.scroll(gekozenwapen)
        inv.append(gekozenwapen)
    if accelerometer.current_gesture() == "left":
        display.scroll("You get")
        vbucks2 += (random.choice(vbucks))
        display.scroll(vbucks2)
        display.scroll("Vbucks")    
    if accelerometer.current_gesture() == "right":
        display.scroll(random.choice(items))
    if button_a.is_pressed() and button_b.is_pressed():
        display.scroll("Inventory:")
        for item in inv:
          display.scroll(item)
        display.scroll("Your Vbucks")
        display.scroll(vbucks2)
    