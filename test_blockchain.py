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
    assert bc.blocks[0].hash == 78624724043625491631625081821467555022045426575092870519192049178840472517206
    assert bc.blocks[1].hash == 17722030891731471998491204984460733743673572268750253659970108527622090887524
