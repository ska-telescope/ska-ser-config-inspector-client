# coding: utf-8

"""
    config-inspector

    Get the configurational status of a currently deployed product in terms of its sub     configurational items and their corresponding health

    The version of the OpenAPI document: 0.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ska_ser_config_inspector_client.api.tango_devices_and_their_deployment_status_api import TangoDevicesAndTheirDeploymentStatusApi


class TestTangoDevicesAndTheirDeploymentStatusApi(unittest.TestCase):
    """TangoDevicesAndTheirDeploymentStatusApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TangoDevicesAndTheirDeploymentStatusApi()

    def tearDown(self) -> None:
        pass

    def test_get_device_from_a_given_sub_chart_chart_name_device_name_get(self) -> None:
        """Test case for get_device_from_a_given_sub_chart_chart_name_device_name_get

        Get Device From A Given Sub Chart
        """
        pass

    def test_search_release_for_devices_search_devices_get(self) -> None:
        """Test case for search_release_for_devices_search_devices_get

        Search Release For Devices
        """
        pass

    def test_search_sub_chart_for_devices_chart_name_search_devices_get(self) -> None:
        """Test case for search_sub_chart_for_devices_chart_name_search_devices_get

        Search Sub Chart For Devices
        """
        pass


if __name__ == '__main__':
    unittest.main()
