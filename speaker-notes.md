# The Journey of an Unsigned Transaction Output (UTXO)

## Introduction

- Pre-req

  - Let's focus on the tech, Imagine 1 bitcoin is worth $0, and briefly pretend
  - No monetary theory "No what is money"
  - No macro economics
  - We can get coffee or drinks if you'd like to talk about
  - Legal disclaimer

  - "I don't care how long your blockchain is or how big your block size is"

## Objective

- The aim to demystify Bitcoin by focusing on its data structures and algorithms.
- This talk provides a brief overview of key concepts, serving as a foundation for deeper exploration.

## Questions

I'd like to answering these questions

- What is a hash? Where is it used in Bitcoin?
- What is a blockchan?
- What is proof of work?
- What is the difficult ajustmentg
- What is a unsigned transation ouput (UTXO)?
- Why UTXO and not accounting based?
- Where are your coins?
- What is a public key? What is private key?
- How is a transaction built?
- How is a transaction broadcasted?
- How is a transaction verified?
- How does a transaction get added to the next block?

## The Journey of an UTXO

### Mining

What is Proof of Work (PoW)?

Proof of Work (PoW) is a consensus algorithm used in Bitcoin to validate transactions and create new blocks.

or

Proof of work (PoW) is a form of cryptographic proof in which one party (the prover) proves to others (the verifiers) that a certain amount of a specific computational effort has been expended.

A key feature of proof-of-work schemes is their asymmetry: the work – the computation – must be moderately hard (yet feasible) on the prover or requester side but easy to check for the verifier or service provider

In otherwords:

- Computationally difficult to come up with the answer
  -> why do we want it to be difficult to come up with the answer?
- Computationally easy to verify the answer is correct

What is this "work" in bitcoin?

SHA256

What is a block?
How do bitcoin come into existence?

- Block reward
- Block fees
- Block subsidy

- Quick demo of what POW looks like: [Proof of work](https://stefanhuber.github.io/proof-of-work/)

[The genesis block](https://www.blockstream.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)
This is the Genesis address, it is owned by Satoshi Nakamoto and contains the unspendable 50 bitcoin mined from the genesis block.

### Coinbase

What is a coinbase? (not to be confused with Coinbase)

coinbase -> first transaction in a blockchain

- breaking down the transaction

### Building a Transaction

Types of addresses

### Broadcasting a Transaction

Sharing your transaction to a node

### Validating a transaction

_Do miners check it before including it in a block?_
** - Yes, if a miner includes an invalid transaction, the other nodes will not accept that block and that miner won't earn the block reward for that block.**

_Do other nodes check it and where there is a certain conensus miner include it into a block?_
** Yes, but why?**

Are all miners trying to solve the same block at the same time or different blocks?
They are trying to find a block with the same height, but with different tx, different nonces (a random number, related to block hash and difficult) and a different block reward

### Mining the Next Block

What is a confirmation

## Conclusion

Include donation link at the end in LN/BTC

## Resources

- [Esplora](https://github.com/Blockstream/esplora)
- [Electrs](https://github.com/romanz/electrs)
- [Sender, nodes or miners? Who validates transactions](https://bitcoin.stackexchange.com/questions/63910/sender-nodes-or-miners-who-validates-transactions)
- [Geroge Levy](https://www.youtube.com/watch?v=5-IGfoY1SfE)
- [Bitcoin Developer Guides](https://developer.bitcoin.org/devguide/)
- [Proof of Work](https://en.wikipedia.org/wiki/Proof_of_work)
- [How Is Difficulty Calculated](https://bitcoin.stackexchange.com/questions/5838/how-is-difficulty-calculated)
- [Difficult](https://en.bitcoin.it/wiki/Difficulty)
