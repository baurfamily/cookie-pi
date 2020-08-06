from gsct.models import Sale, Box

BOX_TYPES = {
    'thinmints': Box(cost=5, flavor='Thin Mints'),
    'tagalongs': Box(cost=5, flavor='Tag-Alongs'),
    'smores':    Box(cost=6, flavor="S'mores"),
}

class TestSale:
    def test_init(self):
        s = Sale()
        assert s.box_count() == 0
        assert s.total() == 0


    def test_checking_count(self):
        s = Sale()

        s.add_box( BOX_TYPES['thinmints'] )
        s.add_box( BOX_TYPES['tagalongs'] )
        s.add_box( BOX_TYPES['tagalongs'] )
        
        assert s.box_count() == 3


    def test_checking_total(self):
        s = Sale()

        s.add_box( BOX_TYPES['thinmints'] )
        s.add_box( BOX_TYPES['smores'] )
        
        assert s.total() == 11

