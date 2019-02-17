import blockchain


def standardize_last_block(bc):
    bc.blocks[-1].set_hash(standardized=True)


def test_blockchain_synthesis():
    bc = blockchain.Blockchain("foo")
    standardize_last_block(bc)

    bc.add_block("bar")
    standardize_last_block(bc)

    for block in bc.blocks:
        print(block.hash)

    # Copy of previous block hash matches original.
    assert bc.blocks[0].hash == bc.blocks[1]._prev_block_hash

    # Hashes match expectation.
    assert bc.blocks[0].hash == 97008229366431559932534276396918853258125216905484365321406195610963944071001
    assert bc.blocks[1].hash == 43689312143490453084997289309309791731884751642456703427447473670013231739557
