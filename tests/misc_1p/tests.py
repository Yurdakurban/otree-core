# -*- coding: utf-8 -*-
from __future__ import division
from . import views
from otree.api import Bot, SubmissionMustFail, Currency as c
import random



class PlayerBot(Bot):

    def play_round(self):

        yield SubmissionMustFail(
            views.ErrorMessage,
            {'add100_1': 1, 'add100_2': 98}
        )
        yield (views.ErrorMessage, {'add100_1': 1, 'add100_2': 99})
        yield SubmissionMustFail(views.FieldErrorMessage, {'even_int': 1})
        yield (views.FieldErrorMessage, {'even_int': 2})
        yield SubmissionMustFail(views.DynamicChoices, {'dynamic_choices': 'c'})
        yield (
            views.DynamicChoices,
            {'dynamic_choices': random.choice(['a', 'b'])}
        )
        # if using a radio widget, there should not be a ------ choice;
        # that's only for dropdowns
        # FIXME: there's no HTML in this game!
        assert '-----' not in self.html
        yield (views.RadioWidgets, {'radio': c(1), 'dynamic_radio': 'a'})
        yield SubmissionMustFail(views.MinMax, {'min_max': 2})
        yield (views.MinMax, {'min_max': 5})
        yield SubmissionMustFail(views.DynamicMinMax, {'dynamic_min_max': 4})
        yield (views.DynamicMinMax, {'dynamic_min_max': 3})
        yield (views.Blank)
