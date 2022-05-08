from unittest import TestCase
from mark.graders.graham import GrahamGrader, StageMarkData


class TestGraders(TestCase):
    def test_graham_total(self):
        correct = [1, (1,1,1,1), '1111', lambda x: x+1]
        answer = [1, (1,1,1,1), '1111', lambda x: x+1]
        mark = GrahamGrader.grade(correct, answer)
        self.assertEqual(mark[0], 0.75)
        markdata = [
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=0.25, min_mark=0), 0.25), 
            (StageMarkData(max_mark=1.25, min_mark=0), 0)
        ]
        self.assertEqual(mark[1], markdata)

