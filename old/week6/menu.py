def menu():
    while(True):
        print("Press 1 to play a game, or q to exit.")
        choice = input()
        if choice == '1':
            return True
        elif choice == 'q':
            return False
