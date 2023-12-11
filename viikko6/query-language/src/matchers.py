class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return True
        return False
    
class Or:
    def __init__(self, *matchers):
        self._mathcers = matchers

    def test(self, player):
        matches = 0
        for matcher in self._mathcers:
            if matcher.test(player):
                matches += 1
        if matches == 1:
            return True
        return False
    
class All:
    def __init__(self):
        pass

    def test(self, player):
        return player
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(HasAtLeast(value, attr))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(HasFewerThan(value, attr))
    
    def build(self):
        return self._matcher
    