# twelve-word-search
If you have 12 seed words of a Bitcoin seed, but you don't know the order, can we figure it out?

The script iterates through all 12! or 12 factorial possibilities.

I generated a test mnemonic and derived the xpub for testing purposes.  The initial mnemonic is randomized and the testing is started.

# The answer is YES, but it will take a while
I did a test for the first 100,000 combinations, and it took about 7 minutes on an M1 mac. This means that going through all 479001600 combinations would take approximately 3-4 weeks.

The script uses meherett's hdwallet to generate and check wallets! https://github.com/meherett/python-hdwallet
