import numpy as np

def simulate_stochastic_resonance(
    true_signal_rate=80, 
    threshold=96, 
    laplace_scale=10.0, 
    days=30
):
    print(f"--- Stochastic Resonance in Differential Privacy ---")
    print(f"True Signal Rate:   {true_signal_rate} errors/day")
    print(f"Detection Threshold: {threshold} (Deterministic)")
    print(f"DP Noise added:      Laplace(scale={laplace_scale})")
    print(f"Simulation Period:   {days} days\n")

    # 1. Deterministic System (No Noise)
    deterministic_detections = 0
    for day in range(days):
        if true_signal_rate > threshold:
            deterministic_detections += 1
            
    print(f"[Without DP Noise] Number of days detected: {deterministic_detections}")

    # 2. DP System (With Laplace Noise)
    np.random.seed(42)  # For reproducibility in the demo
    dp_detections = 0
    dp_days_fired = []
    
    for day in range(1, days + 1):
        noise = np.random.laplace(loc=0.0, scale=laplace_scale)
        noisy_signal = true_signal_rate + noise
        
        if noisy_signal > threshold:
            dp_detections += 1
            dp_days_fired.append(day)
            
    print(f"[With DP Noise]    Number of days detected: {dp_detections}")
    
    if dp_detections > 0:
        print(f"                   Fired on days: {dp_days_fired}")
        print("\nCONCLUSION: The DP noise constructively interfered with the sub-threshold signal,")
        print("pushing it over the threshold and allowing the system to detect the anomaly!")
    else:
        print("\nCONCLUSION: Signal remained undetected.")

if __name__ == "__main__":
    # Simulate a signal that is structurally invisible (80) against the 3.6-sigma threshold (96)
    simulate_stochastic_resonance(true_signal_rate=80, threshold=96, laplace_scale=12.0, days=90)
