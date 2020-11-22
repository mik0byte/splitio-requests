# -*- coding: utf-8 -*-
"""Utils methods suite"""

from marshmallow import EXCLUDE, RAISE


class Utils:
    """Utils methods class"""

    @classmethod
    def get_unknown_field_handler(cls, handler_name: str) -> str:
        """
        Schemas unknown field handler retriever

        :param handler_name: Name of handler
        :return: Handler type or None
        """
        unknown_field_handlers = {
            'EXCLUDE': EXCLUDE,
            'RAISE': RAISE
        }

        if not isinstance(handler_name, str):
            raise TypeError('Handler should be string')

        handler = unknown_field_handlers.get(handler_name.upper())

        if handler is None:
            raise ValueError(f"There is no such handler '{handler_name}'")

        return handler
