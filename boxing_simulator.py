from random import randint
'''Hajime no Ippo'''

defensive_success = {
  # measured in percentage of  damage reduction
  "jab": {"shell": 0.5, "philly shell": 1, "head movement": 1, "dempsey roll": 0.5},
  "cross": {"shell": 0.4, "philly shell": 0, "head movement": 0.2, "dempsey roll": 0.2},
  "hook left": {"shell": 0, "philly shell": 0, "head movement": 0.2, "dempsey roll": 0.8},
  "hook right": {"shell": 0, "philly shell": 0, "head movement": 0.2, "dempsey roll": 0.8},
}

class boxer:
  stances = ["orthodox", "southpaw"]
  styles = ["outboxer", "infighter"]


  def __init__(self, name, stance = 0, style = 0, endurance = 2, power = 2): #, technique, adaptability = 1):
    # one from
    self.name = name
    self.stance = self.stances[stance]
    self.style = self.styles[style]
    self.endurance = endurance # level 1 to 3
    self.power = power # level 1 to 3
    # self.adaptability = adaptability # level 1 to 3
    self.cumulative_damage = 0
    self.knocked_down = 0
    self.knocked_out = False

  def __repr__(self):
    description = f"""{self.name} is an {self.style} with {self.endurance} endurance and {self.power} power.""" # From a technical perspective his got {", ".join(self.techniques)} and his capacity of adapting to a fighters style is {self.adaptability}."""
    return description

  def defense(self):
    defense_techniques = ["philly shell", "head movement","shell", "dempsey roll"]
    if self.style == "outboxer":
      defense = defense_techniques[randint(0,1)]
      print(f"{self.name} defends with his {defense}.")
      return defense
    else:
      defense = defense_techniques[randint(2,3)]
      print(f"{self.name} defends with his {defense}.")
      return defense
  
  def attack(self):
      techniques = ["jab", "hook left", "hook right", "cross"]
      attack_idx = randint(0,3)
      attack = techniques[attack_idx]
      print(f"{self.name} attacks with an {attack}.")
      return (attack, attack_idx * self.power)
  
  def fight(self, opponent_boxer): #, gameplan):
    print("\nThe fight starts NOW!")
    fight = True
    i = 1
    while fight:
      print(f"\nThey`re getting to their {i}. exchange.")
      # print(defensive_success[self.attack()[0]])
      # print([opponent_boxer.defense()])
      attack_name, attack_intensity = self.attack()
      damage_inflicted = round(attack_intensity *  (1 - defensive_success[attack_name][opponent_boxer.defense()]), 2)
      print(f"{self.name} just caused {damage_inflicted} damage on his opponent.")
      opponent_boxer.cumulative_damage += damage_inflicted

      if 5 >= damage_inflicted > 4.0:
        opponent_boxer.knocked_down += 1
        print(f"{self.name} just got a knock down!")
      elif (damage_inflicted > 5.0) | (opponent_boxer.cumulative_damage > 8.0):
        opponent_boxer.knocked_out = True

      if opponent_boxer.knocked_out == True | (opponent_boxer.knocked_down == 4):
        return print(f"{self.name} wins the fight with {opponent_boxer.name} via KO."), print(opponent_boxer.cumulative_damage, self.cumulative_damage)
      
      opp_attack_name, opp_attack_intensity = opponent_boxer.attack()
      damage_suffered = round(opp_attack_intensity * (1 - defensive_success[opp_attack_name][self.defense()]), 2)
      print(f"{self.name} just suffered {damage_suffered} damage from his opponent.")
      self.cumulative_damage += damage_suffered

      if 5 >= damage_suffered > 4:
        self.knocked_down += 1
        print(f"{opponent_boxer.name} just got a knock down!")
      elif (damage_suffered > 5) | (self.cumulative_damage > 8):
        self.knocked_out = True

      if self.knocked_out == True | (self.knocked_down == 4):
        return print(f"{self.name} looses the fight to {opponent_boxer.name} via KO"), print(opponent_boxer.cumulative_damage, self.cumulative_damage)
      i += 1



boxer_1 = boxer("Ippo Makanouchi", stance = 0, style = 1, endurance = 2, power = 3)
boxer_2 = boxer("Miyada", stance = 0, style = 0, endurance = 3, power = 2)

print(boxer_1)
print(boxer_2)
boxer_1.fight(boxer_2)