def compute_relative_frequency(data, event):
    """
    Computes the probability of an event using the relative frequency approach.
    """
  
    event_count = list(data).count(event)
    total_trials = len(data)
    
    probability = event_count / total_trials
    
    return probability

# Example Usage:
tosses = ['Heads', 'Tails', 'Heads', 'Heads', 'Tails']
prob_heads = compute_relative_frequency(tosses, 'Heads')
print(f"Probability of Heads: {prob_heads}") # Output: 0.6
