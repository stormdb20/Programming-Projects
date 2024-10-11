import random

verbs = ['leverage', 'sync', 'target', '24/7']

adjectives = ['Hyperlocal', 'Siloed', 'oriented', 'api-based']

nouns = ['process', 'productivity', 'paradigm', 'pipeline']

verb = random.choice(verbs)

adjective = random.choice(adjectives)

noun = random.choice(nouns)

phrase = verb + ' ' + adjective + ' ' + noun

print(phrase)
