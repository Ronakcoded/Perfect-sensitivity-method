def psa_method(initial_sens, steps=8, scale=0.1):
    low = initial_sens * (1 - scale)
    high = initial_sens * (1 + scale)
    
    current = initial_sens

    for i in range(steps):
        print(f"\nStep {i+1}")
        print(f"Test these sensitivities:")
        print(f"1. Lower:  {low:.4f}")
        print(f"2. Higher: {high:.4f}")

        choice = input("Which feels better? (l/h): ").strip().lower()

        if choice == 'l':
            # Narrow towards lower side
            high = current
            current = low
        elif choice == 'h':
            # Narrow towards higher side
            low = current
            current = high
        else:
            print("Invalid input, skipping...")
            continue

        # Shrink range further
        low = current * (1 - scale / 2)
        high = current * (1 + scale / 2)

    return current


# Example usage
result = psa_method(initial_sens=2.0)
print(f"\n🎯 Optimal Sensitivity ≈ {result:.4f}")
