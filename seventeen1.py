#!/usr/bin/env python

#########################################################

import random 

def print_marbles_remaining(marbles_remaining):
	'''Prints a string indicating the marbles remaining
	in the jar.
	'''
	print 'Number of marbles left in jar: {0}\n'.format(marbles_remaining)

def user_turn(marbles_remaining):
	'''Prompts the user to remove 1, 2, or 3 marbles.

	Function prompts the user again if the user inputs
	an inappropriate value (e.g. a string, more than 3 marbles
	or more marbles than there are remaining in the jar.)
	'''
	while True:
		marbles_removed = raw_input('Your turn: How many marbles will you remove (1-3)? ')
		if marbles_removed == '1' or marbles_removed == '2' or marbles_removed == '3' and int(marbles_removed)<= marbles_remaining:		#How can I make this line wrap?
			print 'You removed {0} marble(s).'.format(marbles_removed)
			return int(marbles_removed)
		else:
			print 'Sorry, that is not a valid option. Try again!'
			print_marbles_remaining(marbles_remaining)

def computer_turn(marbles_remaining):
	'''Function calculates how many marbles the computer
	will remove from the jar. 

	Computer strategy: remove a random integer between
	1 and 3.
	'''
	while True:
		print "Computer's turn..."

		marbles_removed = random.randint(1, min(marbles_remaining, 3))
								
		print "Computer removed {0} marble(s).".format(marbles_removed)
		return marbles_removed

def determine_winner(play_sequence):
	'''Takes the play_sequence as an input and 
	determines the winner based on the length of the 
	play_sequence, given the user took the first turn.
	'''
	if len(play_sequence)%2 == 0:
		winner = 'You'
	else:
		winner = 'Computer'
	print 'There are no marbles left. {0} win(s)!'.format(winner)

def play_game():
	'''Function plays a game of Seventeen. 

	Function first prompts the user to remove marbles, 
	then alternates between the compuer and the user.
	The function keeps track of the play sequence, marbles 
	remaining in the jar, and determines the winner at the end of the game.
	'''
	initial_marbles = 17
	play_sequence = []
	marbles_remaining = initial_marbles - sum(play_sequence)

	print "Let's play the game of Seventeen!"

	#Play the game while there are still marbles in the jar.
	while sum(play_sequence) < initial_marbles:						
		print_marbles_remaining(marbles_remaining)
		if len(play_sequence)%2 == 0:								#User's turn
			play_sequence.append(user_turn(marbles_remaining))
		else:														#Computer's turn
		 	play_sequence.append(computer_turn(marbles_remaining))
		
		marbles_remaining = initial_marbles - sum(play_sequence)
		
	determine_winner(play_sequence)

#########################################################

def main():
	'''Plays the game of seventeen. 

	A human user plays against a computer, with the human
	always going first. 
	The user and the computer take turns removing 1, 2, or 3
	marbles from a jar of seventeen marbles.
	The player who removes the last marble from the jar
	loses the game.
	'''
	play_game()


if __name__ == "__main__":
	main()