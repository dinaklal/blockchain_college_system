from hashlib import sha256
import time


class Block:
    def __init__(self, timestamp, prevHash, data, difficulty, student_id, student_name, class_id, class_name, grade, absences, credits):
        self.height = 0
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.currHash = 0
        self.data = data
        self.nonce = 0
        self.difficulty = difficulty
        self.student_id=student_id
        self.student_name=student_name
        self.class_id=class_id
        self.class_name=class_name
        self.grade=grade
        self.absences=absences
        self.credits=credits

    def __repr__(self):
        return 'Block<\n\t\theight:{}\n\t\ttimestamp:{}\n\t\tprevHash:{}\n\t\tcurrHash:{}\n\t\tdata:{}\n\t\tnonce:{}\n\t\tdifficulty:{}\n\t\tstudent_id:{}\n\t\tstudent_name:{}\n\t\tclass_id:{}\n\t\tclass_name:{}\n\t\tgrade:{}\n\t\tabsences:{}\n\t\tcredits:{}\n\t>\n'.format(self.height, self.timestamp, self.prevHash, self.currHash, self.data, self.nonce, self.difficulty, self.student_id, self.student_name, self.class_id, self.class_name, self.grade, self.absences, self.credits)

    @staticmethod
    def genesis():
        return Block(0, 0, "genesis", 4, 0, "None", "COMP0000", "None", 0, 0, 0)

    @staticmethod
    def mine(block, last_block):
        difficulty=last_block.difficulty
        block.height=last_block.height+1
        block.prevHash=last_block.currHash
        while True:
            block.nonce=block.nonce+1
            block.timestamp=int(time.time())
            tmp_hash=sha256(str(block).encode()).hexdigest()
            if tmp_hash[0:difficulty] == '0'*difficulty:
                break
        block.currHash = tmp_hash
        return block
