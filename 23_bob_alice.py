def love_meet(alice, bob):
    alice_set   = set(alice)
    bob_set     = set(bob)
    common      = alice_set.intersection(bob_set)
    
    return common


def affair_meet(bob, alice, silvester):
    bob_set         = set(bob)
    alice_set       = set(alice)
    silvester_set   = set(silvester)
    com_ali_sil     = alice_set.intersection(silvester_set)
    diff            = com_ali_sil.difference(bob_set)

    return diff



alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

print(love_meet(alice, bob))
print(affair_meet(bob, alice, silvester))

