import random


class CookieHelper(object):

    def __init__(self):
        self.BID_LEN = 20
        self.BID_LIST_LEN = 500

    def gen_bids(self):
        bids = []
        for i in range(self.BID_LIST_LEN):
            bid = []
            for j in range(self.BID_LEN):
                bid.append(chr(random.randint(65,90)))
            bids.append("".join(bid))
        return bids