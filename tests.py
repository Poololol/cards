import unittest
from cardGroup import CardGroup
from card import Card

class TestCardGroup(unittest.TestCase):
    def setUp(self):
        card1 = Card(11, 0)
        card2 = Card(13, 1)
        card3 = Card(10, 2)
        card4 = Card(3, 3)
        card5 = Card(1, 2)
        self.cards = [card1, card2, card3, card4, card5]
        self.card_group = CardGroup(self.cards)

    def test_isFlush(self):
        flush_cards = [Card(value, 1) for value in range(1, 6)]
        flush_group = CardGroup(flush_cards)
        self.assertTrue(flush_group.isFlush())
        self.assertFalse(self.card_group.isFlush())

    def test_isStraight(self):
        straight_cards = [Card(value, 1) for value in range(1, 6)]
        straight_group = CardGroup(straight_cards)
        self.assertTrue(straight_group.isStraight())
        self.assertFalse(self.card_group.isStraight())

    def test_isXOfAKind(self):
        kind_cards = [Card(1, 1) for _ in range(3)]
        kind_cards.extend([Card(2, 2) for _ in range(2)])
        self.assertEqual(self.card_group.isXOfAKind(1), 5)
        self.assertEqual(self.card_group.isXOfAKind(2), 0)
        self.assertEqual(CardGroup(kind_cards).isXOfAKind(3), 1)

    def test_getPokerHand(self):
        self.assertEqual(self.card_group.getPokerHand(), 'High Card')
        flush_cards = [Card(value, 1) for value in range(1, 6)]
        flush_group = CardGroup(flush_cards)
        self.assertEqual(flush_group.getPokerHand(), 'Straight Flush')

    def test_sort(self):
        unsorted_cards = [Card(3, 1), Card(1, 1), Card(2, 1)]
        unsorted_group = CardGroup(unsorted_cards)
        unsorted_group.sort()
        self.assertEqual([card.value for card in unsorted_group.cards], [3, 2, 1])
        unsorted_group.sort(method='Suit')
        self.assertEqual([card.value for card in unsorted_group.cards], [1, 2, 3])

    def test_addCards(self):
        new_card = Card(10, 2)
        self.card_group.addCards([new_card])
        self.assertIn(new_card, self.card_group.cards)

    def test_removeCard(self):
        card_to_remove = self.cards[0]
        self.card_group.removeCard(card_to_remove)
        self.assertNotIn(card_to_remove, self.card_group.cards)

    def test_len(self):
        self.assertEqual(len(self.card_group), len(self.cards))

    def test_getitem(self):
        self.assertEqual(self.card_group[0], self.cards[0])

    def test_setitem(self):
        new_card = Card(10, 2)
        self.card_group[0] = new_card
        self.assertEqual(self.card_group[0], new_card)

if __name__ == '__main__':
    unittest.main()