#!/usr/bin/env python

#########################################################

import random 

def get_user_play_sequences():
	'''Opens a txt file and reads the Player 1 game sequences 
	listed on each row. Returns a list of tuples. Each tuple
	is a different game played, and indicates the marbles
	removed at each turn by Player 1.
	'''
	with open('i206_placein_input.txt') as f:
		user_play_sequences = f.read().split()
		user_play_sequences = [tuple(sequence.split(',')) for sequence in user_play_sequences]
		return user_play_sequences

def user_turn(marbles_remaining, game_num, turn_index_num):
	'''Determines the number of marbles removed for a
	game for a given turn by Player 1.

	Function returns an integer of the marbles that were
	removed from the jar by Player 1.
	'''
	while True:
		marbles_removed = min(int(get_user_play_sequences()[game_num][turn_index_num]), marbles_remaining)
		return int(marbles_removed)

def computer_turn(marbles_remaining):
	'''Function calculates how many marbles the computer
	will remove from the jar. 

	Computer strategy: remove a random integer between
	1 and 3.
	'''
	while True:
		marbles_removed = random.randint(1, min(marbles_remaining, 3))			
		return marbles_removed

def determine_winner(play_sequence):
	'''Takes the play_sequence of a game as an input and 
	determines the winner of the game based on the length of the 
	play_sequence, given the user took the first turn.
	'''
	if len(play_sequence)%2 == 0:
		winner = 'P1'
	else:
		winner = 'P2'
	return winner

def play_game(game_num):
	'''Function plays a game of Seventeen. 

	Function first retrieves the marbles removed by Player 1, 
	then alternates between Player 2 (the computer) and Player 1.
	The function keeps track of the play sequence, marbles 
	remaining in the jar, and determines the winner at the end of the game.
	'''
	initial_marbles = 17
	play_sequence = []
	marbles_remaining = initial_marbles - sum(play_sequence)

	#Play the game while there are still marbles in the jar.
	while sum(play_sequence) < initial_marbles:						
		if len(play_sequence)%2 == 0:								#Player 1's turn
			turn_index_num = len(play_sequence)/2
			play_sequence.append(user_turn(marbles_remaining, game_num, turn_index_num))
		else:														#Computer's turn
		 	play_sequence.append(computer_turn(marbles_remaining))
		
		marbles_remaining = initial_marbles - sum(play_sequence)
	
	winner = determine_winner(play_sequence)	
	return play_sequence, winner

def play_multiple_games(user_play_sequences):
	'''Plays the game for each user play sequence
	in the given file and prints the play sequences, 
	winners, and losers for each game to a new file.
	'''
	with open('i206_placein_output2_AndreaGagliano.txt', 'w') as f:
		P1_wins = 0
		P2_wins = 0	
		for i, game in enumerate(user_play_sequences):
			play_sequence, winner = play_game(i)
			play_sequence = [str(value) for value in play_sequence]
			play_sequence = '-'.join(play_sequence)
			f.write('Game #{0}. Play sequence: {1}. Winner: {2}\n'.format((i+1), play_sequence, winner))
			if winner == 'P1':
				P1_wins += 1
			else:
				P2_wins += 1
		f.write('Player 1 won {0} times; Player 2 won {1} times.'.format(P1_wins, P2_wins))
	

#########################################################

def main():
	'''Plays the game of seventeen. 

	Player 1 (text file) and Player 2 (computer) alternate
	removing 1, 2, or 3 marbles from a jar of seventeen marbles.
	The player who removes the last marble from the jar
	loses the game.
	'''
	play_multiple_games(get_user_play_sequences())


if __name__ == "__main__":
	main()