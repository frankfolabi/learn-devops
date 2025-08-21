spike = {
    'owner' :'chris',
    'kind' : 'eskimo',
    }

blac = {
    'owner' : 'rey',
    'kind' : 'eskimo',
    }
rocky = {
    'owner' : 'tim',
    'kind' : 'aus'
}

pets = [spike, blac, rocky]

for pet in pets:
    owner = (pet['owner'])
    kind = (pet['kind'])
    print(f"{owner.title()} owns an {kind.title()} dog.")
    
