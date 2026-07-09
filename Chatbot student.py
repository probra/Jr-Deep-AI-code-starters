"""
BUILD YOUR OWN CHATBOT — STUDENT VERSION
===========================================

Your job is two-fold:
  1. Fill in the get_response() function (marked "YOUR CODE HERE")
     — this is the actual keyword-matching "brain" of the bot.
  2. Fill out RESPONSE_BANK below with your own bot's personality!

THE BIG AI IDEA:
  This is called "keyword matching" or "pattern matching." The bot
  doesn't understand you — it just scans what you typed for certain
  KEYWORDS, and replies with something that matches. This is a much
  simpler cousin of what real chatbots and assistants do.
"""

import random

# ------------------------------------------------------------------
# THIS IS YOUR BOT'S PERSONALITY — EDIT THIS!
# ------------------------------------------------------------------
#
# Each keyword maps to a LIST of possible responses. The bot picks
# one at random each time, so it doesn't feel too repetitive.
#
# Keep keywords lowercase — we lowercase what the player types too,
# so "MOM" and "mom" both match.

BOT_NAME = "Botly"   # TODO: give your bot its own name!

RESPONSE_BANK = {
    "hello": [
        "Oh, hello there.",
        "Hi! I was just recalculating the meaning of life.",
    ],
    "name": [
        f"I'm {BOT_NAME}, obviously.",
    ],
    # TODO: Add at least 4-5 more of your own keywords and responses!
    # Give your bot a theme/personality — grumpy robot, fortune
    # teller, conspiracy-theorist toaster, overly-dramatic diary,
    # whatever you want.
    #
    # "keyword": ["response one", "response two"],
}

# If nothing matches, the bot picks randomly from here instead. Change this or add more
FALLBACK_RESPONSES = [
    "I don't quite follow. Try saying that differently?",
    "Hmm, that's outside my programming.",
    "Interesting. Tell me more.",
]

EXIT_WORDS = ("bye", "quit", "exit")


# ------------------------------------------------------------------
# YOUR CODE HERE: get_response
# ------------------------------------------------------------------
#
# This function looks through RESPONSE_BANK for any keyword that
# appears inside what the player typed. If it finds one, it should
# return a random response for that keyword. If nothing matches at
# all, it should return a random fallback response instead.
#
# STEPS TO WRITE:
#   1. Make the player's input lowercase, so matching isn't
#      case-sensitive:
#        text = player_input.lower()
#
#   2. Loop through every keyword in RESPONSE_BANK, one at a time:
#        for keyword in RESPONSE_BANK:
#
#   3. Inside the loop, check: is `keyword` found anywhere INSIDE
#      `text`? (Hint: Python lets you write `if keyword in text:`
#      to check if one string appears inside another.)
#
#   4. If it IS found:
#        a. Get that keyword's list of responses out of the
#           dictionary:
#              matching_responses = RESPONSE_BANK[keyword]
#        b. Pick a random one from that list:
#              chosen_response = random.choice(matching_responses)
#        c. Return chosen_response — we're done, no need to keep
#           looping.
#
#   5. If the loop finishes and NOTHING matched: return a random
#      choice from FALLBACK_RESPONSES instead.
def get_response(player_input):
    # TODO: replace this line with your code (see steps above)
    # text = player_input.lower()
    #
    # for something in something
    # if the keyword is in the text
    # find the matching response
    # find your response
    # return our response
    # if keyword not in the text, return a random fallback choice


# ------------------------------------------------------------------
# Final step. MAIN LOOP
# ------------------------------------------------------------------

def main():
    print("=" * 50)
    print(f"Chatting with {BOT_NAME}  (type 'bye' to quit)")
    print("=" * 50)

    # infinite loop
        # take input "player_input"

        #if player_input.lower() in EXIT_WORDS:
            #print(f"{BOT_NAME}: See you later!")
            #break

        #response = get_response(player_input)
        #print(f"{BOT_NAME}: {response}")


if __name__ == "__main__":
    main()