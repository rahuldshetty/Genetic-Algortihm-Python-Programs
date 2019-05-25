import datetime
import random

target = input('Enter text to guess:')

random.seed()
startTime = datetime.datetime.now()

geneSet = "abcdefghijklmnopqrstuvwxyz"
geneSet += geneSet.upper()
geneSet += " .!"


def gen_parent(length):
    genes = []
    while len(genes) < length:
        sampleSize = min(length-len(genes),len(geneSet))
        genes.extend(random.sample(geneSet,sampleSize))
    return ''.join(genes)

def get_fitness(guess):
    return sum(1 for i in range(len(guess)) if guess[i]==target[i])

def mutate(parent):
    index = random.randrange(0,len(parent))
    childGenes = list(parent)
    newGene , alternate = random.sample(geneSet,2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    return ''.join(childGenes)

def display(guess):
    timeDiff = datetime.datetime.now() - startTime
    fitness = get_fitness(guess)
    print("{}\t{}\t{}.".format(guess,fitness,timeDiff))

bestParent = gen_parent(len(target))
bestFitness = get_fitness(bestParent)
display(bestParent)

while True:
    child = mutate(bestParent)
    childFitness = get_fitness(child)
    if bestFitness >= childFitness:
        continue 
    display(child)
    if childFitness >= len(bestParent):
        break
    bestFitness = childFitness
    bestParent = child