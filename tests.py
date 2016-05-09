# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.0
# Created 7/3/16



test_cases = {
    "is_valid_play":
    [
        # can only play the single card held if phase 1 or 19 (or end of phase)
        ("""submission.is_valid_play('0D', ('9D', '9S', '3S'), ('0D',))""", True), 
        ("""submission.is_valid_play('AH', ('9D', '9S', '3S'), ('AH',))""", True), 
        ("""submission.is_valid_play('AH', ('9D', '9S', '3S'), ('2H',))""", False), 

        # must follow suit if held
        ("""submission.is_valid_play('0D', ('9D', '9S', '3S'), ('0D', 'AH'))""", True), 
        ("""submission.is_valid_play('AH', ('9D', '9S', '3S'), ('0D', 'AH'))""", False), 
        ("""submission.is_valid_play('AS', ('9D', '9S', 'KS'), ('0D', 'AS'))""", False), 
    ],

    "score_phase":
    [
        # phase 1/19 tests
        ("""submission.score_phase((0, 0, 0, 0), (('9D', '9S', '3S', '0D'),), '2D')""", (10, 10, 10, 1)),
        ("""submission.score_phase((0, 0, 0, 1), (('9D', '9S', '3S', '0D'),), '2D')""", (10, 10, 10, 11)),
        ("""submission.score_phase((0, 0, 0, 0), (('9D', '9S', '3S', '0D'),), '2S')""", (10, 1, 10, 10)),

        # phase two tests
        ("""submission.score_phase((0, 0, 0, 0), (('9D', '9S', '3S', '0D'), ('3D', '8S', 'AS', 'JS')), '2D')""", (10, 10, 10, 2)),
        ("""submission.score_phase((1, 0, 0, 1), (('9D', '9S', '3S', '0D'), ('3D', '8S', 'AS', 'JS')), '2D')""", (0, 10, 10, 2)),
        ("""submission.score_phase((0, 0, 0, 2), (('9D', '9S', '3S', '0D'), ('3D', '8S', 'AS', 'JS')), '2D')""", (10, 10, 10, 12)),
    ],

    "play":
    [
#        curr_trick, hand, prev_tricks, player_no, deck_top, phase_bids
        ("""submission.play((), ('KD',), (), 0, 'AS', (1, 0, 0, 0))""", 'KD'),
        ("""submission.play(('AD',), ('KD', '2H', '3C'), (), 1, 'AS', (2, 1, 1, 1))""", 'KD'),
        ("""submission.play(('AD', 'KS'), ('2D', '2H', '3C'), (), 2, 'AS', (1, 2, 0, 0))""", '2D'),
    ],
    
    "bid":
    [
#  bid(hand, player_no, phase_no, deck_top)
        ("""submission.bid(('AS', 'KS', 'QS', 'JS'), 1, 4, '0S')""", 1),
        ("""submission.bid(('AS', 'KS', 'QS', 'JS', '0S', '9S', '8S', '7S'), 3, 8, '2S')""", 2),
        ("""submission.bid(('AS', 'KS', 'QS', 'JS', '0S', '9S', '8S', '7S', '6S', '5S'), 0, 10, '2S')""", 0),
        ("""submission.bid(('AS', 'KS', 'QS', 'JS', '0S', '9S', '8S', '7S', '6S', '5S'), 3, 10, '2S', True)""", 0),
        ("""submission.bid(('AS', 'KS', 'QS', 'JS', '0S', '9S', '8S', '7S'), 0, 12, '3S')""", 2),
        ("""submission.bid(('AS', 'KS', 'QS', 'JS'), 0, 16, '3S')""", 1),
    ]        

}
