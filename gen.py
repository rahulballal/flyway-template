#!/usr/bin/env python

import time


class TemplateGenerator:

    def __init__(self):
        self.current_schema_prefix = 'V1'
        self.jira_ticket = ''
        self.short_description = ''
        self.full_description = ''

    def get_jira_ticket(self):
        good_to_go = False

        while not good_to_go:
            self.jira_ticket = raw_input('Enter the JIRA ticket for this migration:\n')
            str_len = len(self.jira_ticket)
            good_to_go = str_len > 0
            if not good_to_go:
                print 'You must enter a JIRA ticket number'

    def get_short_description(self):
        good_to_go = False

        while not good_to_go:
            self.short_description = raw_input('Enter a short description of the migration (< 20 chars):\n')
            str_len = len(self.short_description)
            good_to_go = 21 > str_len > 0
            if not good_to_go:
                print 'Invalid length for short description \n'

    def get_full_description(self):
        good_to_go = False

        while not good_to_go:
            self.full_description = raw_input('Enter full description of the migration (< 100 chars):\n')
            str_len = len(self.full_description)
            good_to_go = 101 > str_len > 0
            if not good_to_go:
                print 'Invalid length for short description \n'

    def generate_file(self):
        file_name = './sql/{}_{}__{}.sql'.format(self.current_schema_prefix, int(time.time()), self.short_description)
        print 'Genrating migration file : {}\n'.format(file_name)
        file_handle = open(file_name, 'w')
        file_handle.write('# JIRA TICKET: {} \n'.format(self.jira_ticket))
        file_handle.write('# SHORT DESC: {} \n'.format(self.short_description))
        file_handle.write('# FULL DESCRIPTION: {} \n'.format(self.full_description))
        file_handle.write('# ADD SQL BELOW \n')
        file_handle.close()

    def run(self):
        self.get_jira_ticket()
        self.get_short_description()
        self.get_full_description()
        self.generate_file()

instance = TemplateGenerator()
instance.run()
