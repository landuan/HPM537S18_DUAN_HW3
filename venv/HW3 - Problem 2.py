class Node:
    """base node"""
    def __init__(self, name, cost, health_utility):
        self.name = name
        self.cost = cost
        self.health_utility = health_utility

    def get_expected_cost(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")
    def get_health_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes")

class ChanceNode(Node):
    def __init__(self, name, cost, future_nodes, probs, health_utility):
        Node.__init__(self, name, cost, health_utility)
        self.future_nodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        exp_cost = self.cost
        i = 0
        for thisNode in self.future_nodes:
            exp_cost += self.probs[i] * thisNode.get_expected_cost()
            i += 1
        return exp_cost

    def get_health_utility(self):
        exp_HU = self.health_utility
        i = 0
        for thisNode in self.future_nodes:
            exp_HU += self.probs[i] * thisNode.get_health_utility()
            i += 1
        return exp_HU

class TerminalNode(Node):
    def __init__(self, name, cost, health_utility):
        Node.__init__(self, name, cost, health_utility)

    def get_expected_cost(self):
        return self.cost

    def get_health_utility(self):
        return self.health_utility

class DecisionNode(Node):
    def __init__(self, name, cost, future_nodes,health_utility):
        Node.__init__(self, name, cost, health_utility)
        self.future_nodes = future_nodes # List of FutureNotes
    def get_expected_cost(self):
        outcomes = dict() # dictionary to store expected cost of future nodes
        for thisNode in self.future_nodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()

        return outcomes

    def get_health_utility(self):
        outcomes1 = dict()
        for thisNode in self.future_nodes:
            outcomes1[thisNode.name] = thisNode.get_health_utility()

        return outcomes1

 # Creating terminal nodes
T1 = TerminalNode("T1", cost=10, health_utility=0.9)
T2 = TerminalNode("T2", cost=20, health_utility=0.8)
T3 = TerminalNode("T3", cost=30, health_utility=0.7)
T4 = TerminalNode("T4", cost=40, health_utility=0.6)
T5 = TerminalNode("T5", cost=50, health_utility=0.5)


# Create C2
C2 = ChanceNode("C2", 35, [T1, T2], probs=[0.7, 0.3],health_utility=0)
# Create C1
C1 = ChanceNode("C1", 25, [C2, T3], probs=[0.2, 0.8],health_utility=0)
# Create C3
C3 = ChanceNode("C3", 45, [T4, T5], probs=[0.1, 0.9],health_utility=0)

# Decision
D1 = DecisionNode("D1", 0, [C1, C3], 0)

print(D1.get_expected_cost())
print(D1.get_health_utility())