def complains():
    google_branches = {1: 'google_kazakhstan.txt',
                       2: 'google_paris.txt',
                       3: 'google_kyrgyzstan.txt',
                       4: 'google_san_francisco.txt',
                       5: 'google_germany.txt',
                       6: 'google_moscow.txt',
                       7: 'google_sweden.txt'
                       }
    print("Enter a number: ")
    for key, value in google_branches.items():
        office = value.replace('_', ' ').title()
        print(f"{key}:{office.replace('.Txt','')}")

    user_choice = int(input("Enter branch num:"))


    try:

        office = google_branches[user_choice]
        user_text = input("Enter your text:")
        with open(office, 'w') as the_file:
            the_file.write(user_text)
        print("Thanks for feedback")
    except KeyError:
        print("Choose from the list above")
        complains()


complains()