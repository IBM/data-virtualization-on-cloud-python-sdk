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
Unit Tests for DataVirtualizationV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud.data_virtualization_v1 import *


_service = DataVirtualizationV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://fake'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: DataSources
##############################################################################
# region

class TestListDatasourceConnections():
    """
    Test Class for list_datasource_connections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_datasource_connections_all_params(self):
        """
        list_datasource_connections()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections')
        mock_response = '{"datasource_connections": [{"node_name": "node_name", "node_description": "node_description", "agent_class": "agent_class", "hostname": "hostname", "port": "port", "os_user": "os_user", "is_docker": "is_docker", "dscount": "dscount", "data_sources": [{"cid": "cid", "dbname": "dbname", "connection_id": "connection_id", "srchostname": "srchostname", "srcport": "srcport", "srctype": "srctype", "usr": "usr", "uri": "uri", "status": "status", "connection_name": "connection_name"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_datasource_connections()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestAddDatasourceConnection():
    """
    Test Class for add_datasource_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_datasource_connection_all_params(self):
        """
        add_datasource_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections')
        mock_response = '{"connection_id": "connection_id", "datasource_type": "datasource_type", "name": "name"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PostDatasourceConnectionParametersProperties model
        post_datasource_connection_parameters_properties_model = {}
        post_datasource_connection_parameters_properties_model['access_token'] = 'testString'
        post_datasource_connection_parameters_properties_model['account_name'] = 'testString'
        post_datasource_connection_parameters_properties_model['api_key'] = 'testString'
        post_datasource_connection_parameters_properties_model['auth_type'] = 'testString'
        post_datasource_connection_parameters_properties_model['client_id'] = 'testString'
        post_datasource_connection_parameters_properties_model['client_secret'] = 'testString'
        post_datasource_connection_parameters_properties_model['collection'] = 'testString'
        post_datasource_connection_parameters_properties_model['credentials'] = 'testString'
        post_datasource_connection_parameters_properties_model['database'] = 'TPCDS'
        post_datasource_connection_parameters_properties_model['host'] = '192.168.0.1'
        post_datasource_connection_parameters_properties_model['http_path'] = 'testString'
        post_datasource_connection_parameters_properties_model['jar_uris'] = 'testString'
        post_datasource_connection_parameters_properties_model['jdbc_driver'] = 'testString'
        post_datasource_connection_parameters_properties_model['jdbc_url'] = 'testString'
        post_datasource_connection_parameters_properties_model['password'] = 'password'
        post_datasource_connection_parameters_properties_model['port'] = '50000'
        post_datasource_connection_parameters_properties_model['project_id'] = 'testString'
        post_datasource_connection_parameters_properties_model['properties'] = 'testString'
        post_datasource_connection_parameters_properties_model['refresh_token'] = 'testString'
        post_datasource_connection_parameters_properties_model['role'] = 'testString'
        post_datasource_connection_parameters_properties_model['sap_gateway_url'] = 'testString'
        post_datasource_connection_parameters_properties_model['server'] = 'testString'
        post_datasource_connection_parameters_properties_model['service_name'] = 'testString'
        post_datasource_connection_parameters_properties_model['sid'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl'] = 'false'
        post_datasource_connection_parameters_properties_model['ssl_certificate'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl_certificate_host'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl_certificate_validation'] = 'testString'
        post_datasource_connection_parameters_properties_model['username'] = 'db2inst1'
        post_datasource_connection_parameters_properties_model['warehouse'] = 'testString'

        # Set up parameter values
        datasource_type = 'DB2'
        name = 'DB2'
        origin_country = 'us'
        properties = post_datasource_connection_parameters_properties_model
        asset_category = 'testString'

        # Invoke method
        response = _service.add_datasource_connection(
            datasource_type,
            name,
            origin_country,
            properties,
            asset_category=asset_category,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['datasource_type'] == 'DB2'
        assert req_body['name'] == 'DB2'
        assert req_body['origin_country'] == 'us'
        assert req_body['properties'] == post_datasource_connection_parameters_properties_model
        assert req_body['asset_category'] == 'testString'


    @responses.activate
    def test_add_datasource_connection_value_error(self):
        """
        test_add_datasource_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections')
        mock_response = '{"connection_id": "connection_id", "datasource_type": "datasource_type", "name": "name"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PostDatasourceConnectionParametersProperties model
        post_datasource_connection_parameters_properties_model = {}
        post_datasource_connection_parameters_properties_model['access_token'] = 'testString'
        post_datasource_connection_parameters_properties_model['account_name'] = 'testString'
        post_datasource_connection_parameters_properties_model['api_key'] = 'testString'
        post_datasource_connection_parameters_properties_model['auth_type'] = 'testString'
        post_datasource_connection_parameters_properties_model['client_id'] = 'testString'
        post_datasource_connection_parameters_properties_model['client_secret'] = 'testString'
        post_datasource_connection_parameters_properties_model['collection'] = 'testString'
        post_datasource_connection_parameters_properties_model['credentials'] = 'testString'
        post_datasource_connection_parameters_properties_model['database'] = 'TPCDS'
        post_datasource_connection_parameters_properties_model['host'] = '192.168.0.1'
        post_datasource_connection_parameters_properties_model['http_path'] = 'testString'
        post_datasource_connection_parameters_properties_model['jar_uris'] = 'testString'
        post_datasource_connection_parameters_properties_model['jdbc_driver'] = 'testString'
        post_datasource_connection_parameters_properties_model['jdbc_url'] = 'testString'
        post_datasource_connection_parameters_properties_model['password'] = 'password'
        post_datasource_connection_parameters_properties_model['port'] = '50000'
        post_datasource_connection_parameters_properties_model['project_id'] = 'testString'
        post_datasource_connection_parameters_properties_model['properties'] = 'testString'
        post_datasource_connection_parameters_properties_model['refresh_token'] = 'testString'
        post_datasource_connection_parameters_properties_model['role'] = 'testString'
        post_datasource_connection_parameters_properties_model['sap_gateway_url'] = 'testString'
        post_datasource_connection_parameters_properties_model['server'] = 'testString'
        post_datasource_connection_parameters_properties_model['service_name'] = 'testString'
        post_datasource_connection_parameters_properties_model['sid'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl'] = 'false'
        post_datasource_connection_parameters_properties_model['ssl_certificate'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl_certificate_host'] = 'testString'
        post_datasource_connection_parameters_properties_model['ssl_certificate_validation'] = 'testString'
        post_datasource_connection_parameters_properties_model['username'] = 'db2inst1'
        post_datasource_connection_parameters_properties_model['warehouse'] = 'testString'

        # Set up parameter values
        datasource_type = 'DB2'
        name = 'DB2'
        origin_country = 'us'
        properties = post_datasource_connection_parameters_properties_model
        asset_category = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "datasource_type": datasource_type,
            "name": name,
            "origin_country": origin_country,
            "properties": properties,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_datasource_connection(**req_copy)



class TestDeleteDatasourceConnection():
    """
    Test Class for delete_datasource_connection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_datasource_connection_all_params(self):
        """
        delete_datasource_connection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections/75e4d01b-7417-4abc-b267-8ffb393fb970')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        connection_id = '75e4d01b-7417-4abc-b267-8ffb393fb970'
        cid = 'DB210013'

        # Invoke method
        response = _service.delete_datasource_connection(
            connection_id,
            cid=cid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'cid={}'.format(cid) in query_string


    @responses.activate
    def test_delete_datasource_connection_required_params(self):
        """
        test_delete_datasource_connection_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections/75e4d01b-7417-4abc-b267-8ffb393fb970')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        connection_id = '75e4d01b-7417-4abc-b267-8ffb393fb970'

        # Invoke method
        response = _service.delete_datasource_connection(
            connection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_datasource_connection_value_error(self):
        """
        test_delete_datasource_connection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/datasource/connections/75e4d01b-7417-4abc-b267-8ffb393fb970')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        connection_id = '75e4d01b-7417-4abc-b267-8ffb393fb970'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "connection_id": connection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_datasource_connection(**req_copy)



# endregion
##############################################################################
# End of Service: DataSources
##############################################################################

##############################################################################
# Start of Service: Users
##############################################################################
# region

class TestGrantUserToVirtualTable():
    """
    Test Class for grant_user_to_virtual_table
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_grant_user_to_virtual_table_all_params(self):
        """
        grant_user_to_virtual_table()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/users')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'
        authid = 'PUBLIC'

        # Invoke method
        response = _service.grant_user_to_virtual_table(
            table_name,
            table_schema,
            authid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['table_name'] == 'EMPLOYEE'
        assert req_body['table_schema'] == 'dv_ibmid_060000s4y5'
        assert req_body['authid'] == 'PUBLIC'


    @responses.activate
    def test_grant_user_to_virtual_table_value_error(self):
        """
        test_grant_user_to_virtual_table_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/users')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'
        authid = 'PUBLIC'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "table_name": table_name,
            "table_schema": table_schema,
            "authid": authid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.grant_user_to_virtual_table(**req_copy)



class TestRevokeUserFromObject():
    """
    Test Class for revoke_user_from_object
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_revoke_user_from_object_all_params(self):
        """
        revoke_user_from_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/users/PUBLIC')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        authid = 'PUBLIC'
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'

        # Invoke method
        response = _service.revoke_user_from_object(
            authid,
            table_name,
            table_schema,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'table_name={}'.format(table_name) in query_string
        assert 'table_schema={}'.format(table_schema) in query_string


    @responses.activate
    def test_revoke_user_from_object_value_error(self):
        """
        test_revoke_user_from_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/users/PUBLIC')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        authid = 'PUBLIC'
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "authid": authid,
            "table_name": table_name,
            "table_schema": table_schema,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.revoke_user_from_object(**req_copy)



# endregion
##############################################################################
# End of Service: Users
##############################################################################

##############################################################################
# Start of Service: Roles
##############################################################################
# region

class TestGrantRolesToVirtualizedTable():
    """
    Test Class for grant_roles_to_virtualized_table
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_grant_roles_to_virtualized_table_all_params(self):
        """
        grant_roles_to_virtualized_table()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/roles')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'
        role_name = 'PUBLIC'

        # Invoke method
        response = _service.grant_roles_to_virtualized_table(
            table_name,
            table_schema,
            role_name=role_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['table_name'] == 'EMPLOYEE'
        assert req_body['table_schema'] == 'dv_ibmid_060000s4y5'
        assert req_body['role_name'] == 'PUBLIC'


    @responses.activate
    def test_grant_roles_to_virtualized_table_value_error(self):
        """
        test_grant_roles_to_virtualized_table_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/roles')
        responses.add(responses.POST,
                      url,
                      status=204)

        # Set up parameter values
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'
        role_name = 'PUBLIC'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "table_name": table_name,
            "table_schema": table_schema,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.grant_roles_to_virtualized_table(**req_copy)



class TestDvaasRevokeRoleFromTable():
    """
    Test Class for dvaas_revoke_role_from_table
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_dvaas_revoke_role_from_table_all_params(self):
        """
        dvaas_revoke_role_from_table()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/roles/DV_ENGINEER')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_name = 'DV_ENGINEER'
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'

        # Invoke method
        response = _service.dvaas_revoke_role_from_table(
            role_name,
            table_name,
            table_schema,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'table_name={}'.format(table_name) in query_string
        assert 'table_schema={}'.format(table_schema) in query_string


    @responses.activate
    def test_dvaas_revoke_role_from_table_value_error(self):
        """
        test_dvaas_revoke_role_from_table_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/roles/DV_ENGINEER')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        role_name = 'DV_ENGINEER'
        table_name = 'EMPLOYEE'
        table_schema = 'dv_ibmid_060000s4y5'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "role_name": role_name,
            "table_name": table_name,
            "table_schema": table_schema,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.dvaas_revoke_role_from_table(**req_copy)



class TestListTablesForRole():
    """
    Test Class for list_tables_for_role
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_tables_for_role_all_params(self):
        """
        list_tables_for_role()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/tables')
        mock_response = '{"objects": [{"table_name": "table_name", "table_schema": "table_schema"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rolename = 'MANAGER | STEWARD | ENGINEER | USER'

        # Invoke method
        response = _service.list_tables_for_role(
            rolename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'rolename={}'.format(rolename) in query_string


    @responses.activate
    def test_list_tables_for_role_value_error(self):
        """
        test_list_tables_for_role_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/privileges/tables')
        mock_response = '{"objects": [{"table_name": "table_name", "table_schema": "table_schema"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rolename = 'MANAGER | STEWARD | ENGINEER | USER'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rolename": rolename,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tables_for_role(**req_copy)



# endregion
##############################################################################
# End of Service: Roles
##############################################################################

##############################################################################
# Start of Service: Securities
##############################################################################
# region

class TestTurnOnPolicyV2():
    """
    Test Class for turn_on_policy_v2
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_turn_on_policy_v2_all_params(self):
        """
        turn_on_policy_v2()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/security/policy/status')
        mock_response = '{"status": "enabled"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'enabled'

        # Invoke method
        response = _service.turn_on_policy_v2(
            status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'status={}'.format(status) in query_string


    @responses.activate
    def test_turn_on_policy_v2_value_error(self):
        """
        test_turn_on_policy_v2_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/security/policy/status')
        mock_response = '{"status": "enabled"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'enabled'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "status": status,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.turn_on_policy_v2(**req_copy)



class TestCheckPolicyStatusV2():
    """
    Test Class for check_policy_status_v2
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_check_policy_status_v2_all_params(self):
        """
        check_policy_status_v2()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/security/policy/status')
        mock_response = '{"status": "enabled"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.check_policy_status_v2()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Securities
##############################################################################

##############################################################################
# Start of Service: Virtualization
##############################################################################
# region

class TestDvaasVirtualizeTable():
    """
    Test Class for dvaas_virtualize_table
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_dvaas_virtualize_table_all_params(self):
        """
        dvaas_virtualize_table()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/virtualization/tables')
        mock_response = '{"table_name": "Tab1", "schema_name": "dv_ibmid_060000s4y5"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a VirtualizeTableParameterSourceTableDefItem model
        virtualize_table_parameter_source_table_def_item_model = {}
        virtualize_table_parameter_source_table_def_item_model['column_name'] = 'Column1'
        virtualize_table_parameter_source_table_def_item_model['column_type'] = 'INTEGER'

        # Construct a dict representation of a VirtualizeTableParameterVirtualTableDefItem model
        virtualize_table_parameter_virtual_table_def_item_model = {}
        virtualize_table_parameter_virtual_table_def_item_model['column_name'] = 'Column_1'
        virtualize_table_parameter_virtual_table_def_item_model['column_type'] = 'INTEGER'

        # Set up parameter values
        source_name = 'Tab1'
        source_table_def = [virtualize_table_parameter_source_table_def_item_model]
        sources = ['DB210001:"Hjq1"']
        virtual_name = 'Tab1'
        virtual_schema = 'dv_ibmid_060000s4y5'
        virtual_table_def = [virtualize_table_parameter_virtual_table_def_item_model]
        is_included_columns = 'Y, Y, N'
        replace = False

        # Invoke method
        response = _service.dvaas_virtualize_table(
            source_name,
            source_table_def,
            sources,
            virtual_name,
            virtual_schema,
            virtual_table_def,
            is_included_columns=is_included_columns,
            replace=replace,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_name'] == 'Tab1'
        assert req_body['source_table_def'] == [virtualize_table_parameter_source_table_def_item_model]
        assert req_body['sources'] == ['DB210001:"Hjq1"']
        assert req_body['virtual_name'] == 'Tab1'
        assert req_body['virtual_schema'] == 'dv_ibmid_060000s4y5'
        assert req_body['virtual_table_def'] == [virtualize_table_parameter_virtual_table_def_item_model]
        assert req_body['is_included_columns'] == 'Y, Y, N'
        assert req_body['replace'] == False


    @responses.activate
    def test_dvaas_virtualize_table_value_error(self):
        """
        test_dvaas_virtualize_table_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/virtualization/tables')
        mock_response = '{"table_name": "Tab1", "schema_name": "dv_ibmid_060000s4y5"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a VirtualizeTableParameterSourceTableDefItem model
        virtualize_table_parameter_source_table_def_item_model = {}
        virtualize_table_parameter_source_table_def_item_model['column_name'] = 'Column1'
        virtualize_table_parameter_source_table_def_item_model['column_type'] = 'INTEGER'

        # Construct a dict representation of a VirtualizeTableParameterVirtualTableDefItem model
        virtualize_table_parameter_virtual_table_def_item_model = {}
        virtualize_table_parameter_virtual_table_def_item_model['column_name'] = 'Column_1'
        virtualize_table_parameter_virtual_table_def_item_model['column_type'] = 'INTEGER'

        # Set up parameter values
        source_name = 'Tab1'
        source_table_def = [virtualize_table_parameter_source_table_def_item_model]
        sources = ['DB210001:"Hjq1"']
        virtual_name = 'Tab1'
        virtual_schema = 'dv_ibmid_060000s4y5'
        virtual_table_def = [virtualize_table_parameter_virtual_table_def_item_model]
        is_included_columns = 'Y, Y, N'
        replace = False

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "source_name": source_name,
            "source_table_def": source_table_def,
            "sources": sources,
            "virtual_name": virtual_name,
            "virtual_schema": virtual_schema,
            "virtual_table_def": virtual_table_def,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.dvaas_virtualize_table(**req_copy)



class TestDeleteTable():
    """
    Test Class for delete_table
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_table_all_params(self):
        """
        delete_table()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/virtualization/tables/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        virtual_schema = 'testString'
        virtual_name = 'testString'

        # Invoke method
        response = _service.delete_table(
            virtual_schema,
            virtual_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'virtual_schema={}'.format(virtual_schema) in query_string


    @responses.activate
    def test_delete_table_value_error(self):
        """
        test_delete_table_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/virtualization/tables/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        virtual_schema = 'testString'
        virtual_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "virtual_schema": virtual_schema,
            "virtual_name": virtual_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_table(**req_copy)



# endregion
##############################################################################
# End of Service: Virtualization
##############################################################################

##############################################################################
# Start of Service: PrimaryCatalog
##############################################################################
# region

class TestGetPrimaryCatalog():
    """
    Test Class for get_primary_catalog
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_primary_catalog_all_params(self):
        """
        get_primary_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/catalog/primary')
        mock_response = '{"entity": {"auto_profiling": true, "bss_account_id": "999", "capacity_limit": 0, "description": "The governed catalog where data assets are synchronized with the Information assets view.", "generator": "Catalog-OMRS-Synced", "is_governed": true, "name": "Primary Catalog"}, "href": "/v2/catalogs/648fb4e0-3f6c-4ce3-afbb-317acc03faa4", "metadata": {"create_time": "2021-01-11T10:37:03Z", "creator_id": "648fb4e01000330999", "guid": "648fb4e0-3f6c-4ce3-afbb-317acc03faa4", "url": "648fb4e0/v2/catalogs/648fb4e0-3f6c-4ce3-afbb-317acc03faa4"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_primary_catalog()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestPostPrimaryCatalog():
    """
    Test Class for post_primary_catalog
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_post_primary_catalog_all_params(self):
        """
        post_primary_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/catalog/primary')
        mock_response = '{"guid": "d77fc432-9b1a-4938-a2a5-9f37e08041f6", "name": "Default Catalog", "description": "The governed catalog where data assets are synchronized with the Information assets view."}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        guid = 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'

        # Invoke method
        response = _service.post_primary_catalog(
            guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['guid'] == 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'


    @responses.activate
    def test_post_primary_catalog_value_error(self):
        """
        test_post_primary_catalog_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/catalog/primary')
        mock_response = '{"guid": "d77fc432-9b1a-4938-a2a5-9f37e08041f6", "name": "Default Catalog", "description": "The governed catalog where data assets are synchronized with the Information assets view."}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        guid = 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "guid": guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.post_primary_catalog(**req_copy)



class TestDeletePrimaryCatalog():
    """
    Test Class for delete_primary_catalog
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_primary_catalog_all_params(self):
        """
        delete_primary_catalog()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/catalog/primary')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        guid = 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'

        # Invoke method
        response = _service.delete_primary_catalog(
            guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'guid={}'.format(guid) in query_string


    @responses.activate
    def test_delete_primary_catalog_value_error(self):
        """
        test_delete_primary_catalog_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/catalog/primary')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        guid = 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "guid": guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_primary_catalog(**req_copy)



# endregion
##############################################################################
# End of Service: PrimaryCatalog
##############################################################################

##############################################################################
# Start of Service: PublishObjects
##############################################################################
# region

class TestPublishAssets():
    """
    Test Class for publish_assets
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_publish_assets_all_params(self):
        """
        publish_assets()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/integration/catalog/publish')
        mock_response = '{"duplicate_assets": [{"schema_name": "USER999", "table_name": "customer"}], "failed_assets": [{"error_msg": "37fa4a15-1071-4a20-bc9e-0283d3dfb6e", "schema_name": "USER999", "table_name": "customer"}], "published_assets": [{"schema_name": "USER999", "table_name": "customer", "wkc_asset_id": "37fa4a15-1071-4a20-bc9e-0283d3dfb6e1"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PostPrimaryCatalogParametersAssetsItem model
        post_primary_catalog_parameters_assets_item_model = {}
        post_primary_catalog_parameters_assets_item_model['schema'] = 'db2inst1'
        post_primary_catalog_parameters_assets_item_model['table'] = 'EMPLOYEE'

        # Set up parameter values
        catalog_id = '2b6b9fc5-626c-47a9-a836-56b76c0bc826'
        allow_duplicates = False
        assets = [post_primary_catalog_parameters_assets_item_model]

        # Invoke method
        response = _service.publish_assets(
            catalog_id,
            allow_duplicates,
            assets,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalog_id'] == '2b6b9fc5-626c-47a9-a836-56b76c0bc826'
        assert req_body['allow_duplicates'] == False
        assert req_body['assets'] == [post_primary_catalog_parameters_assets_item_model]


    @responses.activate
    def test_publish_assets_value_error(self):
        """
        test_publish_assets_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/integration/catalog/publish')
        mock_response = '{"duplicate_assets": [{"schema_name": "USER999", "table_name": "customer"}], "failed_assets": [{"error_msg": "37fa4a15-1071-4a20-bc9e-0283d3dfb6e", "schema_name": "USER999", "table_name": "customer"}], "published_assets": [{"schema_name": "USER999", "table_name": "customer", "wkc_asset_id": "37fa4a15-1071-4a20-bc9e-0283d3dfb6e1"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PostPrimaryCatalogParametersAssetsItem model
        post_primary_catalog_parameters_assets_item_model = {}
        post_primary_catalog_parameters_assets_item_model['schema'] = 'db2inst1'
        post_primary_catalog_parameters_assets_item_model['table'] = 'EMPLOYEE'

        # Set up parameter values
        catalog_id = '2b6b9fc5-626c-47a9-a836-56b76c0bc826'
        allow_duplicates = False
        assets = [post_primary_catalog_parameters_assets_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "allow_duplicates": allow_duplicates,
            "assets": assets,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.publish_assets(**req_copy)



# endregion
##############################################################################
# End of Service: PublishObjects
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_CatalogPublishResponseDuplicateAssetsItem():
    """
    Test Class for CatalogPublishResponseDuplicateAssetsItem
    """

    def test_catalog_publish_response_duplicate_assets_item_serialization(self):
        """
        Test serialization/deserialization for CatalogPublishResponseDuplicateAssetsItem
        """

        # Construct a json representation of a CatalogPublishResponseDuplicateAssetsItem model
        catalog_publish_response_duplicate_assets_item_model_json = {}
        catalog_publish_response_duplicate_assets_item_model_json['schema_name'] = 'USER999'
        catalog_publish_response_duplicate_assets_item_model_json['table_name'] = 'customer'

        # Construct a model instance of CatalogPublishResponseDuplicateAssetsItem by calling from_dict on the json representation
        catalog_publish_response_duplicate_assets_item_model = CatalogPublishResponseDuplicateAssetsItem.from_dict(catalog_publish_response_duplicate_assets_item_model_json)
        assert catalog_publish_response_duplicate_assets_item_model != False

        # Construct a model instance of CatalogPublishResponseDuplicateAssetsItem by calling from_dict on the json representation
        catalog_publish_response_duplicate_assets_item_model_dict = CatalogPublishResponseDuplicateAssetsItem.from_dict(catalog_publish_response_duplicate_assets_item_model_json).__dict__
        catalog_publish_response_duplicate_assets_item_model2 = CatalogPublishResponseDuplicateAssetsItem(**catalog_publish_response_duplicate_assets_item_model_dict)

        # Verify the model instances are equivalent
        assert catalog_publish_response_duplicate_assets_item_model == catalog_publish_response_duplicate_assets_item_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_publish_response_duplicate_assets_item_model_json2 = catalog_publish_response_duplicate_assets_item_model.to_dict()
        assert catalog_publish_response_duplicate_assets_item_model_json2 == catalog_publish_response_duplicate_assets_item_model_json

class TestModel_CatalogPublishResponseFailedAssetsItem():
    """
    Test Class for CatalogPublishResponseFailedAssetsItem
    """

    def test_catalog_publish_response_failed_assets_item_serialization(self):
        """
        Test serialization/deserialization for CatalogPublishResponseFailedAssetsItem
        """

        # Construct a json representation of a CatalogPublishResponseFailedAssetsItem model
        catalog_publish_response_failed_assets_item_model_json = {}
        catalog_publish_response_failed_assets_item_model_json['error_msg'] = '37fa4a15-1071-4a20-bc9e-0283d3dfb6e'
        catalog_publish_response_failed_assets_item_model_json['schema_name'] = 'USER999'
        catalog_publish_response_failed_assets_item_model_json['table_name'] = 'customer'

        # Construct a model instance of CatalogPublishResponseFailedAssetsItem by calling from_dict on the json representation
        catalog_publish_response_failed_assets_item_model = CatalogPublishResponseFailedAssetsItem.from_dict(catalog_publish_response_failed_assets_item_model_json)
        assert catalog_publish_response_failed_assets_item_model != False

        # Construct a model instance of CatalogPublishResponseFailedAssetsItem by calling from_dict on the json representation
        catalog_publish_response_failed_assets_item_model_dict = CatalogPublishResponseFailedAssetsItem.from_dict(catalog_publish_response_failed_assets_item_model_json).__dict__
        catalog_publish_response_failed_assets_item_model2 = CatalogPublishResponseFailedAssetsItem(**catalog_publish_response_failed_assets_item_model_dict)

        # Verify the model instances are equivalent
        assert catalog_publish_response_failed_assets_item_model == catalog_publish_response_failed_assets_item_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_publish_response_failed_assets_item_model_json2 = catalog_publish_response_failed_assets_item_model.to_dict()
        assert catalog_publish_response_failed_assets_item_model_json2 == catalog_publish_response_failed_assets_item_model_json

class TestModel_CatalogPublishResponsePublishedAssetsItem():
    """
    Test Class for CatalogPublishResponsePublishedAssetsItem
    """

    def test_catalog_publish_response_published_assets_item_serialization(self):
        """
        Test serialization/deserialization for CatalogPublishResponsePublishedAssetsItem
        """

        # Construct a json representation of a CatalogPublishResponsePublishedAssetsItem model
        catalog_publish_response_published_assets_item_model_json = {}
        catalog_publish_response_published_assets_item_model_json['schema_name'] = 'USER999'
        catalog_publish_response_published_assets_item_model_json['table_name'] = 'customer'
        catalog_publish_response_published_assets_item_model_json['wkc_asset_id'] = '37fa4a15-1071-4a20-bc9e-0283d3dfb6e1'

        # Construct a model instance of CatalogPublishResponsePublishedAssetsItem by calling from_dict on the json representation
        catalog_publish_response_published_assets_item_model = CatalogPublishResponsePublishedAssetsItem.from_dict(catalog_publish_response_published_assets_item_model_json)
        assert catalog_publish_response_published_assets_item_model != False

        # Construct a model instance of CatalogPublishResponsePublishedAssetsItem by calling from_dict on the json representation
        catalog_publish_response_published_assets_item_model_dict = CatalogPublishResponsePublishedAssetsItem.from_dict(catalog_publish_response_published_assets_item_model_json).__dict__
        catalog_publish_response_published_assets_item_model2 = CatalogPublishResponsePublishedAssetsItem(**catalog_publish_response_published_assets_item_model_dict)

        # Verify the model instances are equivalent
        assert catalog_publish_response_published_assets_item_model == catalog_publish_response_published_assets_item_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_publish_response_published_assets_item_model_json2 = catalog_publish_response_published_assets_item_model.to_dict()
        assert catalog_publish_response_published_assets_item_model_json2 == catalog_publish_response_published_assets_item_model_json

class TestModel_CheckPolicyStatusV2Response():
    """
    Test Class for CheckPolicyStatusV2Response
    """

    def test_check_policy_status_v2_response_serialization(self):
        """
        Test serialization/deserialization for CheckPolicyStatusV2Response
        """

        # Construct a json representation of a CheckPolicyStatusV2Response model
        check_policy_status_v2_response_model_json = {}
        check_policy_status_v2_response_model_json['status'] = 'enabled'

        # Construct a model instance of CheckPolicyStatusV2Response by calling from_dict on the json representation
        check_policy_status_v2_response_model = CheckPolicyStatusV2Response.from_dict(check_policy_status_v2_response_model_json)
        assert check_policy_status_v2_response_model != False

        # Construct a model instance of CheckPolicyStatusV2Response by calling from_dict on the json representation
        check_policy_status_v2_response_model_dict = CheckPolicyStatusV2Response.from_dict(check_policy_status_v2_response_model_json).__dict__
        check_policy_status_v2_response_model2 = CheckPolicyStatusV2Response(**check_policy_status_v2_response_model_dict)

        # Verify the model instances are equivalent
        assert check_policy_status_v2_response_model == check_policy_status_v2_response_model2

        # Convert model instance back to dict and verify no loss of data
        check_policy_status_v2_response_model_json2 = check_policy_status_v2_response_model.to_dict()
        assert check_policy_status_v2_response_model_json2 == check_policy_status_v2_response_model_json

class TestModel_DatasourceConnectionsList():
    """
    Test Class for DatasourceConnectionsList
    """

    def test_datasource_connections_list_serialization(self):
        """
        Test serialization/deserialization for DatasourceConnectionsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        datasource_connections_list_datasource_connections_item_data_sources_item_model = {} # DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem
        datasource_connections_list_datasource_connections_item_data_sources_item_model['cid'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['dbname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['connection_id'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srchostname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srcport'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srctype'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['usr'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['uri'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['status'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['connection_name'] = 'testString'

        datasource_connections_list_datasource_connections_item_model = {} # DatasourceConnectionsListDatasourceConnectionsItem
        datasource_connections_list_datasource_connections_item_model['node_name'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['node_description'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['agent_class'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['hostname'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['port'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['os_user'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['is_docker'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['dscount'] = 'testString'
        datasource_connections_list_datasource_connections_item_model['data_sources'] = [datasource_connections_list_datasource_connections_item_data_sources_item_model]

        # Construct a json representation of a DatasourceConnectionsList model
        datasource_connections_list_model_json = {}
        datasource_connections_list_model_json['datasource_connections'] = [datasource_connections_list_datasource_connections_item_model]

        # Construct a model instance of DatasourceConnectionsList by calling from_dict on the json representation
        datasource_connections_list_model = DatasourceConnectionsList.from_dict(datasource_connections_list_model_json)
        assert datasource_connections_list_model != False

        # Construct a model instance of DatasourceConnectionsList by calling from_dict on the json representation
        datasource_connections_list_model_dict = DatasourceConnectionsList.from_dict(datasource_connections_list_model_json).__dict__
        datasource_connections_list_model2 = DatasourceConnectionsList(**datasource_connections_list_model_dict)

        # Verify the model instances are equivalent
        assert datasource_connections_list_model == datasource_connections_list_model2

        # Convert model instance back to dict and verify no loss of data
        datasource_connections_list_model_json2 = datasource_connections_list_model.to_dict()
        assert datasource_connections_list_model_json2 == datasource_connections_list_model_json

class TestModel_DatasourceConnectionsListDatasourceConnectionsItem():
    """
    Test Class for DatasourceConnectionsListDatasourceConnectionsItem
    """

    def test_datasource_connections_list_datasource_connections_item_serialization(self):
        """
        Test serialization/deserialization for DatasourceConnectionsListDatasourceConnectionsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        datasource_connections_list_datasource_connections_item_data_sources_item_model = {} # DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem
        datasource_connections_list_datasource_connections_item_data_sources_item_model['cid'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['dbname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['connection_id'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srchostname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srcport'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['srctype'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['usr'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['uri'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['status'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model['connection_name'] = 'testString'

        # Construct a json representation of a DatasourceConnectionsListDatasourceConnectionsItem model
        datasource_connections_list_datasource_connections_item_model_json = {}
        datasource_connections_list_datasource_connections_item_model_json['node_name'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['node_description'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['agent_class'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['hostname'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['port'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['os_user'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['is_docker'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['dscount'] = 'testString'
        datasource_connections_list_datasource_connections_item_model_json['data_sources'] = [datasource_connections_list_datasource_connections_item_data_sources_item_model]

        # Construct a model instance of DatasourceConnectionsListDatasourceConnectionsItem by calling from_dict on the json representation
        datasource_connections_list_datasource_connections_item_model = DatasourceConnectionsListDatasourceConnectionsItem.from_dict(datasource_connections_list_datasource_connections_item_model_json)
        assert datasource_connections_list_datasource_connections_item_model != False

        # Construct a model instance of DatasourceConnectionsListDatasourceConnectionsItem by calling from_dict on the json representation
        datasource_connections_list_datasource_connections_item_model_dict = DatasourceConnectionsListDatasourceConnectionsItem.from_dict(datasource_connections_list_datasource_connections_item_model_json).__dict__
        datasource_connections_list_datasource_connections_item_model2 = DatasourceConnectionsListDatasourceConnectionsItem(**datasource_connections_list_datasource_connections_item_model_dict)

        # Verify the model instances are equivalent
        assert datasource_connections_list_datasource_connections_item_model == datasource_connections_list_datasource_connections_item_model2

        # Convert model instance back to dict and verify no loss of data
        datasource_connections_list_datasource_connections_item_model_json2 = datasource_connections_list_datasource_connections_item_model.to_dict()
        assert datasource_connections_list_datasource_connections_item_model_json2 == datasource_connections_list_datasource_connections_item_model_json

class TestModel_DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem():
    """
    Test Class for DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem
    """

    def test_datasource_connections_list_datasource_connections_item_data_sources_item_serialization(self):
        """
        Test serialization/deserialization for DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem
        """

        # Construct a json representation of a DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem model
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json = {}
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['cid'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['dbname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['connection_id'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['srchostname'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['srcport'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['srctype'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['usr'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['uri'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['status'] = 'testString'
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json['connection_name'] = 'testString'

        # Construct a model instance of DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem by calling from_dict on the json representation
        datasource_connections_list_datasource_connections_item_data_sources_item_model = DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem.from_dict(datasource_connections_list_datasource_connections_item_data_sources_item_model_json)
        assert datasource_connections_list_datasource_connections_item_data_sources_item_model != False

        # Construct a model instance of DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem by calling from_dict on the json representation
        datasource_connections_list_datasource_connections_item_data_sources_item_model_dict = DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem.from_dict(datasource_connections_list_datasource_connections_item_data_sources_item_model_json).__dict__
        datasource_connections_list_datasource_connections_item_data_sources_item_model2 = DatasourceConnectionsListDatasourceConnectionsItemDataSourcesItem(**datasource_connections_list_datasource_connections_item_data_sources_item_model_dict)

        # Verify the model instances are equivalent
        assert datasource_connections_list_datasource_connections_item_data_sources_item_model == datasource_connections_list_datasource_connections_item_data_sources_item_model2

        # Convert model instance back to dict and verify no loss of data
        datasource_connections_list_datasource_connections_item_data_sources_item_model_json2 = datasource_connections_list_datasource_connections_item_data_sources_item_model.to_dict()
        assert datasource_connections_list_datasource_connections_item_data_sources_item_model_json2 == datasource_connections_list_datasource_connections_item_data_sources_item_model_json

class TestModel_PostDatasourceConnection():
    """
    Test Class for PostDatasourceConnection
    """

    def test_post_datasource_connection_serialization(self):
        """
        Test serialization/deserialization for PostDatasourceConnection
        """

        # Construct a json representation of a PostDatasourceConnection model
        post_datasource_connection_model_json = {}
        post_datasource_connection_model_json['connection_id'] = 'testString'
        post_datasource_connection_model_json['datasource_type'] = 'testString'
        post_datasource_connection_model_json['name'] = 'testString'

        # Construct a model instance of PostDatasourceConnection by calling from_dict on the json representation
        post_datasource_connection_model = PostDatasourceConnection.from_dict(post_datasource_connection_model_json)
        assert post_datasource_connection_model != False

        # Construct a model instance of PostDatasourceConnection by calling from_dict on the json representation
        post_datasource_connection_model_dict = PostDatasourceConnection.from_dict(post_datasource_connection_model_json).__dict__
        post_datasource_connection_model2 = PostDatasourceConnection(**post_datasource_connection_model_dict)

        # Verify the model instances are equivalent
        assert post_datasource_connection_model == post_datasource_connection_model2

        # Convert model instance back to dict and verify no loss of data
        post_datasource_connection_model_json2 = post_datasource_connection_model.to_dict()
        assert post_datasource_connection_model_json2 == post_datasource_connection_model_json

class TestModel_PostDatasourceConnectionParametersProperties():
    """
    Test Class for PostDatasourceConnectionParametersProperties
    """

    def test_post_datasource_connection_parameters_properties_serialization(self):
        """
        Test serialization/deserialization for PostDatasourceConnectionParametersProperties
        """

        # Construct a json representation of a PostDatasourceConnectionParametersProperties model
        post_datasource_connection_parameters_properties_model_json = {}
        post_datasource_connection_parameters_properties_model_json['access_token'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['account_name'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['api_key'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['auth_type'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['client_id'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['client_secret'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['collection'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['credentials'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['database'] = 'TPCDS'
        post_datasource_connection_parameters_properties_model_json['host'] = '192.168.0.1'
        post_datasource_connection_parameters_properties_model_json['http_path'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['jar_uris'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['jdbc_driver'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['jdbc_url'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['password'] = 'password'
        post_datasource_connection_parameters_properties_model_json['port'] = '50000'
        post_datasource_connection_parameters_properties_model_json['project_id'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['properties'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['refresh_token'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['role'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['sap_gateway_url'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['server'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['service_name'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['sid'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['ssl'] = 'false'
        post_datasource_connection_parameters_properties_model_json['ssl_certificate'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['ssl_certificate_host'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['ssl_certificate_validation'] = 'testString'
        post_datasource_connection_parameters_properties_model_json['username'] = 'db2inst1'
        post_datasource_connection_parameters_properties_model_json['warehouse'] = 'testString'

        # Construct a model instance of PostDatasourceConnectionParametersProperties by calling from_dict on the json representation
        post_datasource_connection_parameters_properties_model = PostDatasourceConnectionParametersProperties.from_dict(post_datasource_connection_parameters_properties_model_json)
        assert post_datasource_connection_parameters_properties_model != False

        # Construct a model instance of PostDatasourceConnectionParametersProperties by calling from_dict on the json representation
        post_datasource_connection_parameters_properties_model_dict = PostDatasourceConnectionParametersProperties.from_dict(post_datasource_connection_parameters_properties_model_json).__dict__
        post_datasource_connection_parameters_properties_model2 = PostDatasourceConnectionParametersProperties(**post_datasource_connection_parameters_properties_model_dict)

        # Verify the model instances are equivalent
        assert post_datasource_connection_parameters_properties_model == post_datasource_connection_parameters_properties_model2

        # Convert model instance back to dict and verify no loss of data
        post_datasource_connection_parameters_properties_model_json2 = post_datasource_connection_parameters_properties_model.to_dict()
        assert post_datasource_connection_parameters_properties_model_json2 == post_datasource_connection_parameters_properties_model_json

class TestModel_PostPrimaryCatalogParametersAssetsItem():
    """
    Test Class for PostPrimaryCatalogParametersAssetsItem
    """

    def test_post_primary_catalog_parameters_assets_item_serialization(self):
        """
        Test serialization/deserialization for PostPrimaryCatalogParametersAssetsItem
        """

        # Construct a json representation of a PostPrimaryCatalogParametersAssetsItem model
        post_primary_catalog_parameters_assets_item_model_json = {}
        post_primary_catalog_parameters_assets_item_model_json['schema'] = 'db2inst1'
        post_primary_catalog_parameters_assets_item_model_json['table'] = 'EMPLOYEE'

        # Construct a model instance of PostPrimaryCatalogParametersAssetsItem by calling from_dict on the json representation
        post_primary_catalog_parameters_assets_item_model = PostPrimaryCatalogParametersAssetsItem.from_dict(post_primary_catalog_parameters_assets_item_model_json)
        assert post_primary_catalog_parameters_assets_item_model != False

        # Construct a model instance of PostPrimaryCatalogParametersAssetsItem by calling from_dict on the json representation
        post_primary_catalog_parameters_assets_item_model_dict = PostPrimaryCatalogParametersAssetsItem.from_dict(post_primary_catalog_parameters_assets_item_model_json).__dict__
        post_primary_catalog_parameters_assets_item_model2 = PostPrimaryCatalogParametersAssetsItem(**post_primary_catalog_parameters_assets_item_model_dict)

        # Verify the model instances are equivalent
        assert post_primary_catalog_parameters_assets_item_model == post_primary_catalog_parameters_assets_item_model2

        # Convert model instance back to dict and verify no loss of data
        post_primary_catalog_parameters_assets_item_model_json2 = post_primary_catalog_parameters_assets_item_model.to_dict()
        assert post_primary_catalog_parameters_assets_item_model_json2 == post_primary_catalog_parameters_assets_item_model_json

class TestModel_PrimaryCatalogInfoEntity():
    """
    Test Class for PrimaryCatalogInfoEntity
    """

    def test_primary_catalog_info_entity_serialization(self):
        """
        Test serialization/deserialization for PrimaryCatalogInfoEntity
        """

        # Construct a json representation of a PrimaryCatalogInfoEntity model
        primary_catalog_info_entity_model_json = {}
        primary_catalog_info_entity_model_json['auto_profiling'] = True
        primary_catalog_info_entity_model_json['bss_account_id'] = '999'
        primary_catalog_info_entity_model_json['capacity_limit'] = 0
        primary_catalog_info_entity_model_json['description'] = 'The governed catalog where data assets are synchronized with the Information assets view.'
        primary_catalog_info_entity_model_json['generator'] = 'Catalog-OMRS-Synced'
        primary_catalog_info_entity_model_json['is_governed'] = True
        primary_catalog_info_entity_model_json['name'] = 'Primary Catalog'

        # Construct a model instance of PrimaryCatalogInfoEntity by calling from_dict on the json representation
        primary_catalog_info_entity_model = PrimaryCatalogInfoEntity.from_dict(primary_catalog_info_entity_model_json)
        assert primary_catalog_info_entity_model != False

        # Construct a model instance of PrimaryCatalogInfoEntity by calling from_dict on the json representation
        primary_catalog_info_entity_model_dict = PrimaryCatalogInfoEntity.from_dict(primary_catalog_info_entity_model_json).__dict__
        primary_catalog_info_entity_model2 = PrimaryCatalogInfoEntity(**primary_catalog_info_entity_model_dict)

        # Verify the model instances are equivalent
        assert primary_catalog_info_entity_model == primary_catalog_info_entity_model2

        # Convert model instance back to dict and verify no loss of data
        primary_catalog_info_entity_model_json2 = primary_catalog_info_entity_model.to_dict()
        assert primary_catalog_info_entity_model_json2 == primary_catalog_info_entity_model_json

class TestModel_PrimaryCatalogInfoMetadata():
    """
    Test Class for PrimaryCatalogInfoMetadata
    """

    def test_primary_catalog_info_metadata_serialization(self):
        """
        Test serialization/deserialization for PrimaryCatalogInfoMetadata
        """

        # Construct a json representation of a PrimaryCatalogInfoMetadata model
        primary_catalog_info_metadata_model_json = {}
        primary_catalog_info_metadata_model_json['create_time'] = '2021-01-11T10:37:03Z'
        primary_catalog_info_metadata_model_json['creator_id'] = '648fb4e01000330999'
        primary_catalog_info_metadata_model_json['guid'] = '648fb4e0-3f6c-4ce3-afbb-317acc03faa4'
        primary_catalog_info_metadata_model_json['url'] = '648fb4e0/v2/catalogs/648fb4e0-3f6c-4ce3-afbb-317acc03faa4'

        # Construct a model instance of PrimaryCatalogInfoMetadata by calling from_dict on the json representation
        primary_catalog_info_metadata_model = PrimaryCatalogInfoMetadata.from_dict(primary_catalog_info_metadata_model_json)
        assert primary_catalog_info_metadata_model != False

        # Construct a model instance of PrimaryCatalogInfoMetadata by calling from_dict on the json representation
        primary_catalog_info_metadata_model_dict = PrimaryCatalogInfoMetadata.from_dict(primary_catalog_info_metadata_model_json).__dict__
        primary_catalog_info_metadata_model2 = PrimaryCatalogInfoMetadata(**primary_catalog_info_metadata_model_dict)

        # Verify the model instances are equivalent
        assert primary_catalog_info_metadata_model == primary_catalog_info_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        primary_catalog_info_metadata_model_json2 = primary_catalog_info_metadata_model.to_dict()
        assert primary_catalog_info_metadata_model_json2 == primary_catalog_info_metadata_model_json

class TestModel_TablesForRoleResponse():
    """
    Test Class for TablesForRoleResponse
    """

    def test_tables_for_role_response_serialization(self):
        """
        Test serialization/deserialization for TablesForRoleResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tables_for_role_response_objects_item_model = {} # TablesForRoleResponseObjectsItem
        tables_for_role_response_objects_item_model['table_name'] = 'testString'
        tables_for_role_response_objects_item_model['table_schema'] = 'testString'

        # Construct a json representation of a TablesForRoleResponse model
        tables_for_role_response_model_json = {}
        tables_for_role_response_model_json['objects'] = [tables_for_role_response_objects_item_model]

        # Construct a model instance of TablesForRoleResponse by calling from_dict on the json representation
        tables_for_role_response_model = TablesForRoleResponse.from_dict(tables_for_role_response_model_json)
        assert tables_for_role_response_model != False

        # Construct a model instance of TablesForRoleResponse by calling from_dict on the json representation
        tables_for_role_response_model_dict = TablesForRoleResponse.from_dict(tables_for_role_response_model_json).__dict__
        tables_for_role_response_model2 = TablesForRoleResponse(**tables_for_role_response_model_dict)

        # Verify the model instances are equivalent
        assert tables_for_role_response_model == tables_for_role_response_model2

        # Convert model instance back to dict and verify no loss of data
        tables_for_role_response_model_json2 = tables_for_role_response_model.to_dict()
        assert tables_for_role_response_model_json2 == tables_for_role_response_model_json

class TestModel_TablesForRoleResponseObjectsItem():
    """
    Test Class for TablesForRoleResponseObjectsItem
    """

    def test_tables_for_role_response_objects_item_serialization(self):
        """
        Test serialization/deserialization for TablesForRoleResponseObjectsItem
        """

        # Construct a json representation of a TablesForRoleResponseObjectsItem model
        tables_for_role_response_objects_item_model_json = {}
        tables_for_role_response_objects_item_model_json['table_name'] = 'testString'
        tables_for_role_response_objects_item_model_json['table_schema'] = 'testString'

        # Construct a model instance of TablesForRoleResponseObjectsItem by calling from_dict on the json representation
        tables_for_role_response_objects_item_model = TablesForRoleResponseObjectsItem.from_dict(tables_for_role_response_objects_item_model_json)
        assert tables_for_role_response_objects_item_model != False

        # Construct a model instance of TablesForRoleResponseObjectsItem by calling from_dict on the json representation
        tables_for_role_response_objects_item_model_dict = TablesForRoleResponseObjectsItem.from_dict(tables_for_role_response_objects_item_model_json).__dict__
        tables_for_role_response_objects_item_model2 = TablesForRoleResponseObjectsItem(**tables_for_role_response_objects_item_model_dict)

        # Verify the model instances are equivalent
        assert tables_for_role_response_objects_item_model == tables_for_role_response_objects_item_model2

        # Convert model instance back to dict and verify no loss of data
        tables_for_role_response_objects_item_model_json2 = tables_for_role_response_objects_item_model.to_dict()
        assert tables_for_role_response_objects_item_model_json2 == tables_for_role_response_objects_item_model_json

class TestModel_TurnOnPolicyV2Response():
    """
    Test Class for TurnOnPolicyV2Response
    """

    def test_turn_on_policy_v2_response_serialization(self):
        """
        Test serialization/deserialization for TurnOnPolicyV2Response
        """

        # Construct a json representation of a TurnOnPolicyV2Response model
        turn_on_policy_v2_response_model_json = {}
        turn_on_policy_v2_response_model_json['status'] = 'enabled'

        # Construct a model instance of TurnOnPolicyV2Response by calling from_dict on the json representation
        turn_on_policy_v2_response_model = TurnOnPolicyV2Response.from_dict(turn_on_policy_v2_response_model_json)
        assert turn_on_policy_v2_response_model != False

        # Construct a model instance of TurnOnPolicyV2Response by calling from_dict on the json representation
        turn_on_policy_v2_response_model_dict = TurnOnPolicyV2Response.from_dict(turn_on_policy_v2_response_model_json).__dict__
        turn_on_policy_v2_response_model2 = TurnOnPolicyV2Response(**turn_on_policy_v2_response_model_dict)

        # Verify the model instances are equivalent
        assert turn_on_policy_v2_response_model == turn_on_policy_v2_response_model2

        # Convert model instance back to dict and verify no loss of data
        turn_on_policy_v2_response_model_json2 = turn_on_policy_v2_response_model.to_dict()
        assert turn_on_policy_v2_response_model_json2 == turn_on_policy_v2_response_model_json

class TestModel_VirtualizeTableParameterSourceTableDefItem():
    """
    Test Class for VirtualizeTableParameterSourceTableDefItem
    """

    def test_virtualize_table_parameter_source_table_def_item_serialization(self):
        """
        Test serialization/deserialization for VirtualizeTableParameterSourceTableDefItem
        """

        # Construct a json representation of a VirtualizeTableParameterSourceTableDefItem model
        virtualize_table_parameter_source_table_def_item_model_json = {}
        virtualize_table_parameter_source_table_def_item_model_json['column_name'] = 'Column1'
        virtualize_table_parameter_source_table_def_item_model_json['column_type'] = 'INTEGER'

        # Construct a model instance of VirtualizeTableParameterSourceTableDefItem by calling from_dict on the json representation
        virtualize_table_parameter_source_table_def_item_model = VirtualizeTableParameterSourceTableDefItem.from_dict(virtualize_table_parameter_source_table_def_item_model_json)
        assert virtualize_table_parameter_source_table_def_item_model != False

        # Construct a model instance of VirtualizeTableParameterSourceTableDefItem by calling from_dict on the json representation
        virtualize_table_parameter_source_table_def_item_model_dict = VirtualizeTableParameterSourceTableDefItem.from_dict(virtualize_table_parameter_source_table_def_item_model_json).__dict__
        virtualize_table_parameter_source_table_def_item_model2 = VirtualizeTableParameterSourceTableDefItem(**virtualize_table_parameter_source_table_def_item_model_dict)

        # Verify the model instances are equivalent
        assert virtualize_table_parameter_source_table_def_item_model == virtualize_table_parameter_source_table_def_item_model2

        # Convert model instance back to dict and verify no loss of data
        virtualize_table_parameter_source_table_def_item_model_json2 = virtualize_table_parameter_source_table_def_item_model.to_dict()
        assert virtualize_table_parameter_source_table_def_item_model_json2 == virtualize_table_parameter_source_table_def_item_model_json

class TestModel_VirtualizeTableParameterVirtualTableDefItem():
    """
    Test Class for VirtualizeTableParameterVirtualTableDefItem
    """

    def test_virtualize_table_parameter_virtual_table_def_item_serialization(self):
        """
        Test serialization/deserialization for VirtualizeTableParameterVirtualTableDefItem
        """

        # Construct a json representation of a VirtualizeTableParameterVirtualTableDefItem model
        virtualize_table_parameter_virtual_table_def_item_model_json = {}
        virtualize_table_parameter_virtual_table_def_item_model_json['column_name'] = 'Column_1'
        virtualize_table_parameter_virtual_table_def_item_model_json['column_type'] = 'INTEGER'

        # Construct a model instance of VirtualizeTableParameterVirtualTableDefItem by calling from_dict on the json representation
        virtualize_table_parameter_virtual_table_def_item_model = VirtualizeTableParameterVirtualTableDefItem.from_dict(virtualize_table_parameter_virtual_table_def_item_model_json)
        assert virtualize_table_parameter_virtual_table_def_item_model != False

        # Construct a model instance of VirtualizeTableParameterVirtualTableDefItem by calling from_dict on the json representation
        virtualize_table_parameter_virtual_table_def_item_model_dict = VirtualizeTableParameterVirtualTableDefItem.from_dict(virtualize_table_parameter_virtual_table_def_item_model_json).__dict__
        virtualize_table_parameter_virtual_table_def_item_model2 = VirtualizeTableParameterVirtualTableDefItem(**virtualize_table_parameter_virtual_table_def_item_model_dict)

        # Verify the model instances are equivalent
        assert virtualize_table_parameter_virtual_table_def_item_model == virtualize_table_parameter_virtual_table_def_item_model2

        # Convert model instance back to dict and verify no loss of data
        virtualize_table_parameter_virtual_table_def_item_model_json2 = virtualize_table_parameter_virtual_table_def_item_model.to_dict()
        assert virtualize_table_parameter_virtual_table_def_item_model_json2 == virtualize_table_parameter_virtual_table_def_item_model_json

class TestModel_VirtualizeTableResponse():
    """
    Test Class for VirtualizeTableResponse
    """

    def test_virtualize_table_response_serialization(self):
        """
        Test serialization/deserialization for VirtualizeTableResponse
        """

        # Construct a json representation of a VirtualizeTableResponse model
        virtualize_table_response_model_json = {}
        virtualize_table_response_model_json['table_name'] = 'Tab1'
        virtualize_table_response_model_json['schema_name'] = 'dv_ibmid_060000s4y5'

        # Construct a model instance of VirtualizeTableResponse by calling from_dict on the json representation
        virtualize_table_response_model = VirtualizeTableResponse.from_dict(virtualize_table_response_model_json)
        assert virtualize_table_response_model != False

        # Construct a model instance of VirtualizeTableResponse by calling from_dict on the json representation
        virtualize_table_response_model_dict = VirtualizeTableResponse.from_dict(virtualize_table_response_model_json).__dict__
        virtualize_table_response_model2 = VirtualizeTableResponse(**virtualize_table_response_model_dict)

        # Verify the model instances are equivalent
        assert virtualize_table_response_model == virtualize_table_response_model2

        # Convert model instance back to dict and verify no loss of data
        virtualize_table_response_model_json2 = virtualize_table_response_model.to_dict()
        assert virtualize_table_response_model_json2 == virtualize_table_response_model_json

class TestModel_CatalogPublishResponse():
    """
    Test Class for CatalogPublishResponse
    """

    def test_catalog_publish_response_serialization(self):
        """
        Test serialization/deserialization for CatalogPublishResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_publish_response_duplicate_assets_item_model = {} # CatalogPublishResponseDuplicateAssetsItem
        catalog_publish_response_duplicate_assets_item_model['schema_name'] = 'USER999'
        catalog_publish_response_duplicate_assets_item_model['table_name'] = 'customer'

        catalog_publish_response_failed_assets_item_model = {} # CatalogPublishResponseFailedAssetsItem
        catalog_publish_response_failed_assets_item_model['error_msg'] = '37fa4a15-1071-4a20-bc9e-0283d3dfb6e'
        catalog_publish_response_failed_assets_item_model['schema_name'] = 'USER999'
        catalog_publish_response_failed_assets_item_model['table_name'] = 'customer'

        catalog_publish_response_published_assets_item_model = {} # CatalogPublishResponsePublishedAssetsItem
        catalog_publish_response_published_assets_item_model['schema_name'] = 'USER999'
        catalog_publish_response_published_assets_item_model['table_name'] = 'customer'
        catalog_publish_response_published_assets_item_model['wkc_asset_id'] = '37fa4a15-1071-4a20-bc9e-0283d3dfb6e1'

        # Construct a json representation of a CatalogPublishResponse model
        catalog_publish_response_model_json = {}
        catalog_publish_response_model_json['duplicate_assets'] = [catalog_publish_response_duplicate_assets_item_model]
        catalog_publish_response_model_json['failed_assets'] = [catalog_publish_response_failed_assets_item_model]
        catalog_publish_response_model_json['published_assets'] = [catalog_publish_response_published_assets_item_model]

        # Construct a model instance of CatalogPublishResponse by calling from_dict on the json representation
        catalog_publish_response_model = CatalogPublishResponse.from_dict(catalog_publish_response_model_json)
        assert catalog_publish_response_model != False

        # Construct a model instance of CatalogPublishResponse by calling from_dict on the json representation
        catalog_publish_response_model_dict = CatalogPublishResponse.from_dict(catalog_publish_response_model_json).__dict__
        catalog_publish_response_model2 = CatalogPublishResponse(**catalog_publish_response_model_dict)

        # Verify the model instances are equivalent
        assert catalog_publish_response_model == catalog_publish_response_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_publish_response_model_json2 = catalog_publish_response_model.to_dict()
        assert catalog_publish_response_model_json2 == catalog_publish_response_model_json

class TestModel_PostPrimaryCatalog():
    """
    Test Class for PostPrimaryCatalog
    """

    def test_post_primary_catalog_serialization(self):
        """
        Test serialization/deserialization for PostPrimaryCatalog
        """

        # Construct a json representation of a PostPrimaryCatalog model
        post_primary_catalog_model_json = {}
        post_primary_catalog_model_json['guid'] = 'd77fc432-9b1a-4938-a2a5-9f37e08041f6'
        post_primary_catalog_model_json['name'] = 'Default Catalog'
        post_primary_catalog_model_json['description'] = 'The governed catalog where data assets are synchronized with the Information assets view.'

        # Construct a model instance of PostPrimaryCatalog by calling from_dict on the json representation
        post_primary_catalog_model = PostPrimaryCatalog.from_dict(post_primary_catalog_model_json)
        assert post_primary_catalog_model != False

        # Construct a model instance of PostPrimaryCatalog by calling from_dict on the json representation
        post_primary_catalog_model_dict = PostPrimaryCatalog.from_dict(post_primary_catalog_model_json).__dict__
        post_primary_catalog_model2 = PostPrimaryCatalog(**post_primary_catalog_model_dict)

        # Verify the model instances are equivalent
        assert post_primary_catalog_model == post_primary_catalog_model2

        # Convert model instance back to dict and verify no loss of data
        post_primary_catalog_model_json2 = post_primary_catalog_model.to_dict()
        assert post_primary_catalog_model_json2 == post_primary_catalog_model_json

class TestModel_PrimaryCatalogInfo():
    """
    Test Class for PrimaryCatalogInfo
    """

    def test_primary_catalog_info_serialization(self):
        """
        Test serialization/deserialization for PrimaryCatalogInfo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        primary_catalog_info_entity_model = {} # PrimaryCatalogInfoEntity
        primary_catalog_info_entity_model['auto_profiling'] = True
        primary_catalog_info_entity_model['bss_account_id'] = '999'
        primary_catalog_info_entity_model['capacity_limit'] = 0
        primary_catalog_info_entity_model['description'] = 'The governed catalog where data assets are synchronized with the Information assets view.'
        primary_catalog_info_entity_model['generator'] = 'Catalog-OMRS-Synced'
        primary_catalog_info_entity_model['is_governed'] = True
        primary_catalog_info_entity_model['name'] = 'Primary Catalog'

        primary_catalog_info_metadata_model = {} # PrimaryCatalogInfoMetadata
        primary_catalog_info_metadata_model['create_time'] = '2021-01-11T10:37:03Z'
        primary_catalog_info_metadata_model['creator_id'] = '648fb4e01000330999'
        primary_catalog_info_metadata_model['guid'] = '648fb4e0-3f6c-4ce3-afbb-317acc03faa4'
        primary_catalog_info_metadata_model['url'] = '648fb4e0/v2/catalogs/648fb4e0-3f6c-4ce3-afbb-317acc03faa4'

        # Construct a json representation of a PrimaryCatalogInfo model
        primary_catalog_info_model_json = {}
        primary_catalog_info_model_json['entity'] = primary_catalog_info_entity_model
        primary_catalog_info_model_json['href'] = '/v2/catalogs/648fb4e0-3f6c-4ce3-afbb-317acc03faa4'
        primary_catalog_info_model_json['metadata'] = primary_catalog_info_metadata_model

        # Construct a model instance of PrimaryCatalogInfo by calling from_dict on the json representation
        primary_catalog_info_model = PrimaryCatalogInfo.from_dict(primary_catalog_info_model_json)
        assert primary_catalog_info_model != False

        # Construct a model instance of PrimaryCatalogInfo by calling from_dict on the json representation
        primary_catalog_info_model_dict = PrimaryCatalogInfo.from_dict(primary_catalog_info_model_json).__dict__
        primary_catalog_info_model2 = PrimaryCatalogInfo(**primary_catalog_info_model_dict)

        # Verify the model instances are equivalent
        assert primary_catalog_info_model == primary_catalog_info_model2

        # Convert model instance back to dict and verify no loss of data
        primary_catalog_info_model_json2 = primary_catalog_info_model.to_dict()
        assert primary_catalog_info_model_json2 == primary_catalog_info_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
