"""
Créé par Philippe Coutu
groupe 406
24 janvier 2023
"""
import math
import random
from dataclasses import dataclass


class StringFoo:
    def __init__(self, message):
        self.message = message

    def set_string(self, message):
        self.message = message

    def print_string(self):
        print(self.message)


class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self):
        return self.longueur * self.largeur

    def afficher_infos(self):
        print(self.largeur, self.longueur, self.calcul_aire())


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def calcul_aire(self):
        return self.rayon ** 2 * math.pi

    def calcul_circonference(self):
        return self.rayon * 2 * math.pi


class Hero:
    def __init__(self, vie, force_attaque, force_defence, name):
        self.vie = vie
        self.force_attaque = force_attaque
        self.force_defence = force_defence
        self.name = name

    def est_vivant(self):
        return self.vie > 0

    def attaque(self):
        return random.randint(0, 6)

    def dommage(self, nb_dommage):
        self.vie -= nb_dommage - self.force_defence


@dataclass
class Monstre:
    force: int = random.randint(0, 20)
    dexterite: int = random.randint(0, 20)
    constitution: int = random.randint(0, 20)
    intelligence: int = random.randint(0, 20)
    sagesse: int = random.randint(0, 20)
    charisme: int = random.randint(0, 20)


@dataclass
class Monstre:
    name: str
    force: int = random.randint(0, 20)
    dexterite: int = random.randint(0, 20)
    constitution: int = random.randint(0, 20)
    intelligence: int = random.randint(0, 20)
    sagesse: int = random.randint(0, 20)
    charisme: int = random.randint(0, 20)
