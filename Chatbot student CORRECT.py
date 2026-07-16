import random

# ------------------------------------------------------------------
# THIS IS THE PART YOU EDIT!
# ------------------------------------------------------------------
#
# RESPONSE_BANK is a list of lists.
#
# In each inner list:
#   - the FIRST item is the keyword to look for
#   - EVERYTHING AFTER that is a possible response
#
# The bot picks one of the responses at random, so it doesn't feel
# too repetitive.
#
# Keep keywords lowercase — we lowercase what the player types too,
# so "MOM" and "mom" both match.

BOT_NAME = "Botly"

RESPONSE_BANK = [
    ["hello",
     "Oh, hello there.",
     "Hi! I was just recalculating the meaning of life."],

    ["name",
     "I'm", BOT_NAME, "obviously."],
    

    # TODO: Add your own keywords and responses here!
    # ["keyword", "response one", "response two"],
]

# If nothing matches, the bot picks randomly from here instead.
FALLBACK_RESPONSES = [
    "I don't quite follow. Try saying that differently?",
    "Hmm, that's outside my programming.",
    "Interesting. Tell me more.",
]

EXIT_WORDS = ["bye", "quit", "exit"]


def get_response(player_input):
    """
    Look through RESPONSE_BANK for any keyword that appears inside
    what the player typed. If we find one, return a random response
    for it. If we find nothing, return a random fallback.
    """
    text = player_input.lower()

    #for every item in our response bank we loop
        #we set a keyword variable to be the first item in this item
        #we create a new list of everything after that first item.

        #if the specific keyword is in the text
            #return a random response

    #return a random fallback response


def main():
    print("=" * 50)
    print(f"Chatting with {BOT_NAME}  (type 'bye' to quit)")
    print("=" * 50)

    while True:
        player_input = input("You: ").strip()

        if player_input.lower() in EXIT_WORDS:
            print(f"{BOT_NAME}: See you later!")
            break

        response = get_response(player_input)
        print(f"{BOT_NAME}: {response}")


if __name__ == "__main__":
    main()