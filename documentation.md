###Elections###

SLO.parliament_seat_total 			-> Variable, total seat count in parliament
SLO.parliament_level 				-> Variable, 0 means Slovakia, 1 means Europe
SLO.parliament_threshold			-> Variable, what % of votes are needed to enter the parliament
SLO.election_states 				-> Array, what states should we perform elections in
SLO.subdivision_states				-> Array, every state that can be an election state when we form Europe

<state>.x0, x1 ,y0, y1				-> Variables, used to define the bounding box of each state
<state>.x_pos, y_pos				-> Variables, used to define the top x and y pos in the gui
<state>.overlay_token, progressbar_token	-> Variables, GFX tokens
<state>.name_token				-> Variable, name token
<state>.party_popularity			-> Array, used to define party popularities
<state>.seat_count				-> Variable, how many seats does this subdivision have
<state>.subdivision_states			-> Array, which states are part of the subdivision

SLO.previous_election_states			-> Array, states that voted in the last election
SLO.previous_election_turnout			-> Variable, turnout in the country. Turnout was mandatory, so between 85-95
SLO.previous_election_resuts			-> Array, percentage vote of each party at the last election
SLO.previous_election_votes			-> Array, vote count of each party at the last election
<state>.previous_election_turnout		-> Variable, turnout in the state. Turnout was mandatory, so between 85-95
<state>.previous_election_resuts		-> Array, percentage vote of each party at the last election
<state>.previous_election_votes			-> Array, vote count of each party at the last election
<state>.previous_election_party_position	-> Array, position of each party at the last election results. Index = party, value = position
<state>.previous_election_position_party	-> Array, position of each party at the last election results. Index = position, value = party
<state>.previous_election_victor_popularity	-> Variable, between 00-99. First digit represents which party won, second by how much (3% increments)


SLO_initialise_parliament			-> Effect, initialises parliament
SLO_divide_seats				-> Effect, gets seat counts for each state / subdivision
SLO_hold_election				-> Effect, holds an election
SLO_initialise_europe_mechanics			-> Effect, changes election type from Slovakia to Europe