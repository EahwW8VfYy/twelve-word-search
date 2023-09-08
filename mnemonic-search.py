# find a Bitcoin wallet from all 12-word combinations

# libraries

# https://github.com/meherett/python-hdwallet
from hdwallet import BIP44HDWallet
from hdwallet.symbols import BTC as SYMBOL
from hdwallet.utils import generate_mnemonic, is_mnemonic

import json
import random
import time

# search wallet attributes (just a test wallet)
# change these to what you are searching for
# this should be done offline if it's a real wallet
wallet_words = ['open', 'olympic', 'income', 'zebra', 'casual', 'asthma', 'tell', 'enable', 'punch', 'reflect', 'jaguar', 'steak']
wallet_xpub = 'xpub661MyMwAqRbcGFoQNuN4CZpAVpR4BH8BpH9gfzhP8yYRecjxRZLt8vbWz6tBsGt3VMYbYB1uVaRivtxMcoUDZri3WJG3C6PfyzwVWhZ3Q77'

# randomize wallet_words for the hunt
# this line can be commented out for a real search
random.shuffle(wallet_words)

# counter
global counter
counter = 0

# start time
start = time.time()

def all_mnemonics(word_list, n, _accum=[]):
    if len(_accum) == n:
        
        global counter
        counter += 1

        MNEMONIC = " ".join(_accum)
        
        # # testing - uncomment this to simulate successful find at counter value
        # if (counter == 100000):
        #     MNEMONIC = " ".join(['open', 'olympic', 'income', 'zebra', 'casual', 'asthma', 'tell', 'enable', 'punch', 'reflect', 'jaguar', 'steak'])

        # check mnemonic
        if is_mnemonic(mnemonic=MNEMONIC):

            # mnemonic is valid
            print (f'{counter}: valid mnemonic: {MNEMONIC}')

            # get hdwallet from mnemonic
            bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(symbol=SYMBOL)
            bip44_hdwallet.from_mnemonic(mnemonic=MNEMONIC)

            # compare wallet with wallet's xpub
            if bip44_hdwallet.root_xpublic_key() == wallet_xpub:

                # print mnemonic
                print (f'\n---------------------\nMNEMONIC FOUND\n---------------------\n')
                print (f'{counter}: found mnemonic: {MNEMONIC}')

                # print time
                end = time.time()
                print (f'search took {end-start} seconds')

                # print hdwallet info
                print(json.dumps(bip44_hdwallet.dumps(), indent=4, ensure_ascii=False))

                #stop
                exit()

        else:
            
            # mnemonic is invalid
            print (f'{counter}: invalid mnemonic: {MNEMONIC}')

    else:
        for c in word_list:
            if c in _accum:
                continue
            all_mnemonics(word_list, n, _accum+[c])

all_mnemonics(wallet_words, 12)
