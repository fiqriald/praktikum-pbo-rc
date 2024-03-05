import random

class Robot:
    def __init__(self, name, attack_power, max_hp):
        self.name = name
        self.attack_power = attack_power
        self.max_hp = max_hp
        self.hp = max_hp

    def attack_enemy(self, enemy):
        # Menggunakan fungsi random untuk menentukan apakah serangan berhasil atau tidak
        print(f"{self.name} menyerang {enemy.name}!")
        if random.random() < 0.1:  # 10% chance to miss
            print("Serangannya meleset!")
        else:
            enemy.take_damage(self.attack_power)

    def take_damage(self, damage):
        # Mengurangi HP sesuai dengan jumlah damage yang diterima
        self.hp -= damage
        print(f"{self.name} menerima {damage} damage.")
        if self.hp <= 0:
            print(f"{self.name} kalah!")
        else:
            print(f"Sisa HP {self.name}: {self.hp}")

    def regen_health(self):
        # Meregenerasi sebagian HP secara acak
        regen_amount = random.randint(10, 20)
        self.hp = min(self.max_hp, self.hp + regen_amount)
        print(f"{self.name} berhasil meregenerasi {regen_amount} HP. Total HP sekarang: {self.hp}")


class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.rounds = 0

    def start_game(self):
        print("Pertempuran dimulai!")
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            self.rounds += 1
            print(f"\nRound {self.rounds}:")
            # Robot 1 menyerang Robot 2
            self.robot1.attack_enemy(self.robot2)
            if self.robot2.hp <= 0:
                break
            # Robot 2 menyerang Robot 1
            self.robot2.attack_enemy(self.robot1)
        print("\nPertempuran selesai!")

# Membuat robot
robot1 = Robot("Robot A", 20, 100)
robot2 = Robot("Robot B", 15, 120)

# Membuat permainan
game = Game(robot1, robot2)

# Memulai permainan
game.start_game()
