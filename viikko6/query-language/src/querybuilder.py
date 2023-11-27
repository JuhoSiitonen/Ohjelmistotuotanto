from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

class QueryBuilder:
    def __init__(self, *matcher):
        #print(type(matcher))
        
        self.matcher = matcher
        #self.matchers = self.matcher + matcher

    def playsIn(self, team):
        return QueryBuilder(*self.matcher, PlaysIn(team))

    def hasAtLeast(self, limit, ops):
        return QueryBuilder(*self.matcher, HasAtLeast(limit, ops))

    def hasFewerThan(self, limit, ops):
        return QueryBuilder(*self.matcher, HasFewerThan(limit, ops))

    def build(self):
        #print(self.matcher)
        #self.matcher = self.matcher[1:]
        return And(*self.matcher)
    
    def oneOf(self, *objs):
        self.matcher = objs
        return Or(*objs)