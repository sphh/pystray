import unittest

import pystray


class MenuDescriptorTests(unittest.TestCase):
    def test_item_name(self):
        """Tests that the text is set correctly.
        """
        self.assertEqual(
            'Test entry',
            item('Test entry', callable).text)

    def test_item_call(self):
        """Tests that calling a menu item works as expected.
        """
        data = []
        item('', lambda _: data.append(True))(None)
        self.assertEqual(
            [True],
            data)

    def test_menu_construct(self):
        """Tests menu construction from tuples.
        """
        self.assertEqual(
            '''Menu:
    Test entry one
    Test entry two
    Test entry three
    Test entry four''',
        str(menu(
            ('Test entry one', callback),
            ('Test entry two', callback),
            item('Test entry three', callback),
            item('Test entry four', callback))))

    def test_menu_separator(self):
        """Tests menu construction with separators.
        """
        # Separators at the head and tail are ignored
        self.assertEqual(
            '''Menu:
    Test entry one
    - - - -
    Test entry two''',
        str(menu(
            '----',
            '----',
            item('Test entry one', callback),
            '----',
            hidden('Test entry hidden', callback),
            '----',
            item('Test entry two', callback),
            '----',
            '----')))

    def test_menu_default_invalid(self):
        """Tests that an invalid number of default menu items fails.
        """
        with self.assertRaises(ValueError):
            menu(
                item('one', callback, default=True),
                item('two', callback, default=True))

    def test_menu_default_callable(self):
        """Tests that the default menu item is activated when calling the menu.
        """
        self.assertEqual(
            'test result',
            menu(
                item('one', lambda _: 'test result', default=True))(None))


def menu(*args, **kwargs):
    """A wrapper around the :class:`pystray.Menu` constructor.
    """
    return pystray.Menu(*args, **kwargs)


def item(*args, **kwargs):
    """Creates a visible menu item.
    """
    return pystray.MenuItem(True, *args, **kwargs)


def hidden(*args, **kwargs):
    """Creates an invisible menu item.
    """
    return pystray.MenuItem(False, *args, **kwargs)


def separator():
    """A wrapper around :attr:`pystray.Menu.SEPARATOR`.
    """
    return pystray.Menu.SEPARATOR


def callback(*args, **kwargs):
    """A dummy callback function.
    """
    pass