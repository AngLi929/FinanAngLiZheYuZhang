POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03

# transition matrix
TRANS_MATRIX = [
    [0.592,  0.06,   0.33,   0,   0.018],   # Well
    [0,   0.47,   0,   0.33,   0.2],   # Stroke
    [0,   0,   0.79,   0.06,   0.15],   # Fall
    [0,   0,    0,   0.65,   0.35],   # Stroke+Fall
    [0,   0,   0,   0,   1]           # Death
    ]

RR_STROKE_Warfarin = 0.32

RR_STROKE_Aspirin = 0.79

RR_Death_Warfarin_Fall = 1.0001

RR_Death_Aspirin_Fall = 1.00005


# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1,
    0.9,
    0.76,
    0.68,
    ]
