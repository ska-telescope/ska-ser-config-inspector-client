# coding: utf-8

"""
    config-inspector

    Get the configurational status of a currently deployed product in terms of its sub     configurational items and their corresponding health

    The version of the OpenAPI document: 0.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ska_ser_config_inspector_client.models.chart_summary import ChartSummary

class TestChartSummary(unittest.TestCase):
    """ChartSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChartSummary:
        """Test ChartSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChartSummary`
        """
        model = ChartSummary()
        if include_optional:
            return ChartSummary(
                chart = '',
                version = ''
            )
        else:
            return ChartSummary(
                chart = '',
                version = '',
        )
        """

    def testChartSummary(self):
        """Test ChartSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()