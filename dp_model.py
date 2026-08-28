import math

def calculate_required_volume(epsilon, t_max, latency, delta_p, delta_f=1.0, confidence_z=2.0):
    """
    Calculates required traffic volume per round to detect a spike in error rates.
    Using Binary Tree mechanism for continual counting.
    """
    # Number of levels in the tree
    levels = math.ceil(math.log2(t_max))
    
    # StdDev of noise at each node = (delta_f * levels) / (epsilon / sqrt(2) ? No, standard binary tree splits epsilon evenly across levels)
    # Epsilon per level = epsilon / levels
    # Laplace scale b = delta_f / (epsilon / levels) = (delta_f * levels) / epsilon
    # Variance of Laplace = 2 * b^2
    node_variance = 2 * ((delta_f * levels) / epsilon) ** 2
    
    # A prefix sum is composed of at most 'levels' nodes
    # The variance of the prefix sum is bounded by levels * node_variance
    prefix_variance = levels * node_variance
    
    # We are looking at a window of size L: S(t) - S(t-L)
    # The variance of this difference is at most 2 * prefix_variance (worst case)
    window_variance = 2 * prefix_variance
    window_stddev = math.sqrt(window_variance)
    
    # Required signal to overcome noise
    required_signal = confidence_z * window_stddev
    
    # Signal = Volume_per_round * Latency * Delta_P
    # Volume_per_round = Required_signal / (Latency * Delta_P)
    required_volume = required_signal / (latency * delta_p)
    
    return math.ceil(required_volume)

print("| $T_{max}$ (Rounds) | $\\epsilon$ | Latency $L$ | $\\Delta p$ (Spike) | Required Vol/Round | Total Vol/Window |")
print("|---|---|---|---|---|---|")

scenarios = [
    (8192, 1.0, 24, 0.15),
    (8192, 1.0, 4, 0.15),
    (8192, 0.5, 24, 0.15),
    (8192, 0.5, 24, 0.05),
    (32768, 1.0, 24, 0.15),
    (1024, 1.0, 10, 0.20)
]

for t, eps, l, dp in scenarios:
    vol = calculate_required_volume(eps, t, l, dp)
    total_window_vol = vol * l
    print(f"| {t} | {eps} | {l} | {dp*100:.0f}% | {vol} | {total_window_vol} |")

