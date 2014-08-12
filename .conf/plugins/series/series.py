# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pelican import signals
from pelican.generators import Generator, Article
from pelican.utils import slugify
from collections import defaultdict
from functools import partial
from operator import attrgetter

class SeriesGenerator(Generator):
    def __init__(self, *args, **kwargs):
        super(SeriesGenerator, self).__init__(*args, **kwargs)
        self.series = defaultdict(list)
        self.series_slug = {}
        self.base_slug = self.settings.get('SERIES_SLUG', 'series')

    def generate_context(self):
        series_slugs = {}
        for article in self.context['articles']:
            if article.status.lower() == "published" and hasattr(article, 'series'):
                slug = slugify(article.series, self.settings.get('SLUG_SUBSTITUTIONS', ()))
                self.series[slug].append(article)

                if article.series not in self.series_slug:
                    self.series_slug[article.series] = slug

    def generate_output(self, writer):
        write = partial(writer.write_file, relative_urls=self.settings['RELATIVE_URLS']) 
        template = self.get_template('series')
        for title,slug in self.series_slug.items():
            save_as = self.settings.get("SERIES_SAVE_AS", self.base_slug+'/{slug}.html')
            save_as = save_as.format(slug=slug)
            articles = self.series[slug][:]
            articles.sort(key=attrgetter('date' ))
            dates = self.series[slug]
            write(save_as, template, self.context, articles=articles,
                    paginated={'articles': articles, 'dates':dates}, URL=save_as, TITLE=title)

def get_generators(generators):
    return SeriesGenerator

def register():
    signals.get_generators.connect(get_generators)
