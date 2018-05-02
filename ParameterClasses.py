from enum import Enum
import InputData as Data


class HealthStats(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    Fall = 2
    Fall_STROKE = 3
    DEATH = 4


class Therapies(Enum):

    NONE = 0
    Warfarin = 1
    Aspirin = 2


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # transition probability matrix of the selected therapy
        self._prob_matrix = []
        # treatment relative risk
        self._treatmentRR = 0

        # calculate transition probabilities depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix = Data.TRANS_MATRIX
        if therapy == Therapies.Warfarin:
            self._prob_matrix = calculate_prob_matrix_warfarin()
        if therapy == Therapies.Aspirin:
            self._prob_matrix = calculate_prob_matrix_aspirin()

        self._annualStateUtilities = Data.ANNUAL_STATE_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_annual_state_utility(self, state):
        if state == HealthStats.DEATH:
            return 0
        else:
            return self._annualStateUtilities[state.value]


def calculate_prob_matrix_warfarin():

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))

    # for all health states
    for s in HealthStats:
        if s == HealthStats.WELL :
            prob_matrix[s.value][HealthStats.STROKE.value] \
                = Data.RR_STROKE_Warfarin * Data.TRANS_MATRIX[s.value][HealthStats.STROKE.value]
            prob_matrix[s.value][s.value] \
                = 1 - prob_matrix[s.value][HealthStats.STROKE.value] - prob_matrix[s.value][HealthStats.DEATH.value] - prob_matrix[s.value][HealthStats.Fall.value]

        if s== HealthStats.Fall:
            prob_matrix[s.value][HealthStats.DEATH.value] \
                = Data.RR_Death_Warfarin_Fall * Data.TRANS_MATRIX[s.value][HealthStats.DEATH.value]

            prob_matrix[s.value][s.value] \
                = 1 - prob_matrix[s.value][HealthStats.Fall_STROKE.value] - prob_matrix[s.value][HealthStats.DEATH.value]

        else:
            prob_matrix[s.value] = Data.TRANS_MATRIX[s.value]

    return prob_matrix


def calculate_prob_matrix_aspirin():

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))

    # for all health states
    for s in HealthStats:
        if s == HealthStats.WELL :
            prob_matrix[s.value][HealthStats.STROKE.value] \
                = Data.RR_STROKE_Aspirin * Data.TRANS_MATRIX[s.value][HealthStats.STROKE.value]
            prob_matrix[s.value][s.value] \
                = 1 - prob_matrix[s.value][HealthStats.STROKE.value] - prob_matrix[s.value][HealthStats.DEATH.value] - prob_matrix[s.value][HealthStats.Fall.value]

        if s== HealthStats.Fall:
            prob_matrix[s.value][HealthStats.DEATH.value] \
                = Data.RR_Death_Aspirin_Fall * Data.TRANS_MATRIX[s.value][HealthStats.DEATH.value]

            prob_matrix[s.value][s.value] \
                = 1 - prob_matrix[s.value][HealthStats.Fall_STROKE.value] - prob_matrix[s.value][HealthStats.DEATH.value]

        else:
            prob_matrix[s.value] = Data.TRANS_MATRIX[s.value]

    return prob_matrix
