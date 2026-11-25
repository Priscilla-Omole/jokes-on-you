import pyjokes
import random

def call_joke():
    jokes = pyjokes.get_jokes()
    return random.choice(jokes)