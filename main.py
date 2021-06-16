from kahoot import client
import random

bot = client()



def spambots():
    gameid = input("Enter the game pin: ")
    botamount = input("Enter the amount of bots (max 2000): ")
    custom_username = input("Enter bots\' username: ")

    def joingame():
        username = (custom_username + str(random.randint(1, 10000)))
        bot.join((gameid), username)

        def joinHandle():
            pass

        bot.on("joined", joinHandle)
        print(f"Joined game {gameid} with username {username}.")
        # time.sleep(.1)

    for x in range(0, (int(botamount))):  # + 10  this is not code
        joingame()


spambots()
