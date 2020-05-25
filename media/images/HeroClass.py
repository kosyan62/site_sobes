from abc import ABC, abstractmethod


# class Hero:
#     def __init__(self):
#         self.positive_effects = []
#         self.negative_effects = []
#         self.stats = {
#             "HP": 128,  # health points
#             "MP": 42,  # magic points,
#             "SP": 100,  # skill points
#             "Strength": 15,  # сила
#             "Perception": 4,  # восприятие
#             "Endurance": 8,  # выносливость
#             "Charisma": 2,  # харизма
#             "Intelligence": 3,  # интеллект
#             "Agility": 8,  # ловкость
#             "Luck": 1  # удача
#         }
#
    # def get_positive_effects(self):
    #     return self.positive_effects.copy()
    #
    # def get_negative_effects(self):
    #     return self.negative_effects.copy()
    #
    # def get_stats(self):
    #     return self.stats.copy()
    #
    #
class AbstractEffect(ABC, Hero):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass

class AbstractNegative(AbstractEffect):

    @abstractmethod
    def get_stats(self):
        pass

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    @abstractmethod
    def get_negative_effects(self):
        pass


class AbstractPositive(AbstractEffect):

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def get_positive_effects(self):
        pass

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        stats['HP'] += 50
        return stats

    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Berserk')
        return effects


class Blessing(AbstractPositive):
    def get_stats(self):
        main_stats = ['HP', 'MP', 'SP']
        stats = {key: value if key in main_stats else value + 2 for key, value in self.base.get_stats().items()}
        return stats

    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Blessing')
        return effects


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        ch = ['Strength', 'Endurance', 'Agility']
        for i in ch:
            stats[i] -= 4
        return stats

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Weakness')
        return effects


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('EvilEye')
        return effects


class Curse(AbstractNegative):
    def get_stats(self):
        main_stats = ['HP', 'MP', 'SP']
        stats = {key: value if key in main_stats else value - 2 for key, value in self.base.get_stats().items()}
        return stats

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Curse')
        return effects

# hero = Hero()
# print(hero.get_stats())
# # berserk1 = Berserk(hero)
# # print(berserk1.get_stats())
# # berserk2 = Berserk(berserk1)
# # print(berserk2.get_stats())
# curse = Blessing(hero)
# print(curse.get_stats())
