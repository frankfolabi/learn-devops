def make_sandwich(*ingredeents):
    """Display all the ingredeents supplied."""
    print("\nThis are the ingredeents for your sandwich.")
    for ingredeent in ingredeents:
        print(f"- {ingredeent}")


make_sandwich('onions', 'pepper', 'bread', 'sardene')
make_sandwich('green pepper', 'bell pepper', 'tomato', 'pita bread')
make_sandwich('tumeric', 'curry', 'rosmeary', 'dell', 'mint', 'cummin')
