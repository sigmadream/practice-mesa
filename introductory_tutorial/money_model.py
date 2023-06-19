import mesa


class MoneyAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1


class MoneyModel(mesa.Model):
    def __int__(self, N):
        self.num_agents = N
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
