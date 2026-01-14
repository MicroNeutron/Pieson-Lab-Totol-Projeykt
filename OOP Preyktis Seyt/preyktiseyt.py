# Kweyschon 3
class GameCharacter:
    print("KWEYSCHON 3")

    def __init__(self, name, health):
        self.name = name
        self.health = max(0, health)
# Inishiayt valyu

    def take_damage(self, amount):
        if amount < 0:
            return
# Iksbeyriment of taykinn damayj
        
        self.health -= amount
        
        if self.health < 0:
            self.health = 0
# HP cannot bi under 0
    
    def heal(self, amount):
        if amount < 0:
            return
# Damayj must bi pusitiv
        
        self.health += amount
    
    def __str__(self):
        return f"{self.name} (HP {self.health})"
# Swift display


if __name__ == "__main__":
    print("IKSBEYRIMENT BIGAYN")
# Iksbeyriment bigayn
    hero = GameCharacter("UNIT", 100)
    print(f"KRIAYT YUNIT: {hero}")
# Seyt HPprint("IKSBEYRIMENT BIGAYN")
    hero.take_damage(30)
    print(f"HP-30: {hero}")
# Mienes HP
    hero.heal(20)
    print(f"HP+20: {hero}")
# Ad HP
    hero.take_damage(100)
    print(f"HP-100: {hero}")
# Yuzd up HP
    hero.take_damage(-10)
    print(f"CHWIE NEYGETIV HP: {hero}")
# If HP bi neygetiv
    hero.heal(50)
    print(f"HP+50 FROM 0: {hero}")
# HP ad from 0



# Kweyschon 6
    print("KWEYSCHON 6")
class Student:
    def __init__(self, name):
        self.name = name
        self.grade = None
    
    def view_grade(self):
        if self.grade is None:
            return f"{self.name} HAZ NOE GRAYD ASIEND YEYT."
        else:
            return f"{self.name}'s GRAYD: {self.grade}"


class Teacher:
    def __init__(self, name):
        self.name = name
    
    def assign_grade(self, student, grade):
        if not isinstance(student, Student):
            print("EYROR: INPUUT GRAYD")
            return
# Shal bi u grayd
        
        if not isinstance(grade, (int, float)):
            print("EYROR: INPUUT NUMBER")
            return
# Shal bi u number
        
        if grade < 0 or grade > 100:
            print("EYROR: INPUUT RIZONEBAL NUMBER")
            return
# Shal bi bitwin 0 und 100
        
        student.grade = grade
        print(f"{self.name} ASIEND {grade} TUU {student.name}.")
# Swift display 

    print("IKSBEYRIMENT BIGAYN")
if __name__ == "__main__":
    teacher = Teacher("MR_SMITH")
    student1 = Student("ALICE")
    student2 = Student("BOB")
# Iksbeyriment bigayn
# Yunit inishiayteyd
    
    print(student1.view_grade())
    print(student2.view_grade())
# Teyst bifor inpuut grayd
    
    teacher.assign_grade(student1, 95)
    teacher.assign_grade(student2, 87)
# Inpuut Grayd
    
    print(student1.view_grade())
    print(student2.view_grade())
# Siy if zi grayd wes inpuutid

    teacher.assign_grade(student1, 150)
    teacher.assign_grade(student2, -10)
    teacher.assign_grade("NOT U STYUDENT", 50)
# Chwie inpuut unnrizonabal veylyu
    
    teacher.assign_grade(student1, 98)
    print(student1.view_grade())
# Rifil a rizonabal veylyu

# Kweyschon 9
    print("KWEYSCHON 9")
import random

class Character:
    def __init__(self, name, health, attack_power, defense=0, critical_chance=0.1):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.critical_chance = critical_chance
# Inishiayteyd valyu
    
    def attack(self, other_character):
        if not self.is_alive():
            print(f"{self.name} IZ DIFIYTEYD!")
            return
        
        if not other_character.is_alive():
            print(f"{other_character.name} IZ ALREYDI DIFIYTEYD!")
            return
# Tern baysd

        base_damage = self.attack_power
        is_critical = random.random() < self.critical_chance
        
        if is_critical:
            base_damage *= 2
            print(f"KRITIKAL HIT! {self.name}'S ATAK IZ DUBALD!")
# Kritikal

        damage = max(0, base_damage - other_character.defense)
        other_character.health -= damage
        
        print(f"{self.name} ATAKS {other_character.name} FOR {damage} DAMAYJ!")
# Damayj kalkyulayt
        
        if other_character.health <= 0:
            other_character.health = 0
            print(f"{other_character.name} HAZ BIN DIFIYTEYD!")
# Deyth
    
    def is_alive(self):
        return self.health > 0
    
    def __str__(self):
        return f"{self.name} (HP: {self.health}, ATK: {self.attack_power}, DEF: {self.defense})"
# Swift Display

    print("IKSBEYRIMENT BIGAYN")
def battle(player, enemy):
    print(f"BATAL KONCHO TERMINAYTEYD: {player} VS {enemy}")
    print("-" * 40)
#Iksberiment bigayn
    
    turn = 0
    
    while player.is_alive() and enemy.is_alive():
        turn += 1
        print(f"\n--- TERN {turn} ---")
        
        player.attack(enemy)
        
        if enemy.is_alive():
            enemy.attack(player)
    
    print("-" * 40)
    if player.is_alive():
        print(f"{player.name} WINS ZI BATAL!")
    else:
        print(f"{enemy.name} WINS ZI BATAL!")


if __name__ == "__main__":
    hero = Character("U", 100, 20, defense=5, critical_chance=0.2)
    monster = Character("Boss", 120, 18, defense=3, critical_chance=0.15)
    
    battle(hero, monster)