


class NameTestCase(unittest.TestCase):
    def test_title_name(self):
        formatted_name=get_formatted_name('tom','lee')
        self.assertEqual(formatted_name,'Tom Lee')
if __name__=='__main__':
    unittest.main()



