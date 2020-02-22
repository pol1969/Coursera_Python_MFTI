from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):    
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + [__class__.__name__]


class Blessing(AbstractPositive):    
    def get_stats(self):
        stats = self.base.get_stats()
        for key, value in stats.items():
            if len(key) > 3:
                stats[key] = (value+2)
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + [__class__.__name__]


class Weakness(AbstractNegative):    
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + [__class__.__name__]


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        for key, value in stats.items():
            if len(key) > 3:
                stats[key] = (value-2)
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + [__class__.__name__]


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + [__class__.__name__]
