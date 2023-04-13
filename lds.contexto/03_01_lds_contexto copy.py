import spacy
import random
from numpy import dot
from numpy.linalg import norm
from gensim.models import Word2Vec

nlp = spacy.load("en_core_web_sm")

print("Welcome to LDS.Contexto! Here's how the game works: Find the secret word. You have unlimited guesses. The words are sorted by an artificial intelligence algorithm according to how similar they are to the secret word. After submitting a word, you will see its position. The secret word is number 0. The algorithm analyzed over 4,000 general conference talks. It uses the context in which words are used to calculate the similarity between them. Good luck!")

target_words =["endowment", "gospel", "faith", "ordinance", "baptism", "atonement", "priesthood", "bible", "mormon", "agency", "proxy", "bishop", "prophet", "celestial", "heaven", "hell", "satan", "cross", "godhead", "gratitude", "christmas", "humble", "miracle", "peace", "polygamy", "sacrament", "spirit", "commandments", "tithing", "authority", "blessing", "christian", "church", "calling", "doctrine", "creation", "mortality", "charity", "faith", "hope", "repentance", "conversion", "mission", "missionary", "doctrine", "disciple", "easter", "endure", "fall", "jesus", "joy", "happiness", "knowledge", "language", "light", "love", "mercy", "mortality", "patience", "prayer", "pride", "prompting", "restoration", "vision", "redemption", "resurrection", "sabbath", "sunday", "sacrifice", "scriptures", "sealing", "sin", "talent", "temple", "testimony"]
random_index = random.randrange(len(target_words))

def get_rank_dict(target_word, model):
    '''this function will loop through each word vector in the word2vec.model file and process the cosine similarity against the vector of the target word. they are stored into ranks according to their similarity to the target word (with the target word being first or index [0]'''
    ranks = []
    
    for word in model.wv.index_to_key:
        a = model.wv[word]
        b = model.wv[target_word]
        cos_sim = dot(a, b)/(norm(a)*norm(b))
        ranks.append((word, cos_sim)) 
    ranks = sorted(ranks, reverse=True, key=lambda x:x[1])
    rank_dict = {}

    for i, (word, cos_sim) in enumerate(ranks):
        rank_dict[word] = i 
    return rank_dict

# model = Word2Vec.load("word2vec.model")
# output = get_rank_dict("jesus", model)
# rank = dict(list(output.items())[0:51])
# print(rank)

def check_the_guess(target_word):
    '''this function puts everything together. it processes the guesses and outputs the guess (and past guesses) with the rank aka how close the guess is to the target word.'''
    guesses = []
    model = Word2Vec.load("word2vec.model")
    rank_dict = get_rank_dict(target_word, model)

    while True: # infinite while loop
        guessed_word = input("Guess a word: ").lower() # these next few lines process the guessed word (lowercase and lemmatize it)
        guessed_word = nlp(guessed_word)[0]
        guessed_word = guessed_word.lemma_
        try:
            guessed_rank = rank_dict[guessed_word]
        except KeyError: 
            print("Sorry, that word is either not in our General Conference corpus or may be misspelled. Go again.")
            continue

        guesses.append((guessed_word, guessed_rank))
        past_guesses = list(set(guesses))
        for word, rank in sorted(past_guesses, reverse=True, key=lambda x: x[1]):
            print('\u2588' * int(((len(rank_dict)-rank)/len(rank_dict)) * 79), word, rank) # ADD NUMER OF HOW MANY BLOCKS I WANT (RN: 30)

        if guessed_word == target_word:
            print("Congratulations! You guessed the word!")
            break
        else:
            print('Your guess:')
            print('\u2588' * int(((len(rank_dict)-guessed_rank)/len(rank_dict)) * 79), guessed_word, guessed_rank)
            print("Nice try! Go again.")

check_the_guess(target_words[random_index])
