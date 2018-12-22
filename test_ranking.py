import th_poker_ranking


def test_two_cards():
    pair = th_poker_ranking.ranker('2C 2C')
    ace_high = th_poker_ranking.ranker('AC 3C')
    assert pair > ace_high
    
    king_high = th_poker_ranking.ranker('KC 3C')
    assert ace_high > king_high
    
    
def test_high_card_kicker():
    ace_high_kicker_2card = th_poker_ranking.ranker('AC KC')
    ace_high_2card = th_poker_ranking.ranker('AC 3C')
    assert ace_high_kicker_2card > ace_high_2card
    
    ace_high_kicker = th_poker_ranking.ranker('AC KC 2S 8H 4D')
    ace_high = th_poker_ranking.ranker('AC 3C 2S 8H 4D')
    assert ace_high_kicker > ace_high

    
def test_hand_types():    
    straight_flush = th_poker_ranking.ranker('2C 3C 4C 5C 6C')
    
    four_of_kind  = th_poker_ranking.ranker('2S 2H 2D 2C AC')
    assert straight_flush > four_of_kind

    full_house = th_poker_ranking.ranker('2S 2H 2D 3C 3C')
    assert four_of_kind > full_house

    flush = th_poker_ranking.ranker('2C 3C AC TC 6C')
    assert full_house > flush
    
    straight = th_poker_ranking.ranker('2S 3H 4D 5C 6C')
    assert flush > straight

    three_of_kind = th_poker_ranking.ranker('2S 2H 2D 5C AC')
    assert straight > three_of_kind

    two_pair = th_poker_ranking.ranker('2S 2H 4D 4C AC')
    assert three_of_kind > two_pair

    pair = th_poker_ranking.ranker('2S 2H 4D 5C AC')
    assert two_pair > pair

    ace_high = th_poker_ranking.ranker('2S 3H 4D 7C AC')
    assert pair > ace_high

    seven_high = th_poker_ranking.ranker('2S 3H 4D 6C 7C')
    assert ace_high > seven_high
    
    
def test_straght_flushes():
    straight_flush = th_poker_ranking.ranker('2C 3C 4C 5C 6C')
    straight_flush_2 = th_poker_ranking.ranker('7C 3C 4C 5C 6C')
    assert straight_flush_2 > straight_flush