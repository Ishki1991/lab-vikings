
# Soldier


class Soldier:
    def __init__(self,healt,strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage



# Viking

class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(healt, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


    def battleCry(self):
        return "Odin Owns You All!"

class Viking:
    pass



# Saxon


class Saxon:
    def __init__(self, health, strength):
        super().__init__(health, strength)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War:
    pass
