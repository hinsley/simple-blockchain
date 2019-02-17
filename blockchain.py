import datetime
import hashlib
import pickle


class Block():
    def __init__(self, data, prev_block_hash):
        self._data = data
        self._timestamp = datetime.datetime.now()
        self._prev_block_hash = prev_block_hash
        self.nonce = 0

        # This always needs to be the last statement in this method.
        self.set_hash()
    
    def _standardize_block(self):
        """
        Make sure this block generates reproducible hashes.
        
        Standardizes timestamp. This is useful for unit tests.
        """
        # Set timestamp to POSIX epoch.
        self._timestamp = datetime.datetime.utcfromtimestamp(0)

    def _serialize(self):
        return repr([self.data,
                     self._timestamp,
                     self._prev_block_hash,
                     self.nonce]).encode()

    def set_hash(self, standardized=False):
        if standardized:
            self._standardize_block()

        serialization = self._serialize()
        self._hash = int(hashlib.sha256(serialization).hexdigest(), 16)

    @property
    def data(self):
        return self._data

    @property
    def hash(self):
        return self._hash


class Blockchain():
    def __init__(self, genesis_data="Genesis block"):
        self.blocks = [Block(genesis_data, None)]
    
    def add_block(self, data):
        self.blocks.append(Block(data, self.blocks[-1].hash))
