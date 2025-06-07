###Elections###

SLO.seat_count		 			-> Variable, total seat count in parliament
SLO.parliament_level 				-> Variable, 0 means Slovakia, 1 means Europe
SLO.parliament_threshold			-> Variable, what % of votes are needed to enter the parliament
SLO.election_states 				-> Array, what states should we perform elections in. Only updates when we hold an election
SLO.subdivision_states				-> Array, every state that can be an election state when we form Europe
SLO.language					-> Variable, 0 for Slovakia, 1 for English
SLO.seat_array					-> Array, how many seats does each party have?
SLO.seats_needed_for_majority			-> Variable, how many seats are needed for a majority?
SLO.party_campaigning_as			-> Variable, which party are we campaigning for?
SLO.parties_in_government			-> Array, which parties are in government?
SLO.parties_in_opposition			-> Array, which parties are in opposition?
SLO.government_seat_count			-> Variable, total government seat count
SLO.opposition_seat_count			-> Variable, total opposition seat count

SLO.party_names_long_no_colour_array		-> Array
SLO.party_names_long_coloured_array		-> Array
SLO.party_names_short_no_colour_array		-> Array
SLO.party_names_short_coloured_array		-> Array

SLO.gui_gridbox_width				-> Variable, width of our parliament
SLO.gui_party_dot_entry_size			-> Variable, size of a dot
SLO.gui_bottom_y_pos				-> Variable, bottom row y pos
SLO.parliament_x_pos_array			-> Variable
SLO.parliament_y_pos_array			-> Variable
SLO.parliament_frame_array			-> Variable

<state>.x0, x1 ,y0, y1				-> Variables, used to define the bounding box of each state
<state>.x_pos, y_pos				-> Variables, used to define the top x and y pos in the gui
<state>.overlay_token, progressbar_token	-> Variables, GFX tokens
<state>.name_token				-> Variable, name token
<state>.party_popularity			-> Array, used to define party popularities
<state>.seat_count				-> Variable, how many seats does this subdivision have
<state>.seat_array				-> Array, how many seats does each party have?
<state>.subdivision_states			-> Array, which states are part of the subdivision

SLO.previous_election_turnout			-> Variable, turnout in the country. Turnout was mandatory, so between 85-95
SLO.previous_election_results			-> Array, percentage vote of each party at the last election
SLO.previous_election_votes			-> Array, vote count of each party at the last election
SLO.previous_election_party_position		-> Array, position of each party at the last election results. Index = party, value = position
SLO.previous_election_position_party		-> Array, position of each party at the last election results. Index = position, value = party
SLO.previous_election_margin_of_victory		-> Variable, gap between first and second place nationally
SLO.previous_election_seat_array		-> Array, how many seats each party got nationally at the last election
SLO.previous_election_date			-> Variable, date of the last election
<state>.previous_election_turnout		-> Variable, turnout in the state. Turnout was mandatory, so between 85-95
<state>.previous_election_results		-> Array, percentage vote of each party at the last election
<state>.previous_election_votes			-> Array, vote count of each party at the last election
<state>.previous_election_party_position	-> Array, position of each party at the last election results. Index = party, value = position
<state>.previous_election_position_party	-> Array, position of each party at the last election results. Index = position, value = party
<state>.previous_election_margin_of_victory	-> Variable, gap between first and second place in a state
<state>.previous_election_victor_popularity	-> Variable, between 00-97. Floor divide by 14 to get the victor, modulo 14 to get the margin of victory (2% increments)
<state>.previous_election_seat_array		-> Array, how many seats each party got in this state at the last election


SLO_initialise_parliament			-> Effect, initialises parliament
SLO_divide_seats				-> Effect, gets seat counts for each state / subdivision
SLO_hold_election				-> Effect, holds an election
SLO_initialise_europe_mechanics			-> Effect, changes election type from Slovakia to Europe
SLO_get_active_election_states			-> Effect, gets the election_states array if we've formed Europe
SLO_get_map_positions				-> Effect, gets the x_pos and y_pos variables
STATE_set_popularities_to_100			-> Effect, sets the state's party popularities to sum to 100
SLO_change_language				-> Effect, changes the language to and from Slovak & English
SLO_update_parliament_position_gfx		-> Effect, updates the parliament dots positions
SLO_update_government_opposition_seat_counts	-> Effect, gets how many parliamentarians are in government vs opposition

SLO.SLO_electoral_map_selected_state		-> Variable, set to SLO for national results or to <state> for state results in the GUI