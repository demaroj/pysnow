# -*- coding: utf-8 -*-


class Report(object):
    def __init__(self, resource, generator_size, session):
        """Constructs a report, keeping track of resources, requests and responses

        :param resource: :class:`pysnow.Resource <Resource>` object
        :param generator_size: Generator size (integer)
        :param session: :class:`requests.Session <Session>` object
        """
        self.x_total_count = -1
        self.consumed_records = 0
        self.responses = []
        self.generator_size = generator_size
        self.request_params = None
        self.resource = resource
        self.session = session

    def set_x_total_count(self, count):
        """Sets the x-total-count (from response header)

        :param count: total count
        """
        self.x_total_count = int(count)

    def add_consumed_count(self, records):
        """Adds the number of records present in a response to the :prop:`consumed_count`

        :param records: response content record count
        """
        self.consumed_records = self.consumed_records + int(records)

    def add_response(self, response):
        """Adds a :class:`requests.Response <Response>` object to the :prop:`responses` list

        :param response: :class:`requests.Response <Response>` object
        """
        self.responses.append(response)

    def __getitem__(self, key):
        return self.__getattribute__(key)

    def __repr__(self):
        return "%s %s" % (self.__class__, self.__dict__)
