from typing import Callable, Iterable
from mark.markdata import MarkData, Mistake
from collections import Counter
from itertools import cycle


def default_grading(correct, answer, sub=0.0):
    return [] if correct == answer else [Mistake(sub=sub)]


def iterable_grading(correct: Iterable, answer: Iterable, sub=0.0, big_sub=0.0):
    diff = len(correct) - len(answer)
    extra = [
        Mistake(sub=sub, big_sub=big_sub, data="Too many items")
        for _ in range(-diff)
    ] if diff < 0 else [
        Mistake(sub=sub, big_sub=big_sub, data="Too few items")
        for _ in range(diff)
    ]

    return [
        Mistake(sub=sub, big_sub=big_sub, systematic=big_sub>0)
        for pair in zip(correct, answer)
        if pair[0] != pair[1]
    ] + extra


def mistakes_sub_pairs(mistakes):
    counter = Counter(mistakes)
    return {
        mistake: mistake.big_sub if mistake.systematic and count > 1 else mistake.sub
        for mistake, count
        in counter.items()
    }


class Grader:
    markdata: MarkData
    stage_grading_methods: Iterable[Callable] = cycle([default_grading])

    @classmethod
    def grade(cls, correct, answer):
        mistakes = [
            method(correct_stage, answer_stage)
            for method, correct_stage, answer_stage 
            in zip(cls.stage_grading_methods, correct, answer)
        ]

        by_stages = list(zip(cls.markdata.stages, mistakes))

        by_stages_counter = [
            (stage, mistakes_sub_pairs(mistakes))
            for stage, mistakes
            in by_stages
        ]

        marks_per_stage = [
            (stage, max(stage.min_mark, stage.max_mark - sum(counter.values())))
            for stage, counter
            in by_stages_counter
        ]

        mark = sum(mark for stage, mark in marks_per_stage)

        return mark, marks_per_stage
