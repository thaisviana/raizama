
from django.contrib.admin.filters import (
    RelatedOnlyFieldListFilter, AllValuesFieldListFilter, DateFieldListFilter, FieldListFilter
)


class AllValuesDropdownFilter(AllValuesFieldListFilter):
    template = 'admin/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'admin/dropdown_filter.html'


class DateDropdownFilter(DateFieldListFilter):
    template = 'admin/dropdown_filter.html'


class WeekdayDropdownFilter(FieldListFilter):
    display_title = "Dia da semana"
    template = 'admin/dropdown_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_weekday = '%s__week_day' % field_path
        self.date_params = {k: v for k, v in params.items() if k.startswith(self.lookup_kwarg_weekday)}

        self.links = (
            ('Qualquer dia', {}),
            ('segunda-feira', {
                self.lookup_kwarg_weekday: '2'
            }),
            ('terça-feira', {
                self.lookup_kwarg_weekday: '3'
            }),
            ('quarta-feira', {
                self.lookup_kwarg_weekday: '4'
            }),
            ('quinta-feira', {
                self.lookup_kwarg_weekday: '5'
            }),
            ('sexta-feira', {
                self.lookup_kwarg_weekday: '6'
            }),
            ('sábado', {
                self.lookup_kwarg_weekday: '7'
            }),
            ('domingo', {
                self.lookup_kwarg_weekday: '1'
            }),
        )
        super().__init__(field, request, params, model, model_admin, field_path)
        if self.display_title is not None:
            self.title = self.display_title

    def expected_parameters(self):
        params = [self.lookup_kwarg_weekday]
        return params

    def choices(self, changelist):
        for title, param_dict in self.links:
            yield {
                'selected': self.date_params == param_dict,
                'query_string': changelist.get_query_string(param_dict, [self.lookup_kwarg_weekday]),
                'display': title,
            }


class HourDropdownFilter(FieldListFilter):
    display_title = "Hora"
    template = 'admin/dropdown_filter.html'

    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg_hour = '%s__hour' % field_path
        self.date_params = {k: v for k, v in params.items() if k.startswith(self.lookup_kwarg_hour)}

        self.links = [
            ('Qualquer hora', {}),
        ]
        for t in range(24):
            time = ('0%s' % t)[-2:]
            self.links.append((
                'entre %s:00 e %s:59' % (time, time), {
                    self.lookup_kwarg_hour: str(t)
                }
            ))

        super().__init__(field, request, params, model, model_admin, field_path)
        if self.display_title is not None:
            self.title = self.display_title

    def expected_parameters(self):
        params = [self.lookup_kwarg_hour]
        return params

    def choices(self, changelist):
        for title, param_dict in self.links:
            yield {
                'selected': self.date_params == param_dict,
                'query_string': changelist.get_query_string(param_dict, [self.lookup_kwarg_hour]),
                'display': title,
            }
