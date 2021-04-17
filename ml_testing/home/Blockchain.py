from home.block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(Block.genesis())

    def get_block(self, index):

        return self.chain[index]

    def add_block(self, new_block):
        mined_block = Block.mine(new_block, self.chain[len(self.chain)-1])
        self.chain.append(mined_block)

    def get_length(self):
        return len(self.chain)

#    def get_gpa(self, student_id):
#        for b in range(len(self.chain)):
#            print(b)
#        return 90

    def __repr__(self):
        out = "Blockchain<\n"
        for b in range(len(self.chain)):
            out=out+"\t"+repr(self.chain[b])
        out=out+">"
        return out
