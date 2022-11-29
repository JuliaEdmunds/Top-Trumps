import helpers


def keep_playing():
    is_still_playing = input("\nDo you want to play again? (yes/no) ").lower().strip()
    while is_still_playing != "yes" and is_still_playing != "no":
        is_still_playing = input("Please answer yes or no? ").lower().strip()

    if is_still_playing == "yes":
        helpers.clear()
        return True
    else:
        print("\nThanks for playing! Bye...")
        return False
