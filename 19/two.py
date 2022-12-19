from __future__ import annotations

import re
import bisect

class Recipe:
    def __init__(self, costList) -> None:
        self.id = int(costList[0])

        self.oreBotOre = int(costList[1])
        self.clayBotOre = int(costList[2])

        self.obsidianBotOre = int(costList[3])
        self.obsidianBotClay = int(costList[4])

        self.geodeBotOre = int(costList[5])
        self.geodeBotObsidian = int(costList[6])

class State:

    def __init__(self, recipe: Recipe, other: State=None) -> None:
        self.recipe = recipe

        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geodes = 0

        self.orebots = 1
        self.claybots = 0
        self.obsidianBots = 0
        self.geodeBots = 0
        
        self.timeleft = 32
        self.calcScore()
        if other != None:
            self.ore = other.ore
            self.clay = other.clay
            self.obsidian = other.obsidian
            self.geodes = other.geodes

            self.orebots = other.orebots
            self.claybots = other.claybots
            self.obsidianBots = other.obsidianBots
            self.geodeBots = other.geodeBots

            self.timeleft = other.timeleft
            self.calcScore()

    def tick(self):
        self.timeleft -= 1
        self.ore += self.orebots
        self.clay += self.claybots
        self.obsidian += self.obsidianBots
        self.geodes += self.geodeBots
        self.calcScore()
        
    def calcScore(self):
        self.score = -(
            self.orebots * self.recipe.oreBotOre + self.claybots * self.recipe.clayBotOre + self.obsidianBots * self.recipe.obsidianBotOre + self.geodeBots * self.recipe.geodeBotOre + self.ore
            + (self.obsidianBots * self.recipe.obsidianBotClay + self.clay) * 1000
            + (self.geodeBots * self.recipe.geodeBotObsidian + self.obsidian) * 1000000
            + self.geodes * 1000000000
        )

def addToQueue(queue: list[State], state: State):
    bisect.insort(queue, state, key=lambda a: a.score)
    
product = 1
def inspectRecipe(recipe: Recipe):
    global product
    sample = 0
    best = 0
    queue = [State(recipe)]
    while len(queue) > 0:
        nextMinuteQueue = []
        while len(queue) > 0:
            next = queue.pop(0)
            #if sample % 1000 == 0:
            #    print('step', sample, next.timeleft, len(queue)+1)
            sample += 1
            if next.timeleft > 0:
                advanced = State(recipe, next)
                advanced.tick()
                addToQueue(nextMinuteQueue, advanced)
                if next.ore >= recipe.geodeBotOre and next.obsidian >= recipe.geodeBotObsidian:
                    buildGeodeBot = State(recipe, advanced)
                    buildGeodeBot.ore -= recipe.geodeBotOre
                    buildGeodeBot.obsidian -= recipe.geodeBotObsidian
                    buildGeodeBot.geodeBots += 1
                    buildGeodeBot.calcScore()
                    addToQueue(nextMinuteQueue, buildGeodeBot)
                if next.ore >= recipe.obsidianBotOre and next.clay >= recipe.obsidianBotClay:
                    buildObsidianBot = State(recipe, advanced)
                    buildObsidianBot.ore -= recipe.obsidianBotOre
                    buildObsidianBot.clay -= recipe.obsidianBotClay
                    buildObsidianBot.obsidianBots += 1
                    buildObsidianBot.calcScore()
                    addToQueue(nextMinuteQueue, buildObsidianBot)
                if next.ore >= recipe.clayBotOre:
                    buildClayBot = State(recipe, advanced)
                    buildClayBot.ore -= recipe.clayBotOre
                    buildClayBot.claybots += 1
                    buildClayBot.calcScore()
                    addToQueue(nextMinuteQueue, buildClayBot)
                if next.ore >= recipe.oreBotOre:
                    buildOreBot = State(recipe, advanced)
                    buildOreBot.ore -= recipe.oreBotOre
                    buildOreBot.orebots += 1
                    buildOreBot.calcScore()
                    addToQueue(nextMinuteQueue, buildOreBot)
            else:
                best = max(best, next.geodes)                
        queue = nextMinuteQueue[0:50000] # can't quite guarantee that higher score states will lead to the best result, so we keep a couple to continue with, needed more since there are more iteration steps
    product *= best
    print('result', recipe.id, best, product)        

recipes: list[Recipe] = []

expression = re.compile('Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.')

num = 0
with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        matched = expression.match(line)
        recipes.append(Recipe(matched.groups()))
        num += 1
        if num == 3:
            break

for recipe in recipes:
    inspectRecipe(recipe)
