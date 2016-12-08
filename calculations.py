import pickle


def one_rep_max(input_weight, input_reps):
    """
    This calculates the one rep max for a given exercise. 
    The formula is from BRZYCKI, M. (1993) Strength testing-Predicting a one-rep max from reps-to-fatigue. JOPERD, 68, p. 88-90
    """
    one_rep_max = input_weight / (1.0278 - (0.0278* input_reps ))
    return one_rep_max

#Make the Wendlers 5/3/1 Weightlifting Program FROM https://www.t-nation.com/workouts/531-how-to-build-pure-strength

"""
The first four weeks calculates theset weights for the sets. 
"""

class week1:
    def set_1(one_rep_max):
        set_1 = one_rep_max * 0.65
        return set_1
    def set_2(one_rep_max):
        set_2 = one_rep_max * 0.75
        return set_2
    def set_3(one_rep_max):
        set_3 = one_rep_max * 0.85
        return set_3

class week2:
    def set_1(one_rep_max):
        set_1 = one_rep_max * 0.70
        return set_1
    def set_2(one_rep_max):
        set_2 = one_rep_max * 0.80
        return set_2
    def set_3(one_rep_max):
        set_3 = one_rep_max * 0.90
        return set_3

class week3:
    def set_1(one_rep_max):
        set_1 = one_rep_max * 0.75
        return set_1
    def set_2(one_rep_max):
        set_2 = one_rep_max * 0.85
        return set_2
    def set_3(one_rep_max):
        set_3 = one_rep_max * 0.95
        return set_3

class week4:
    def set_1(one_rep_max):
        set_1 = one_rep_max * 0.40
        return set_1
    def set_2(one_rep_max):
        set_2 = one_rep_max * 0.50
        return set_2
    def set_3(one_rep_max):
        set_3 = one_rep_max * 0.60
        return set_3

def open_file(filename):
    """
    This opens the pickle file and returns the max lifts as a dictionary. 
    """
    input_file = open(filename,'rb')
    max_lifts = pickle.load(input_file)
    input_file.close()
    return max_lifts

if __name__ == '__main__':
    main()
