import random
import json
from data2 import nouns,nounsEs,adjectives,adjectivesEs

def random_prefix(data,dataEs):
    prefixIndex=random.randint(0, len(data) - 1)
    prefix=f"{data[prefixIndex]}"
    prefixEs=f"{dataEs[prefixIndex]}"
    return prefix,prefixEs

def random_adjective(data,dataEs):
    adjIndex = random.randint(0, len(data) - 1)
    adj = f"{data[adjIndex]}"
    adjEs = f"{dataEs[adjIndex]}"
    return adj.capitalize(), adjEs.capitalize()

def create_unique_nickname(user_list, prefixes_data,prefixes_dataEs, adjectives_data,adjectives_dataEs):
    prefix,prefixEs = random_prefix(prefixes_data,prefixes_dataEs)
    adjective,adjectiveEs = random_adjective(adjectives_data,adjectives_dataEs)
    nickname = f"{prefix} {adjective}"
    nicknameEs = f"{prefixEs} {adjectiveEs}"
    if nickname in user_list: # to ensure no duplicate nicknames
        create_unique_nickname(user_list, prefixes_data,prefixes_dataEs, adjectives_data,adjectives_dataEs)
    else:
        return nickname,nicknameEs

prefixes_data = nouns
adjectives_data=adjectives
prefixes_dataEs = nounsEs
adjectives_dataEs=adjectivesEs

# Ejemplo de uso
user_list = ["John", "Jane", "Mike"]

# Generar 5 nicks aleatorios
for _ in range(5):
    unique_nickname,unique_nicknameEs = create_unique_nickname(user_list, prefixes_data,prefixes_dataEs, adjectives_data,adjectives_dataEs)
    print(f"Unique nickname: {unique_nickname} ({unique_nicknameEs})")


