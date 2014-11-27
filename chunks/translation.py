# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from . import models


class ChunkOpts(TranslationOptions):
    fields = ('content', )


class ChunkGroupOpts(TranslationOptions):
    fields = ('content', )


class ChunkMediaOpts(TranslationOptions):
    fields = ('title', 'desc', 'media', )


translator.register(models.Media, ChunkMediaOpts)
translator.register(models.Group, ChunkGroupOpts)
translator.register(models.Chunk, ChunkOpts)
