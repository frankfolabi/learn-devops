def make_shirt(size='l', slogan='I love Python'):
    """Display the size and message printed on the T-Shirt"""
    print(f"\nMy T-Shirt size is {size.upper()} with the slogan {slogan.title()}.")

# Medeum shirt with default message
make_shirt(size='m')
# Different shirt size with anothe message
make_shirt('s', 'never stop learning')
# Large shirt with default message
make_shirt()
