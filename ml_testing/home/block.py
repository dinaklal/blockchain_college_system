from hashlib import sha256
import time


class Block:
    def __init__(self, timestamp, prevHash, data, difficulty, student_id, first_name, last_name, tuition_fee, mess_fee, hostel_fee, course, status):
        self.height = 0
        self.timestamp = timestamp
        self.prevHash = prevHash
        self.currHash = 0
        self.data = data
        self.nonce = 0
        self.difficulty = difficulty
        self.student_id=student_id
        self.first_name=first_name
        self.last_name=last_name
        self.tuition_fee=tuition_fee
        self.mess_fee=mess_fee
        self.hostel_fee=hostel_fee
        self.course = course
        self.status=status

    def __repr__(self):
        return 'Block<\n\t\theight:{}\n\t\ttimestamp:{}\n\t\tprevHash:{}\n\t\tcurrHash:{}\n\t\tdata:{}\n\t\tnonce:{}\n\t\tdifficulty:{}\n\t\tstudent_id:{}\n\t\tfirst_name:{}\n\t\tlast_name:{}\n\t\ttuition_fee:{}\n\t\tmess_fee:{}\n\t\thostel_fee:{}\n\t\tcourse:{}\n\t\tstatus:{}\n\t>\n'.format(self.height, self.timestamp, self.prevHash, self.currHash, self.data, self.nonce, self.difficulty, self.student_id, self.first_name, self.last_name, self.tuition_fee, self.mess_fee, self.hostel_fee, self.course, self.status)

    @staticmethod
    def genesis():
        return Block(0, 0, "genesis", 4, 0, "None", "COMP0000", "None", 0, 0, 0, 0)

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
