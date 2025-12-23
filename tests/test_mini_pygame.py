import unittest
from pygame import Surface
from pygame.sprite import Sprite, Group
from src.mini_pygame import *
from src.constants import CARD_PATHS


class TestResolver(unittest.TestCase):

    def test_resolves_image(self):
        image = resolve_image(CARD_PATHS["error"])
        self.assertIsInstance(image, Surface)

class TestPrototype(unittest.TestCase):

    def test_Prototype_initializes(self):
        spr = Prototype()
        self.assertIsInstance(spr, Prototype)
    
    # this needs more test cases tbh
    
class TestGroup(unittest.TestCase):
    def setUp(self) -> None:
        self.sprites = [Sprite(), Sprite()]
        self.spr1, self.spr2 = self.sprites
        self.length_of_group = 2
        self.group = Group(*self.sprites)

    def test_Group_initializes(self):
        self.assertIsInstance(self.group, Group)
    
    def test_Group_contains(self):
        spr = Sprite()
        self.group.add(spr)
        self.assertTrue(spr in self.group)
    
    def test_Group_len(self):
        self.assertEqual(len(self.group), self.length_of_group)
    
    def test_Group_bool_True(self):
        self.assertTrue(self.group)
    
    def test_Group_bool_False(self):
        group = Group()
        self.assertFalse(group)
    
    def test_Group_iter(self):
        self.assertEqual(list(self.group), self.sprites)
    
    def test_Group_sprites(self):
        self.assertEqual(self.group.sprites(), self.sprites)
    
    def test_Group_copy(self):
        group = self.group.copy()
        self.assertEqual(group.sprites(), self.group.sprites())
    
    # with the following tests, i need to ensure that the functions work with iterables

    def test_Group_add(self):
        spr1, spr2 = Sprite(), Sprite()
        self.group.add(spr1, spr2)
        self.assertEqual(len(self.group), self.length_of_group + 2)

    def test_Group_add_with_iterable(self):
        sprites = iter([Sprite(), Sprite()])
        self.group.add(sprites) # type: ignore
        self.assertEqual(len(self.group), self.length_of_group + 2) # gets 3 instead of 4

    def test_Group_remove(self):
        self.group.remove(self.spr2)
        self.assertNotIn(self.spr2, self.group)

    """We lazy and we know it 
    def test_Group_remove_with_iterable(self):
        pass

    def test_Group_has(self):
        pass

    def test_Group_has_with_iterable(self):
        pass

    # im not sure how to test the rest of the functions in this class TBH
    """

