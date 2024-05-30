from collections import defaultdict

class Road:
    def __init__(self, name, length, mainWidth, sideWidth, roadFace) -> None:
        self.data = {
            'name':name,
            'length':length,
            'mainWidth':mainWidth,
            'sideWidth':sideWidth,
            'roadFace':roadFace
        }
        self.cost = {
            'liqing':1600,
            'shuini':400,
            'suishi':500,
            'worker':300,
            'wajueji':1500,
            'truck':800
        }
        self.budget = {}

    def setCost(self, name, cost):
        self.cost[name] = cost

    def getCost(self, name):
        print(self.cost.get(name, 'undefined'))

    def roadBudget(self, high, material):
        if material not in ('liqing', 'shuini'):
            tiji = self.data['length'] * (self.data['mainWidth'] + self.data['sideWidth'] * 2) * high
        else:
            tiji = self.data['length'] * self.data['mainWidth'] * high
        cost = tiji * self.cost.get(material, 0)
        self.budget[material] = round(cost, 2)

    def workerBudget(self, n):
        cost = self.cost['worker'] * n
        self.budget['worker'] = cost

    def machineBudget(self, name, n):
        cost = self.cost[name] * n
        self.budget[name] = cost

    def summaryCost(self):
        total = sum(self.budget.values())
        self.budget['total'] = total

    def showSummary(self):
        print(self.data['name'])
        for k, v in self.budget.items():
            print(k, v, sep=' : ')




if __name__ == '__main__':
    road = Road('XuTuanLu', 1000, 6, 1, 'liqing')
    road.getCost('truck')