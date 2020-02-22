from test_decorator import Hero

from abc import ABC, abstractmethod
# =============================================================================
# начало секции ВАШ КОД
# =============================================================================
# Поместите в этой секции реализацию классов AbstractEffect, AbstractPositive,
# AbstractNegative, Berserk, Blessing, Curse, EvilEye, Weakness из вашего
# решения
# =============================================================================

class AbstractEffect(ABC, Hero):
    @abstractmethod
    def __init__(self, base):
        self.base = base
        self.positive_effects = \
                self.base.get_positive_effects()
        self.negative_effects = \
                self.base.get_negative_effects()
        self.stats = self.base.stats.copy()
 
    def get_stats(self):
        self.stats = self.base.stats
        self._add()
        return self.stats
    
    @abstractmethod
    def _add(self):
        pass


class AbstractPositive(AbstractEffect):
    
    def get_positive_effects(self):
        self.positive_effects = \
                self.base.positive_effects.copy()
        self.positive_effects.append(self.name)
        return self.positive_effects.copy()

    def get_negative_effects(self):
        self.negative_effects = \
                self.base.negative_effects.copy()
        return self.negative_effects.copy()


class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        self.negative_effects =\
                self.base.negative_effects.copy()
        self.negative_effects.append(self.name)
        return self.negative_effects.copy()

    def get_positive_effects(self):
        self.positive_effects = \
                self.base.positive_effects.copy()
        return self.positive_effects.copy() 



class Berserk(AbstractPositive):
    def __init__(self, base):
        AbstractPositive.__init__(self,base)
        self.name = __class__.__name__
        self.positive_effects.append(self.name)
        self._add()

    def _add(self):  
        self.stats["Strength"] += 7
        self.stats["Endurance"] += 7
        self.stats["Agility"] += 7
        self.stats["Luck"] += 7
        self.stats["Perception"] -= 3
        self.stats["Charisma"] -= 3
        self.stats["Intelligence"] -= 3
        self.stats["HP"] += 50


class Blessing(AbstractPositive):
    def __init__(self, base):
        AbstractPositive.__init__(self,base)
        self.name = __class__.__name__
        self.positive_effects.append(self.name)
        self._add()

    def _add(self):
       for key, value in self.stats.items():
            if len(key) > 3:
                self.stats[key] = (value+2)


class Weakness(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self,base)
        self.name = __class__.__name__
        self.negative_effects.append(self.name)
        self._add()

    def _add(self):
        self.stats["Strength"] -= 4
        self.stats["Endurance"] -= 4
        self.stats["Agility"] -= 4



class EvilEye(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self,base)
        self.name = __class__.__name__
        self.negative_effects.append(self.name)
        self._add()

    def _add(self):
        self.stats["Luck"] -= 10


 
class Curse(AbstractNegative):
    def __init__(self, base):
        AbstractNegative.__init__(self,base)
        self.name = __class__.__name__
        self.negative_effects.append(self.name)
        self._add()

    def _add(self):
        for key, value in self.stats.items():
            if len(key) > 3:
                self.stats[key] = (value-2)





# конец секции ВАШ КОД
# =============================================================================


