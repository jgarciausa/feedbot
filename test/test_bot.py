import unittest
from test import BaseTest
from feedbot import bot


class BotTest(BaseTest):

    def test_main(self):
        bot.main(self.config_tree, 'foo_status.xml', self.status_tree_empty)


if __name__ == '__main__':
    unittest.main()
