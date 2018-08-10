import unittest
from Bio.Alphabet import generic_dna, generic_protein
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment
from alv.alignment import aaAlignment

class TestAlignment(unittest.TestCase):
    def setUp(self):
        simple_al = MultipleSeqAlignment([
             SeqRecord(Seq("AR", generic_protein), id="Alpha"),
             SeqRecord(Seq("AR", generic_protein), id="Beta_"),
             SeqRecord(Seq("AS", generic_protein), id="Gamma"),
         ])
        self.al = aaAlignment(simple_al)
 
    def test_summarize_columns(self):
        self.assertEqual(self.al._summarize_columns()[0]['A'], 3)
        self.assertEqual(self.al._summarize_columns()[1]['R'], 2)
        self.assertEqual(self.al._summarize_columns()[1]['S'], 1)
        self.assertEqual(self.al._summarize_columns()[1]['A'], 0)

    def test_accession_length(self):
        for acc in self.al.accessions():
            self.assertEqual(len(acc), 5)

if __name__ == '__main__':
    unittest.main()
    

