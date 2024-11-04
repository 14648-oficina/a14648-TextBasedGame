import random
i = 1
def endgame():
  print(f"{'----------Game Over----------': ^70}")
def bestending():
  print(f"{'----------Best Ending----------': ^70}")
def capending():
  print(f"{'----------Capture Ending----------': ^70}")
def Goodending():
  print(f"{'----------Good Ending----------': ^70}")

print(f"{'--------Auf Dem Ost-Wind--------': ^70}")
Start1 = input("Do You Want To Enlist? Y/N: ")
Start2 = Start1.lower()
if (Start2 == "no") or (Start2 == "n"):
  print(f"You have refused the Service in name of the Heiliges Vartische KaiserReich. In Response to your dissobidience and downright betrayel of the Kaiser you have been sentenced to death.")
  print(f"{'--------Traitor Ending--------': ^70}")
  endgame()
elif (Start2 == "y") or (Start2 == "yes"):
  print(f"\n{'--------{Der KaiserKrieg}--------': ^70}")
  print("""The Year is 1532 and yet another endless war on the Continent Broke out. The Heiliges Kaiserreich von Varhüt and the Greater Union of Süd-Jøhl-Karbenhäl find themselves another endless Dynastic Dispute. 

The War, Named the “Dritter KaiserKrieg” has reached Stalemate like along the Rhüner River, and in order to break this Stalemate, the Kaiser has authorized a flank through the Schwarzwald, also known as the Black Forest. Tales of Hunters, Soldiers and travelers who’ve entered the Schwarzwald and never came back are all too common and all too known. 

You are a Mercenary Under Kaiser Hartich of Varhüt, tasked with leading a small force and pave the way for the main Vartian Force.

The outcome of the war is in your hands.

Godspeed.""")
  Price = 0
  Warspoils = 0
  global SquadHealth
  SquadHealth = 100
  DamageTaken = 0
  global SquadHealth2 
  SquadHealth2 = SquadHealth
  SquadHealth = SquadHealth2
  HealthBonus = 0
  EnemIsranged = 0
  IsCav = 0
  victory = 0
  IsArmoured = 0
  IsUnarmoured = 0
  CombatResult = 0
  Price = 0
  FleshRangedDamage = 0
  ArmouredRangedDamage = 0
  FleshMeleeDamage = 0
  ArmourMeleeDamage = 0
  HealthBonus = 0
  RangedMissChanceAlly = random.randint(0,0)
  Isranged = 0
  CurrentCoins = 40
  GMammount = 0
  YourFMD = 0
  YourAMD = 0
  GMammount2 = 0
  stataleatorio = 0
  EnemyMeleeDamage = 0
  RangedMissChance1 = 0 
  def GeldMarks():
    GMammount = int(CurrentCoins + Warspoils - Price)
    GMammount2 = GMammount
    print(f"You have {GMammount} GeldMarks")
  def HealthPoints1():
    SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
  
  print("Select your Company: ")
  print("""\n 
  1-Arquebus
  2-Halberdier
  3-Pfalzhammer
  4-Zweihander-Swordsman""")
  ChosenUnit = str(input("\n Type Which Squad you want to take: "))
  Unit = ChosenUnit.lower()
  if (Unit == "arquebus") or (Unit == "1"):
    FleshRangedDamage = 120 ## Damage Dealth During Ranged Phase To Unarmoured Enemies
    ArmouredRangedDamage = 40 ## Damage Dealth During Ranged Phase To Armoured Enemies
    FleshMeleeDamage = 47 ## Damage Dealth During Melee Phase To Unarmorued Enemies
    ArmourMeleeDamage = 20 ## Damage Dealth During Melee Phase To armorued Enemies
    HealthBonus = 0 ## Armour Bonus
    RangedMissChanceAlly = random.randint(1,14) ## The chance to miss
    Isranged = 1 ## Checks if the unit is ranged
  elif (Unit == "halberdier") or (Unit == "2"):
      FleshRangedDamage = 0
      ArmouredRangedDamage = 0
      FleshMeleeDamage = 70
      ArmourMeleeDamage = 90
      HealthBonus = 30
      RangedMissChanceAlly = random.randint(0,0)
      Isranged = 0
  elif (Unit == "pfalzhammer") or (Unit == "3"):
      FleshRangedDamage = 0
      ArmouredRangedDamage = 0
      FleshMeleeDamage = 50
      ArmourMeleeDamage = 120
      HealthBonus = 25
      RangedMissChanceAlly = random.randint(0,0)
      Isranged = 0
  elif (Unit == "zweihander-swordsman") or (Unit == "zweihander swordsman") or (Unit == "4"):
      FleshRangedDamage = 0
      ArmouredRangedDamage = 0
      FleshMeleeDamage = 110
      ArmourMeleeDamage = 47
      HealthBonus = 39
      RangedMissChanceAlly = random.randint(0,0)
      Isranged = 0
  SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
  
  SquadHealth = SquadHealth2
  
  HealthBonus = 0
 
  SquadHealth = SquadHealth2
 
  print("""Choose Your Primary Weapon:
  1-Halberd
  2-Zweihander
  3-Warhammer""")
  ChosenWeapon = str(input())
  Weapon = ChosenWeapon.lower()
  
  if (Weapon == "halberd") or (Weapon == "1"):
    YourFMD = 47
    YourAMD = 58
  
  elif (Weapon == "zweihander") or (Weapon == "2"):
    YourFMD = 57
    YourAMD = 36
  
  elif (Weapon == "warhammer") or (Weapon == "3"):
    YourFMD = 30
    YourAMD = 67
  
  TotalFRD = FleshRangedDamage 
  TotalARD = ArmouredRangedDamage
  TotalFMD = YourFMD + FleshMeleeDamage
  TotalAMD = YourAMD + ArmourMeleeDamage
  
  print(TotalFRD)
  print(TotalARD)
  print(TotalFMD)
  print(TotalAMD)
  print(SquadHealth)
  
  print(f"{'--------Chapter I--------': ^70}")
  print(f"{'Auf der Schwarzwald': ^70}")
  print("After Entering the Schwarzwald, you and your company are met with a dirt path leading to what seems to be a village, a weird sight in such a deadly forest.")
  Dir1_1 = str(input("""Do you wish to
  1- Follow the Path
  2- Ignore the Path and keep moving fowards
  """))
  if Dir1_1 == "1":
    print("You and your forces find themselves infront of a bandit filled town, what used to be an attempt to settle in a remote forest is now a hub for criminal activity")
    print("The Bandits prepare to engage you and your men")
    banditType = ["Spearmen","Swordsmen","Crossbowmen","Armoured AxeMen"]
    BanditEnemy1 = random.choice(banditType)
    Veterancy = random.randint(1,2)
    if Veterancy == 1:
      EnemVeterancy1 = 1
      EnemVeterancy2 = "Unprepared"
    elif Veterancy == 2:
      EnemVeterancy1 = 1.6
      EnemVeterancy2 = "Seasoned"
    
    if BanditEnemy1 == "Spearmen":
      EnemyMeleeDamage = 50
      EnemyRangedDamage = 0
      EnemyHealth = 60
      IsCav = 0
      IsArmoured = 0
      IsUnarmoured = 1
      RangedMissChance1 = random.randint(0,0)
      EnemIsranged = 0
    elif BanditEnemy1 == "Swordsmen":
        EnemyMeleeDamage = 53
        EnemyRangedDamage = 0
        EnemyHealth = 70
        IsCav                = 0
        IsArmoured = 0
        IsUnarmoured = 1
        RangedMissChance1 = random.randint(0,0)
        EnemIsranged = 0
    elif BanditEnemy1 == "Crossbowmen":
        EnemyMeleeDamage = 33
        EnemyRangedDamage = 60
        EnemyHealth = 40
        IsCav = 0
        IsArmoured = 0
        IsUnarmoured = 1
        RangedMissChance1 = random.randint(1,8)
        EnemIsranged = 1
    elif BanditEnemy1 == "Armoured Axemen":
        EnemyMeleeDamage = 40
        EnemyRangedDamage = 0
        EnemyHealth = 80
        IsCav = 0
        IsArmoured = 1
        IsUnarmoured = 0
        RangedMissChance1 = random.randint(0,0)
        EnemIsranged = 0
    print(f"You're Attacked by a {EnemVeterancy2} group of {BanditEnemy1}")
    Rangedinitiative = random.randint(1,4)
    EnemyMeleeDamage = EnemyMeleeDamage * Veterancy
    if RangedMissChance1 <= 3:
      EnemyRangedDamage = 0
    elif RangedMissChance1 > 3:
      stataleatorio = 0
    
    if (Rangedinitiative >= 3) and (Isranged == 1) or (EnemIsranged == 0):
      print("We Have the Initiative for the Ranged Phase")
      if RangedMissChanceAlly >= 4:
        print("We've hit the enemy")
        if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFRD - EnemyHealth
        elif (IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
          CombatResult = TotalARD - EnemyHealth
        if CombatResult <= 0:
          print("We Have Won we May now take the warspoils and Advance")
          victory = 1
        elif CombatResult > 0:
          print("the enemy is firing back")
          DamageTaken = EnemyRangedDamage
          SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
          SquadHealth = SquadHealth2
          if SquadHealth <= 0:
            victory = -1
            print("We Have Been Defeated")
          elif SquadHealth > 0:
            print("We are Entering Melee Combat")
            if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
              CombatResult = TotalFMD - EnemyHealth
            elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
              CombatResult = TotalAMD - EnemyHealth
            if CombatResult <= 0:
              victory = 1 
              print("We Have Won we May now take the warspoils and Advance")
            elif CombatResult > 0:
              DamageTaken = EnemyMeleeDamage
              SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
              if SquadHealth <= 0:
                victory = -1
              
              elif SquadHealth > 0:
                print("We are Engaging the Enemy Again")
                if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                  CombatResult = TotalFMD - EnemyHealth
                elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                  CombatResult = TotalAMD - EnemyHealth
                if CombatResult <= 0:
                  victory = 1 
                  print("We Have Won we May now take the warspoils and Advance")
                elif CombatResult > 0:
                  DamageTaken = EnemyMeleeDamage
                  SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                  if (SquadHealth < CombatResult):
                    victory = -1
                  elif (SquadHealth > CombatResult):
                    victory = 1
                    print("The Enemy is shattered and Retreating!")
                    print("We Have Won we May now take the warspoils and Advance")
                    
              
            
            
            
            
      if RangedMissChanceAlly < 4:
        print("We Have Missed our Shots!")
        print("the enemy is firing back")
        DamageTaken = EnemyRangedDamage
        SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
        SquadHealth = SquadHealth2
        if SquadHealth <= 0:
          victory = -1
          print("We Have Been Defeated")
        elif SquadHealth > 0:
          print("We are Entering Melee Combat")
          if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFMD - EnemyHealth
          elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
            CombatResult = TotalAMD - EnemyHealth
          if CombatResult <= 0:
            victory = 1 
            print("We Have Won we May now take the warspoils and Advance")
          elif CombatResult > 0:
            DamageTaken = EnemyMeleeDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
            if SquadHealth <= 0:
              victory = -1

            elif SquadHealth > 0:
              print("We are Engaging the Enemy Again")
              if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                CombatResult = TotalFMD - EnemyHealth
              elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                CombatResult = TotalAMD - EnemyHealth
              if CombatResult <= 0:
                victory = 1 
                print("We Have Won we May now take the warspoils and Advance")
              elif CombatResult > 0:
                DamageTaken = EnemyMeleeDamage
                SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                if (SquadHealth < CombatResult):
                  victory = -1
                elif (SquadHealth > CombatResult):
                  victory = 1
                  print("The Enemy is shattered and Retreating!")
                  print("We Have Won we May now take the warspoils and Advance")
        
    elif (Rangedinitiative <= 2) and (EnemIsranged == 1):
      print("The Enemy Has Initiative for the Ranged Phase")
      DamageTaken = EnemyRangedDamage
      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
      SquadHealth = SquadHealth2
      if SquadHealth <= 0:
        victory = -1
        print("We Have Been Defeated")
      elif SquadHealth > 0:
        print("We are firing back")
        if RangedMissChanceAlly >= 4:
          print("We've hit the enemy")
          if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
              CombatResult = TotalFRD - EnemyHealth
          elif (IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
            CombatResult = TotalARD - EnemyHealth
          if CombatResult <= 0:
            victory = 1
            print("We Have Won we May now take the warspoils and Advance")
          elif CombatResult > 0:
            DamageTaken = EnemyMeleeDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
          if SquadHealth <= 0:
            victory = -1
          
          elif SquadHealth > 0:
            print("We are Engaging the Enemy")
            if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
              CombatResult = TotalFMD - EnemyHealth
            elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
              CombatResult = TotalAMD - EnemyHealth
            if CombatResult <= 0:
              victory = 1 
              print("We Have Won we May now take the warspoils and Advance")
            elif CombatResult > 0:
              DamageTaken = EnemyMeleeDamage
              SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
              if (SquadHealth < CombatResult) or (SquadHealth <= 0):
                victory = -1
              elif (SquadHealth > CombatResult) and (SquadHealth > 0):
                victory = 1
                print("The Enemy is shattered and Retreating!")
                print("We Have Won we May now take the warspoils and Advance")
          
          
          






            if RangedMissChanceAlly < 4:
              print("We Have Missed our Shots!")
              print("the enemy is firing back")
              DamageTaken = EnemyRangedDamage
              SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
              SquadHealth = SquadHealth2
              if SquadHealth <= 0:
                victory = -1
                print("We Have Been Defeated")
              elif SquadHealth > 0:
                print("We are Entering Melee Combat")
                if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                  CombatResult = TotalFMD - EnemyHealth
                elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                  CombatResult = TotalAMD - EnemyHealth
                if CombatResult <= 0:
                  victory = 1 
                  print("We Have Won we May now take the warspoils and Advance")
                elif CombatResult > 0:
                  DamageTaken = EnemyMeleeDamage
                  SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                  if SquadHealth <= 0:
                    victory = -1
  
                  elif SquadHealth > 0:
                    print("We are Engaging the Enemy Again")
                    if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                      CombatResult = TotalFMD - EnemyHealth
                    elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                      CombatResult = TotalAMD - EnemyHealth
                    if CombatResult <= 0:
                      victory = 1 
                      print("We Have Won we May now take the warspoils and Advance")
                    elif CombatResult > 0:
                      DamageTaken = EnemyMeleeDamage
                      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                      if (SquadHealth < CombatResult) or (SquadHealth <= 0):
                        victory = -1
                      elif (SquadHealth > CombatResult) and (SquadHealth > 0):
                        victory = 1
                        print("The Enemy is shattered and Retreating!")
                        print("We Have Won we May now take the warspoils and Advance")
    elif Isranged == (0):
      print("the enemy is firing back")
      DamageTaken = EnemyRangedDamage
      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
      SquadHealth = SquadHealth2
      if SquadHealth <= 0:
        victory = -1
        print("We Have Been Defeated")
      elif SquadHealth > 0:
        print("We are Entering Melee Combat")
        if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
          CombatResult = TotalFMD - EnemyHealth
        elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
          CombatResult = TotalAMD - EnemyHealth
        if CombatResult <= 0:
          victory = 1 
          print("We Have Won we May now take the warspoils and Advance")
        elif CombatResult > 0:
          DamageTaken = EnemyMeleeDamage
          SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
          if SquadHealth <= 0:
            victory = -1

          elif SquadHealth > 0:
            print("We are Engaging the Enemy Again")
            if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
              CombatResult = TotalFMD - EnemyHealth
            elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
              CombatResult = TotalAMD - EnemyHealth
            if CombatResult <= 0:
              victory = 1 
              print("We Have Won we May now take the warspoils and Advance")
            elif CombatResult > 0:
              DamageTaken = EnemyMeleeDamage
              SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
              if (SquadHealth < CombatResult) or (SquadHealth <= 0):
                victory = -1
              elif (SquadHealth > CombatResult) and (SquadHealth > 0):
                victory = 1
                print("The Enemy is shattered and Retreating!")
                print("We Have Won we May now take the warspoils and Advance")
    
    SquadHealth = SquadHealth2
    if victory == -1:
      print("You and your forces have been defeated in combat")
      endgame()
    
    elif victory == 1:
      Warspoils = random.randint(2,23)
      GeldMarks()
      print(f"You and Your Company have {SquadHealth} HealthPoints")
      print(f"""Upon defeating the enemy at hand you find yourself moving deeper into the forest you see a travelling merchant, upon closer inspection you notice that this merchant is a Tiefling.
      The Legends are infact true, here leave other species other than humans.""")
      print("Merchant: Hello Travellers, The Army isn't a very common sight here if i do say so myself, how can i be of service?")
      shop1_1 = input("Do you want to purchase anything (Purchasing is Automatic). Y/N: ")
      shop1_2 = shop1_1.lower()
      if (shop1_2 == "y") or (shop1_2 == "yes"):
        print("Merchant: Very well then travellers, take a look at the prices")
        print("""
        Apple - 20 GeldMarks
        Iberian Ham - 40 GeldMarks
        Bandages - 52 GeldMarks """)
        if GMammount >= 52:
          print("We have Purchased Some Bandages")
          HealthBonus = 50
        elif (GMammount < 52) and (GMammount >= 49):
          print("We have Purchased Some Premium Rations")
          HealthBonus = 30
        elif (GMammount < 49) and (GMammount >= 20):
          print("We have Purchased Some Rations")
          HealthBonus = 20
      elif (shop1_2 == "n") or (shop1_2 == "no"):
        print("Merchant: Such a Shame, Farewell Travellers")
      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
      SquadHealth = SquadHealth2
      HealthBonus = 0
      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
      victory = 0
      print("You and your forces keep following the path, do you decide to go offroad or keep following the path")
      Dir1_2 = str(input("""
      1- Go Offroad
      2- Keep Follwing"""))
      if Dir1_2 == "1":
        print("As you go offroad you and your forces find yourselves getting caught in an elf trap. Your forces couldn't handle the onslaught and you get captured.")
        capending()
        endgame()
      elif Dir1_2 == "2":
        print("As you and your forces keep following the path you find a clearing. Crossing the clearing you spot non other than Jøhlan Soldiers, could they be possibly doing in here?")
        print("You engage them")
        JSoldiers = ["Guards"]
        GuardEnemy = random.choice(JSoldiers)
        Veterancy = random.randint(1,2)
        if Veterancy == 1:
          EnemVeterancy1 = 1
          EnemVeterancy2 = "Rookie"
        elif Veterancy == 2:
          EnemVeterancy1 = 1.8
          EnemVeterancy2 = "Veteran"
        if GuardEnemy == "Guards":
          EnemyMeleeDamage = 50
          EnemyRangedDamage = 0
          EnemyHealth = 100
          IsCav = 0
          IsArmoured = 0
          IsUnarmoured = 1
          RangedMissChance1 = random.randint(0,0)
          EnemIsranged = 0
        
        print(f"You're Attacked by a {EnemVeterancy2} group of {GuardEnemy}")
        EnemyMeleeDamage = EnemyMeleeDamage * EnemVeterancy1
        if (Rangedinitiative >= 3) and (Isranged == 1) or (EnemIsranged == 0):
          print("We Have the Initiative for the Ranged Phase")
          if RangedMissChanceAlly >= 4:
            print("We've hit the enemy")
            if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                CombatResult = TotalFRD - EnemyHealth
            elif (IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
              CombatResult = TotalARD - EnemyHealth
            if CombatResult <= 0:
              print("We Have Won we May now take the warspoils and Advance")
              victory = 1
            elif CombatResult > 0:
                print("We are Entering Melee Combat")
                if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                  CombatResult = TotalFMD - EnemyHealth
                elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                  CombatResult = TotalAMD - EnemyHealth
                if CombatResult <= 0:
                  victory = 1 
                  print("We Have Won we May now take the warspoils and Advance")
                elif CombatResult > 0:
                  DamageTaken = EnemyMeleeDamage
                  SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                  if SquadHealth <= 0:
                    victory = -1

                  elif SquadHealth > 0:
                    print("We are Engaging the Enemy Again")
                    if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                      CombatResult = TotalFMD - EnemyHealth
                    elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                      CombatResult = TotalAMD - EnemyHealth
                    if CombatResult <= 0:
                      victory = 1 
                      print("We Have Won we May now take the warspoils and Advance")
                    elif CombatResult > 0:
                      DamageTaken = EnemyMeleeDamage
                      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                      if (SquadHealth < CombatResult):
                        victory = -1
                      elif (SquadHealth > CombatResult):
                        victory = 1
                        print("The Enemy is shattered and Retreating!")
                        print("We Have Won we May now take the warspoils and Advance")






          if RangedMissChanceAlly < 4:
            print("We Have Missed our Shots!")
            if SquadHealth > 0:
              print("We are Entering Melee Combat")
              if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                CombatResult = TotalFMD - EnemyHealth
              elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                CombatResult = TotalAMD - EnemyHealth
              if CombatResult <= 0:
                victory = 1 
                print("We Have Won we May now take the warspoils and Advance")
              elif CombatResult > 0:
                DamageTaken = EnemyMeleeDamage
                SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                if SquadHealth <= 0:
                  victory = -1

                elif SquadHealth > 0:
                  print("We are Engaging the Enemy Again")
                  if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                    CombatResult = TotalFMD - EnemyHealth
                  elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                    CombatResult = TotalAMD - EnemyHealth
                  if CombatResult <= 0:
                    victory = 1 
                    print("We Have Won we May now take the warspoils and Advance")
                  elif CombatResult > 0:
                    DamageTaken = EnemyMeleeDamage
                    SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                    if (SquadHealth < CombatResult):
                      victory = -1
                    elif (SquadHealth > CombatResult):
                      victory = 1
                      print("The Enemy is shattered and Retreating!")
                      print("We Have Won we May now take the warspoils and Advance")
        
        if victory == -1:
          print("You and your forces have been defeated in combat")
          endgame()
        elif victory == 1:
          print("""\n Upon Defeating the Enemy forces you keep pursuing the retreating forces through the clearing until you find a way out of the forest. After leaving the forest you are greeted with a camp and more guards. You and your company fight bravely the defending force and manage to wound an especially golden clad soldier. 
          Upon closer inspection you notice that it was the king leading a small force, probably to hunt. After wounding the king the forces quickly retreat back to their lines.
          While the effects of this deed wouldn't be immediately noticable, the wounding of the king has caused a retreat en masse of the enemy forces.
          You have won the Battle, and possibly the war.
          
          You're a hero""")
          bestending()
          endgame()
  if Dir1_1 == "2":
    print("""You keep moving fowards, ignoring the path.
    As you mark the path for the main force you and your forces get ambushed by a group of mercenaries""")
  MercType = ["Pikemen","Armoured Swordsmen"]
  MercEnemy1 = random.choice(MercType)
  Veterancy = random.randint(1,2)
  if Veterancy == 1:
    EnemVeterancy1 = 1
    EnemVeterancy2 = "Rookie"
  elif Veterancy == 2:
    EnemVeterancy1 = 1.6
    EnemVeterancy2 = "Veteran"

  if MercType == "Pikemen":
    EnemyMeleeDamage = 59
    EnemyRangedDamage = 0
    EnemyHealth = 40
    IsCav = 0
    IsArmoured = 0
    IsUnarmoured = 1
    RangedMissChance1 = random.randint(0,0)
    EnemIsranged = 0
  elif MercType == "Armoured Swordsmen":
      EnemyMeleeDamage = 58
      EnemyRangedDamage = 0
      EnemyHealth = 70
      IsCav = 0
      IsArmoured = 0
      IsUnarmoured = 1
      RangedMissChance1 = random.randint(0,0)
      EnemIsranged = 0
  print(f"You're Attacked by a {EnemVeterancy2} group of {MercEnemy1}")
  Rangedinitiative = random.randint(1,4)
  EnemyMeleeDamage = EnemyMeleeDamage * Veterancy
  if RangedMissChance1 <= 3:
    EnemyRangedDamage = 0
  elif RangedMissChance1 > 3:
    stataleatorio = 0

  if (Rangedinitiative >= 3) and (Isranged == 1) or (EnemIsranged == 0):
    print("We Have the Initiative for the Ranged Phase")
    if RangedMissChanceAlly >= 4:
      print("We've hit the enemy")
      if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
          CombatResult = TotalFRD - EnemyHealth
      elif (IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
        CombatResult = TotalARD - EnemyHealth
      if CombatResult <= 0:
        print("We Have Won we May now take the warspoils and Advance")
        victory = 1
      elif CombatResult > 0:
        print("the enemy is firing back")
        DamageTaken = EnemyRangedDamage
        SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
        SquadHealth = SquadHealth2
        if SquadHealth <= 0:
          victory = -1
          print("We Have Been Defeated")
        elif SquadHealth > 0:
          print("We are Entering Melee Combat")
          if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFMD - EnemyHealth
          elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
            CombatResult = TotalAMD - EnemyHealth
          if CombatResult <= 0:
            victory = 1 
            print("We Have Won we May now take the warspoils and Advance")
          elif CombatResult > 0:
            DamageTaken = EnemyMeleeDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
            if SquadHealth <= 0:
              victory = -1

            elif SquadHealth > 0:
              print("We are Engaging the Enemy Again")
              if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                CombatResult = TotalFMD - EnemyHealth
              elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                CombatResult = TotalAMD - EnemyHealth
              if CombatResult <= 0:
                victory = 1 
                print("We Have Won we May now take the warspoils and Advance")
              elif CombatResult > 0:
                DamageTaken = EnemyMeleeDamage
                SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                if (SquadHealth < CombatResult):
                  victory = -1
                elif (SquadHealth > CombatResult):
                  victory = 1
                  print("The Enemy is shattered and Retreating!")
                  print("We Have Won we May now take the warspoils and Advance")






    if RangedMissChanceAlly < 4:
      print("We Have Missed our Shots!")
      print("the enemy is firing back")
      DamageTaken = EnemyRangedDamage
      SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
      SquadHealth = SquadHealth2
      if SquadHealth <= 0:
        victory = -1
        print("We Have Been Defeated")
      elif SquadHealth > 0:
        print("We are Entering Melee Combat")
        if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
          CombatResult = TotalFMD - EnemyHealth
        elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
          CombatResult = TotalAMD - EnemyHealth
        if CombatResult <= 0:
          victory = 1 
          print("We Have Won we May now take the warspoils and Advance")
        elif CombatResult > 0:
          DamageTaken = EnemyMeleeDamage
          SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
          if SquadHealth <= 0:
            victory = -1

          elif SquadHealth > 0:
            print("We are Engaging the Enemy Again")
            if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
              CombatResult = TotalFMD - EnemyHealth
            elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
              CombatResult = TotalAMD - EnemyHealth
            if CombatResult <= 0:
              victory = 1 
              print("We Have Won we May now take the warspoils and Advance")
            elif CombatResult > 0:
              DamageTaken = EnemyMeleeDamage
              SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
              if (SquadHealth < CombatResult):
                victory = -1
              elif (SquadHealth > CombatResult):
                victory = 1
                print("The Enemy is shattered and Retreating!")
                print("We Have Won we May now take the warspoils and Advance")

  elif (Rangedinitiative <= 2) and (EnemIsranged == 1):
    print("The Enemy Has Initiative for the Ranged Phase")
    DamageTaken = EnemyRangedDamage
    SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
    SquadHealth = SquadHealth2
    if SquadHealth <= 0:
      victory = -1
      print("We Have Been Defeated")
    elif SquadHealth > 0:
      print("We are firing back")
      if RangedMissChanceAlly >= 4:
        print("We've hit the enemy")
        if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFRD - EnemyHealth
        elif (IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
          CombatResult = TotalARD - EnemyHealth
        if CombatResult <= 0:
          victory = 1
          print("We Have Won we May now take the warspoils and Advance")
        elif CombatResult > 0:
          DamageTaken = EnemyMeleeDamage
          SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
        if SquadHealth <= 0:
          victory = -1

        elif SquadHealth > 0:
          print("We are Engaging the Enemy")
          if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFMD - EnemyHealth
          elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
            CombatResult = TotalAMD - EnemyHealth
          if CombatResult <= 0:
            victory = 1 
            print("We Have Won we May now take the warspoils and Advance")
          elif CombatResult > 0:
            DamageTaken = EnemyMeleeDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
            if (SquadHealth < CombatResult) or (SquadHealth <= 0):
              victory = -1
            elif (SquadHealth > CombatResult) and (SquadHealth > 0):
              victory = 1
              print("The Enemy is shattered and Retreating!")
              print("We Have Won we May now take the warspoils and Advance")









          if RangedMissChanceAlly < 4:
            print("We Have Missed our Shots!")
            print("the enemy is firing back")
            DamageTaken = EnemyRangedDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
            SquadHealth = SquadHealth2
            if SquadHealth <= 0:
              victory = -1
              print("We Have Been Defeated")
            elif SquadHealth > 0:
              print("We are Entering Melee Combat")
              if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                CombatResult = TotalFMD - EnemyHealth
              elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                CombatResult = TotalAMD - EnemyHealth
              if CombatResult <= 0:
                victory = 1 
                print("We Have Won we May now take the warspoils and Advance")
              elif CombatResult > 0:
                DamageTaken = EnemyMeleeDamage
                SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                if SquadHealth <= 0:
                  victory = -1

                elif SquadHealth > 0:
                  print("We are Engaging the Enemy Again")
                  if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
                    CombatResult = TotalFMD - EnemyHealth
                  elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
                    CombatResult = TotalAMD - EnemyHealth
                  if CombatResult <= 0:
                    victory = 1 
                    print("We Have Won we May now take the warspoils and Advance")
                  elif CombatResult > 0:
                    DamageTaken = EnemyMeleeDamage
                    SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
                    if (SquadHealth < CombatResult) or (SquadHealth <= 0):
                      victory = -1
                    elif (SquadHealth > CombatResult) and (SquadHealth > 0):
                      victory = 1
                      print("The Enemy is shattered and Retreating!")
                      print("We Have Won we May now take the warspoils and Advance")
  elif Isranged == (0):
    print("the enemy is firing back")
    DamageTaken = EnemyRangedDamage
    SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
    SquadHealth = SquadHealth2
    if SquadHealth <= 0:
      victory = -1
      print("We Have Been Defeated")
    elif SquadHealth > 0:
      print("We are Entering Melee Combat")
      if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
        CombatResult = TotalFMD - EnemyHealth
      elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
        CombatResult = TotalAMD - EnemyHealth
      if CombatResult <= 0:
        victory = 1 
        print("We Have Won we May now take the warspoils and Advance")
      elif CombatResult > 0:
        DamageTaken = EnemyMeleeDamage
        SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
        if SquadHealth <= 0:
          victory = -1

        elif SquadHealth > 0:
          print("We are Engaging the Enemy Again")
          if (IsCav == 0) and (IsArmoured == 0) and (IsUnarmoured == 1):
            CombatResult = TotalFMD - EnemyHealth
          elif(IsCav == 0) and (IsArmoured == 1) and (IsUnarmoured == 0):
            CombatResult = TotalAMD - EnemyHealth
          if CombatResult <= 0:
            victory = 1 
            print("We Have Won we May now take the warspoils and Advance")
          elif CombatResult > 0:
            DamageTaken = EnemyMeleeDamage
            SquadHealth2 = ((SquadHealth + HealthBonus) - DamageTaken)
            if (SquadHealth < CombatResult) or (SquadHealth <= 0):
              victory = -1
            elif (SquadHealth > CombatResult) and (SquadHealth > 0):
              victory = 1
              print("The Enemy is shattered and Retreating!")
              print("We Have Won we May now take the warspoils and Advance")
  if victory == -1:
    print("You and your forces have been defeated in combat")
    endgame()
  
  elif victory == 1:
    print("Upon your victory you find a map in the pouch of one of the dead bodies, this map marked a safe passage.")
    print("Do you keep Marching fowards and scout ahead")
    Dir2_1 = input("""
    1- Go Back to friendly lines
    2- Keep scouting ahead""")
    if Dir2_1 == "1":
      print("You Have managed to return back to your forces with the mercenary's map. The Vartian soldiers are now moving through the forest and preparing to flank the enemy. Great Job Soldier")
      Goodending()
    elif Dir2_1 == "2":
      print("As you and your forces keep exploring, you are suddenly ambushed by a squad of mercenaries with firearms. Your squad manages to retreat, but you fall in battle.")
      endgame()
