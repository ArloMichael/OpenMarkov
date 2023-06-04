import json
import random
from collections import defaultdict

class Chain:
    def __init__(self, order=1, clean=False):
        self.order = order
        self.transitions = defaultdict(list)
        self.clean = clean
    
    def tokenize(self, text):
        return text.split()
    
    def fix(self, text):
        if self.clean:
            return text.lower()
        else:
            return text
    
    def train(self, text):
        tokens = self.tokenize(self.fix(text))
        
        if len(tokens) <= self.order:
            raise ValueError("Text is too short for the given order")
        
        for i in range(len(tokens) - self.order):
            prefix = tuple(tokens[i:i+self.order])
            suffix = tokens[i+self.order]
            self.transitions[prefix].append(suffix)
    
    def generate(self, length=10, seed=None):
        if seed is None:
            seed = random.choice(list(self.transitions.keys()))
        else:
            seed = self.tokenize(self.fix(seed))

        generated_text = list(seed)
        
        while len(generated_text) < length:
            prefix = tuple(generated_text[-self.order:])
            
            if prefix not in self.transitions:
                break
            
            next_word = random.choice(self.transitions[prefix])
            generated_text.append(next_word)
        
        return " ".join(generated_text)

    def save(self, filename):
        data = {
            'order': self.order,
            'transitions': {
                'keys': [list(key) for key in self.transitions.keys()],
                'values': list(self.transitions.values())
            },
            'clean': self.clean
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        
    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        
        chain = cls(order=data['order'], clean=data['clean'])
        chain.transitions = defaultdict(list)
        keys = [tuple(key) for key in data['transitions']['keys']]
        values = data['transitions']['values']
        chain.transitions.update(zip(keys, values))
        
        return chain