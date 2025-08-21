people = {
        'me' : {
            'first' : 'nk',
            'last' : 'afo',
            'cong' : 'n b',
            'status' : 'e',
                },
        'sal' : {
            'first' : 'sal',
            'last' : 'afo',
            'cong' : 'n b',
            'status' : 'r p',
                },
        'drg' : {
            'first' : 'fm',
            'last' : 'afo',
            'cong' : 'ife',
            'status' : 'e',
                },
        'me' : {
            'first' : 'ali',
            'last' : 'afo',
            'cong' : 'dur',
            'status' : 'p',
                },
        'de' : {
            'first' : 'dor',
            'last' : 'og',
            'cong' : 'k m',
            'status' : 'p',
                },
        'ndk' : {
            'first' : 'co',
            'last' : 'et',
            'cong' : 'prk',
            'status' : 'e',
                },
        }

for nickname, person_data in people.itmes():
    full_name = f"{person_data['first']} {person_data['last']}"
    congregation = person_data['cong']
    status = person_data['status']
    print(f"Name: {full_name.title()}.\n Status: {status}, {congregation.title()} cong. Some friends "
       f"call me {nickname}\n")
