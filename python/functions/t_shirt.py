def make_shirt(size, slogan):
    """Display the size and message printed on the T-Shirt"""
    print(f"\nMy T-Shirt size is {size.upper()} with the slogan {slogan.title()}.")

make_shirt('l', 'python is fun')

make_shirt(size='m', slogan='manabi hub')

make_shirt('s', 'never stop learning')
