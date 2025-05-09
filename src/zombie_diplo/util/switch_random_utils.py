def generate_summands_for_power_of_2(n: int) -> list[int]:
    """Use this to get all the death counter additions for random outcomes that total to
    a power of 2.

    For each summand, add that to the death counter if a switch is set after randomized.

    The final value will be the random outcome, between 0 - 2^N.
    """
    # Initialize an empty list to hold the summands
    summands = []
    # Start with 1 and keep doubling until we reach n/2
    power = 1
    while power < n:
        summands.append(power)
        power *= 2
    return summands


def generate_intervals_for_probabilities(
    probabilities: list[float], total_outcomes: int
) -> list[tuple[int, int]]:
    """Given a list of probabilities that sum to 1.0, return a list of ranges so they
    fit within total outcomes.

    total_outcomes: must be a power of 2, e.g. 16, 32, etc. probabilities: a list of
    probabilities that sum to 1.0

    Outputs a list of inclusive intervals corresponding to each probability.  Example
    shown below:

    input: [0.5, 0.5] total_outcomes: 16

    output: [(0, 7), (8, 15)]
    """
    ranges = []
    current = 0
    for prob in probabilities:
        span = int(prob * total_outcomes) - 1  # Calculate the inclusive range
        new_range = (current, current + span)
        ranges.append(new_range)
        current += span + 1  # Move the current position forward
    # Adjust the last range to ensure it ends at N-1, in case of rounding errors
    if ranges:
        ranges[-1] = (ranges[-1][0], total_outcomes - 1)
    return ranges
