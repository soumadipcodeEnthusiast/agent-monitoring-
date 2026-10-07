def calculate_information_gain(prior_prob: float, posterior_prob: float) -> float:
    return abs(posterior_prob - prior_prob)
