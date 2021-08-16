# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Integration Tests for DataVirtualizationV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_data_virtualization_on_cloud.data_virtualization_v1 import *

# Config file name
config_file = 'data_virtualization_v1.env'

class TestDataVirtualizationV1():
    """
    Integration Test Class for DataVirtualizationV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.data_virtualization_service = DataVirtualizationV1.new_instance(
                )
            assert cls.data_virtualization_service is not None

            cls.config = read_external_sources(
                DataVirtualizationV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_datasource_connections(self):

        list_datasource_connections_response = self.data_virtualization_service.list_datasource_connections()

        assert list_datasource_connections_response.get_status_code() == 200
        datasource_connections_list = list_datasource_connections_response.get_result()
        assert datasource_connections_list is not None

    @needscredentials
    def test_add_datasource_connection(self):

        # Construct a dict representation of a PostDatasourceConnectionParametersProperties model
        post_datasource_connection_parameters_properties_model = {
            'access_token': 'ya29.Il-_',
            'account_name': 'ibmdatastage.us-east-1',
            'api_key': 'ApiKey-a31d60c5-0f7b-4995-a4ae-69bf09d3de50',
            'auth_type': 'Bearer Token',
            'client_id': '81571342315',
            'client_secret': 'uIn8rVyIRsd',
            'collection': 'test_collection',
            'credentials': '-----BEGIN PRIVATE KEY-----',
            'database': 'TPCDS',
            'host': '192.168.0.1',
            'http_path': 'cliservice',
            'jar_uris': '/v2/asset_files/dbdrivers/ngdbc.jar',
            'jdbc_driver': 'Snowflake',
            'jdbc_url': '/v2/asset_files/dbdrivers/ngdbc.jar',
            'password': 'password',
            'port': '50000',
            'project_id': 'housecanary-com',
            'properties': 'key=value',
            'refresh_token': '1//06uwhP7_312g',
            'role': 'SYSADMIN',
            'sap_gateway_url': 'https://sapes5.sapdevcenter.com',
            'server': 'ol_informix1410',
            'service_name': 'pdborcl.fyre.ibm.com',
            'sid': 'orcl',
            'ssl': 'false',
            'ssl_certificate': '-----BEGIN CERTIFICATE-----',
            'ssl_certificate_host': 'test.com',
            'ssl_certificate_validation': 'false',
            'username': 'db2inst1',
            'warehouse': 'wdpcondev',
        }

        add_datasource_connection_response = self.data_virtualization_service.add_datasource_connection(
            datasource_type='DB2',
            name='DB2',
            origin_country='us',
            properties=post_datasource_connection_parameters_properties_model,
            asset_category='USER'
        )

        assert add_datasource_connection_response.get_status_code() == 201
        post_datasource_connection = add_datasource_connection_response.get_result()
        assert post_datasource_connection is not None

    @needscredentials
    def test_grant_user_to_virtual_table(self):

        grant_user_to_virtual_table_response = self.data_virtualization_service.grant_user_to_virtual_table(
            table_name='EMPLOYEE',
            table_schema='dv_ibmid_060000s4y5',
            authid='PUBLIC'
        )

        assert grant_user_to_virtual_table_response.get_status_code() == 204

    @needscredentials
    def test_grant_roles_to_virtualized_table(self):

        grant_roles_to_virtualized_table_response = self.data_virtualization_service.grant_roles_to_virtualized_table(
            table_name='EMPLOYEE',
            table_schema='dv_ibmid_060000s4y5',
            role_name='PUBLIC'
        )

        assert grant_roles_to_virtualized_table_response.get_status_code() == 204

    @needscredentials
    def test_list_tables_for_role(self):

        list_tables_for_role_response = self.data_virtualization_service.list_tables_for_role(
            rolename='MANAGER | STEWARD | ENGINEER | USER'
        )

        assert list_tables_for_role_response.get_status_code() == 200
        tables_for_role_response = list_tables_for_role_response.get_result()
        assert tables_for_role_response is not None

    @needscredentials
    def test_turn_on_policy_v2(self):

        turn_on_policy_v2_response = self.data_virtualization_service.turn_on_policy_v2(
            status='enabled'
        )

        assert turn_on_policy_v2_response.get_status_code() == 200
        turn_on_policy_v2_response = turn_on_policy_v2_response.get_result()
        assert turn_on_policy_v2_response is not None

    @needscredentials
    def test_check_policy_status_v2(self):

        check_policy_status_v2_response = self.data_virtualization_service.check_policy_status_v2()

        assert check_policy_status_v2_response.get_status_code() == 200
        check_policy_status_v2_response = check_policy_status_v2_response.get_result()
        assert check_policy_status_v2_response is not None

    @needscredentials
    def test_dvaas_virtualize_table(self):

        # Construct a dict representation of a VirtualizeTableParameterSourceTableDefItem model
        virtualize_table_parameter_source_table_def_item_model = {
            'column_name': 'Column1',
            'column_type': 'INTEGER',
        }

        # Construct a dict representation of a VirtualizeTableParameterVirtualTableDefItem model
        virtualize_table_parameter_virtual_table_def_item_model = {
            'column_name': 'Column_1',
            'column_type': 'INTEGER',
        }

        dvaas_virtualize_table_response = self.data_virtualization_service.dvaas_virtualize_table(
            source_name='Tab1',
            source_table_def=[virtualize_table_parameter_source_table_def_item_model],
            sources=['DB210001:"Hjq1"'],
            virtual_name='Tab1',
            virtual_schema='dv_ibmid_060000s4y5',
            virtual_table_def=[virtualize_table_parameter_virtual_table_def_item_model],
            is_included_columns='Y, Y, N',
            replace=False
        )

        assert dvaas_virtualize_table_response.get_status_code() == 201
        virtualize_table_response = dvaas_virtualize_table_response.get_result()
        assert virtualize_table_response is not None

    @needscredentials
    def test_get_primary_catalog(self):

        get_primary_catalog_response = self.data_virtualization_service.get_primary_catalog()

        assert get_primary_catalog_response.get_status_code() == 200
        primary_catalog_info = get_primary_catalog_response.get_result()
        assert primary_catalog_info is not None

    @needscredentials
    def test_post_primary_catalog(self):

        post_primary_catalog_response = self.data_virtualization_service.post_primary_catalog(
            guid='d77fc432-9b1a-4938-a2a5-9f37e08041f6'
        )

        assert post_primary_catalog_response.get_status_code() == 201
        post_primary_catalog = post_primary_catalog_response.get_result()
        assert post_primary_catalog is not None

    @needscredentials
    def test_publish_assets(self):

        # Construct a dict representation of a PostPrimaryCatalogParametersAssetsItem model
        post_primary_catalog_parameters_assets_item_model = {
            'schema': 'db2inst1',
            'table': 'EMPLOYEE',
        }

        publish_assets_response = self.data_virtualization_service.publish_assets(
            catalog_id='2b6b9fc5-626c-47a9-a836-56b76c0bc826',
            allow_duplicates=False,
            assets=[post_primary_catalog_parameters_assets_item_model]
        )

        assert publish_assets_response.get_status_code() == 200
        catalog_publish_response = publish_assets_response.get_result()
        assert catalog_publish_response is not None

    @needscredentials
    def test_revoke_user_from_object(self):

        revoke_user_from_object_response = self.data_virtualization_service.revoke_user_from_object(
            authid='PUBLIC',
            table_name='EMPLOYEE',
            table_schema='dv_ibmid_060000s4y5'
        )

        assert revoke_user_from_object_response.get_status_code() == 204

    @needscredentials
    def test_dvaas_revoke_role_from_table(self):

        dvaas_revoke_role_from_table_response = self.data_virtualization_service.dvaas_revoke_role_from_table(
            role_name='DV_ENGINEER',
            table_name='EMPLOYEE',
            table_schema='dv_ibmid_060000s4y5'
        )

        assert dvaas_revoke_role_from_table_response.get_status_code() == 204

    @needscredentials
    def test_delete_table(self):

        delete_table_response = self.data_virtualization_service.delete_table(
            virtual_schema='testString',
            virtual_name='testString'
        )

        assert delete_table_response.get_status_code() == 204

    @needscredentials
    def test_delete_primary_catalog(self):

        delete_primary_catalog_response = self.data_virtualization_service.delete_primary_catalog(
            guid='d77fc432-9b1a-4938-a2a5-9f37e08041f6'
        )

        assert delete_primary_catalog_response.get_status_code() == 204

    @needscredentials
    def test_delete_datasource_connection(self):

        delete_datasource_connection_response = self.data_virtualization_service.delete_datasource_connection(
            connection_id='75e4d01b-7417-4abc-b267-8ffb393fb970',
            cid='DB210013'
        )

        assert delete_datasource_connection_response.get_status_code() == 204

