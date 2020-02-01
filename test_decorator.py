# =============================================================================
# Скрипт для тестирования решений студентов по заданию "Создание декоратора
# класса" (тесты содержат примеры, приведенные в описании задания)
# https://stepik.org/lesson/106937/step/4?unit=81460
# Скопируйте код вашего решения в секцию ВАШ КОД и запустите скрипт
# =============================================================================
from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


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
        self.stats = self.base.stats.copy()
        self._add()
        return self.stats.copy()
    
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

if __name__ == '__main__':
    # создадим героя
    hero = Hero()
#    import pdb;pdb.set_trace()
    # проверим правильность характеристик по-умолчанию
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    # проверим список отрицательных эффектов
    assert hero.get_negative_effects() == []
    # проверим список положительных эффектов
    assert hero.get_positive_effects() == []
    #breakpoint()
    # наложим эффект Berserk
    brs1 = Berserk(hero)
    # проверим правильность изменения характеристик
    assert brs1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 22,
                                'Perception': 1,
                                'Endurance': 15,
                                'Charisma': -1,
                                'Intelligence': 0,
                                'Agility': 15,
                                'Luck': 8}
    # проверим неизменность списка отрицательных эффектов
    
    assert brs1.get_negative_effects() == []
    # проверим, что в список положительных эффектов был добавлен Berserk
    assert brs1.get_positive_effects() == ['Berserk']
    # повторное наложение эффекта Berserk
    
#    import pdb;pdb.set_trace()
    brs2 = Berserk(brs1)
    # наложение эффекта Curse
    cur1 = Curse(brs2)
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 228,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 27,
                                'Perception': -4,
                                'Endurance': 20,
                                'Charisma': -6,
                                'Intelligence': -5,
                                'Agility': 20,
                                'Luck': 13}
    # проверим правильность добавления эффектов в список положительных эффектов
    #breakpoint()
    assert cur1.get_positive_effects() == ['Berserk', 'Berserk']
    # проверим правильность добавления эффектов в список отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # снятие эффекта Berserk
    cur1.base = brs1
#    breakpoint()
    # проверим правильность изменения характеристик
    assert cur1.get_stats() == {'HP': 178,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 20,
                                'Perception': -1,
                                'Endurance': 13,
                                'Charisma': -3,
                                'Intelligence': -2,
                                'Agility': 13,
                                'Luck': 6}
    # проверим правильность удаления эффектов из списка положительных эффектов
 #   breakpoint()
    assert cur1.get_positive_effects() == ['Berserk']
    # проверим правильность эффектов в списке отрицательных эффектов
    assert cur1.get_negative_effects() == ['Curse']
    # проверим незменность характеристик у объекта hero
    assert hero.get_stats() == {'HP': 128,
                                'MP': 42,
                                'SP': 100,
                                'Strength': 15,
                                'Perception': 4,
                                'Endurance': 8,
                                'Charisma': 2,
                                'Intelligence': 3,
                                'Agility': 8,
                                'Luck': 1}
    print('All tests - OK!')
