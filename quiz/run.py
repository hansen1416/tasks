class OnlinePredictor :
    def __init__(self, k) :
        self.k = k
        self.prev_y = 1
        # if needed, add code here

    # if needed, helper functions here

    def receive_input_and_predict(self, x):
        assert x >= 0 and x < self.k, "input x out of range"
        # code here, modify the answer below
        return self.k % (x+1) + 1 #int(x+1 == 1)


    def receive_label(self, y) :
        # if needed, code here
        self.prev_y == y

    # For local debugging purposes
    def count_mistakes(self, input_sequence, true_classifier):
        assert len(true_classifier) == self.k and max(true_classifier) == 1 and min(true_classifier) >= 0, "The true classifier should be a list of integers {0,1} of length k with at least one 1"
        number_mistakes = 0
        for x in input_sequence :
            y_true = true_classifier[x]
            y_predicted = self.receive_input_and_predict(x)
            number_mistakes += (y_true != y_predicted)
            self.receive_label(y_true)
        return number_mistakes

# For local debugging
op = OnlinePredictor(1)
assert op.receive_input_and_predict(0) == 1

op = OnlinePredictor(2)
assert op.count_mistakes([0, 1, 0, 1, 1], [0, 1]) < 2

op = OnlinePredictor(3)
assert op.count_mistakes([2, 0, 1, 0], [0, 1, 0]) < 3