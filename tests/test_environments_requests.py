import responses


class TestEnvironmentsRequests:
    @responses.activate
    def test_get_environments(self, admin_api, environments):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/environments/ws/{wsid}",
            status=200,
            json=environments['environments']['without_unknown']
        )

        get_environments = admin_api.environments.get_environments(wsid)

        assert get_environments
        assert get_environments.json() == environments['environments']['without_unknown']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == get_environments.url

    @responses.activate
    def test_create_environment(self, admin_api, environments):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/environments/ws/{wsid}",
            status=200,
            json=environments['environment']['without_unknown']
        )

        create_environment = admin_api.environments.create_environment(wsid, 'New-Env', False)

        assert create_environment
        assert create_environment.json() == environments['environment']['without_unknown']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == create_environment.url

    @responses.activate
    def test_delete_environment(self, admin_api):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name_or_id = 'New-Name'
        responses.add(
            responses.DELETE,
            f"https://api.split.io/internal/api/v2/environments/ws/{wsid}/{environment_name_or_id}",
            status=200,
            json=True
        )

        delete_environment = admin_api.environments.delete_environment(wsid, environment_name_or_id)

        assert delete_environment
        assert delete_environment.json() is True
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == delete_environment.url

    @responses.activate
    def test_update_environment(self, admin_api, environments):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        responses.add(
            responses.PATCH,
            f"https://api.split.io/internal/api/v2/environments/ws/{wsid}/{environment_name}",
            json=environments['environment']['without_unknown'],
            status=200
        )

        update_environment = admin_api.environments.update_environment(
            wsid,
            environment_name,
            patch_string='[{"op": "replace", "path": "/name", "value":"NewName"}]'
        )

        assert update_environment
        assert update_environment.json() == environments['environment']['without_unknown']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == update_environment.url
