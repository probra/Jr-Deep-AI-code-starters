"""
THE SELF-LEARNING ANIMAL GUESSER — STUDENT VERSION
=====================================================

Your job: fill in the two functions marked "YOUR CODE HERE".
Everything else (saving, loading, asking questions) is done for you.

THE BIG AI IDEA:
  A "decision tree" is just a bunch of yes/no questions that branch
  off each other, like a flowchart. Real AI classifiers (deciding
  if an email is spam, if a tumor is dangerous, etc.) often work
  this exact way — just with WAY more questions and WAY more data.
"""

import json
import os

SAVE_FILE = "animal_tree.json"

# The tree is a nested dictionary. Two kinds of "nodes":
#
#   A QUESTION node looks like:
#     {"question": "Does it have fur?", "yes": <node>, "no": <node>}
#
#   An ANIMAL node (a "leaf" — the end of a branch) looks like:
#     {"animal": "dog"}
STARTER_TREE = {
    "question": "Does it live in water?",
    "yes": {"animal": "fish"},
    "no": {"animal": "dog"},
}


# ------------------------------------------------------------------
# Done for you — no need to touch these.
# ------------------------------------------------------------------

def load_tree():
    """Load the saved tree from file, or start fresh if none exists."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return STARTER_TREE


def save_tree(tree):
    """Save the tree to file so it remembers what it learned."""
    with open(SAVE_FILE, "w") as f:
        json.dump(tree, f, indent=2)


def ask_yes_no(question):
    """Ask a yes/no question and keep asking until we get a clean answer."""
    # ------------------------------------------------------------------
    # YOUR CODE HERE #1: ask yes or no
    # ------------------------------------------------------------------
    #
    # This function is what asks the questions during the game.
    #
    # STEPS TO WRITE:
    #   1. A continuous loop that asks for an input.
    #   2. if the input is y, return True and if the input is n return False


# ------------------------------------------------------------------
# YOUR CODE HERE #2: play_round
# ------------------------------------------------------------------
#
# This function walks down the tree, one question at a time, until
# it hits an animal (a "leaf").
#
# 'node' is where we currently are in the tree.
# 'tree' is the WHOLE tree (we need to pass it along so we can save
#         changes later, inside teach_the_computer).
#
# STEPS TO WRITE:
#   1. Check: does `node` have the key "animal" in it?
#        - If YES, we've reached a guess! Use ask_yes_no() to ask
#          "Were you thinking of a {node['animal']}?"
#            - If they say yes: print a success message. Return.
#            - If they say no: call teach_the_computer(node), then
#              save_tree(tree), then return.
#   2. If `node` does NOT have "animal" (so it's a question node):
#        - Use ask_yes_no() to ask node["question"]
#        - If the answer is True, call play_round again, but on
#          node["yes"] this time (and pass tree along too!)
#        - If the answer is False, call play_round again, but on
#          node["no"] this time

def play_round(node, tree):
    # TODO: replace this line with your code (see steps above)
    if "animal" in node:
        # We've reached a guess. Check if we're right.
        # correct = *call a function*
        # if correct
            #print something
        # else
            #teach the computer function
            #save the tree function
        return

    # It's a question — ask it and go down the matching branch.
    if ask_yes_no(node["question"]):
        play_round(node["yes"], tree)
    else:
        play_round(node["no"], tree)


# ------------------------------------------------------------------
# YOUR CODE HERE #2: teach_the_computer
# ------------------------------------------------------------------
#
# We guessed wrong! This function needs to:
#
#   1. Save the wrong guess: old_animal = wrong_node["animal"]
#   2. Ask the player what they were really thinking of, using
#      input(...).strip() — save it as new_animal
#   3. Ask the player for a yes/no QUESTION that is true for the
#      new animal but false for the old one — save it as
#      new_question
#   4. Turn wrong_node from a leaf into a question node:
#        wrong_node["question"] = new_question
#        wrong_node["yes"] = {"animal": new_animal}
#        wrong_node["no"] = {"animal": old_animal}
#        del wrong_node["animal"]     <- it's not a leaf anymore!
#   5. Print a message confirming it learned something
#
# HINT: Steps 4 are already basically written for you above —
# just copy them in, in order, after you've done steps 1-3.

def teach_the_computer(wrong_node):
    # TODO: replace this line with your code (see steps above)
    old_animal = wrong_node["animal"]
    # take an input for the new animal

    # Take another input for the new question that is going to be asked

    # wrong_node["question"] = YOUR VARIABLE FOR QUESTION
    # wrong_node["yes"] = {"animal": YOUR VARIABLE FOR ANIMAL}
    # wrong_node["no"] = {"animal": old_animal}
    del wrong_node["animal"]  # it's not a leaf anymore, it's a question now

    #print a message to say, thank you i got it


# ------------------------------------------------------------------
# Done for you — no need to touch this.
# ------------------------------------------------------------------

def main():
    print("=" * 50)
    print("Think of an animal. I'll try to guess it!")
    print("=" * 50)

    tree = load_tree()

    while True:
        play_round(tree, tree)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print("Thanks for playing! I saved everything I learned.")


if __name__ == "__main__":
    main()