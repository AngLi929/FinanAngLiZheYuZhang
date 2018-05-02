import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov



cohort_notherapy = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_NO = cohort_notherapy.simulate()

cohort_wafarin = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.Warfarin)

cohort_aspirin = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.Aspirin
)


# simulate the cohort
simOutputs_wafarin = cohort_wafarin.simulate()
simOutputs_aspirin = cohort_aspirin.simulate()

SupportMarkov.print_outcomes(simOutputs_NO, "No Therapy:")
SupportMarkov.print_outcomes(simOutputs_wafarin, "Wafarin Therapy:")
SupportMarkov.print_outcomes(simOutputs_aspirin, "Aspirin Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_wafarin, simOutputs_NO)
SupportMarkov.print_comparative_outcomes(simOutputs_wafarin, simOutputs_aspirin)
