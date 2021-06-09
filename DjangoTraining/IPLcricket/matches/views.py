from django.db.models import Count, Q, Sum
from django.shortcuts import render
from matches.models import MatchesPlayed, Deliveries
from django.views.generic import View
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world!")


def winning_team(request):
    logger.debug('winning_team - start')
    request_path = request.path.strip('/').split('/')[-1]
    logger.info(f'request_path:{request_path}')

    winning_teams = tuple(MatchesPlayed.objects.values_list('winner', flat=True).distinct())

    city_winner = MatchesPlayed.objects.values('city', 'winner').annotate(Count('winner', distinct=True))

    _context = {
        'winning_teams': winning_teams,

    }
    return render(request, 'index.html', _context)


class MyClassView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        logger.debug('MyClassView - get - start')
        try:
            _context = {}
            return render(request, self.template_name, _context, status=200)
        except Exception as ex:
            logger.error(repr(ex))
            return render(request, self.template_name, {'error_message': repr(ex)}, status=500)
