import responses


class TestSplitsRequests:
    @responses.activate
    def test_get_split(self, admin_api, splits):
        split_name = 'AEXJLFJPMHGOKQOSWWFG'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}",
            json=splits['objects'][1],
            status=200
        )

        get_split = admin_api.splits.get_split(split_name, wsid)

        assert get_split
        assert get_split.json() == splits['objects'][1]
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == get_split.url

    @responses.activate
    def test_create_split(self, admin_api, splits):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        traffic_type_id_or_name = '624a3ca1-b860-22e9-b012-0a5ed410077c'
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/trafficTypes/{traffic_type_id_or_name}",
            status=200,
            json=splits['objects'][1]
        )

        create_split = admin_api.splits.create_split(wsid, traffic_type_id_or_name,
                                                     {'name': splits['objects'][1]['name']})

        assert create_split
        assert create_split.json() == splits['objects'][1]
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == create_split.url

    @responses.activate
    def test_delete_split(self, admin_api):
        split_name = 'split1'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        responses.add(
            responses.DELETE,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}",
            status=200,
            json=True
        )

        delete_split = admin_api.splits.delete_split(split_name, wsid)

        assert delete_split
        assert delete_split.json() is True
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == delete_split.url

    @responses.activate
    def test_create_split_definition_in_environment(self, admin_api, split_definitions):
        split_name = 'AEXJLFJPMHGOKQOSWWFG'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/{environment_name}",
            json=split_definitions['objects'][3],
            status=200
        )

        create_split_definition = admin_api.splits.create_split_definition_in_environment(
            split_name,
            wsid,
            environment_name,
            split_definitions['objects'][3]
        )

        assert create_split_definition
        assert create_split_definition.json() == split_definitions['objects'][3]
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == create_split_definition.url

    @responses.activate
    def test_get_split_definition_in_environment(self, admin_api, split_definitions):
        split_name = 'AEXJLFJPMHGOKQOSWWFG'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/{environment_name}",
            json=split_definitions['objects'][3],
            status=200
        )

        get_split_definition = admin_api.splits.get_split_definition_in_environment(
            split_name,
            wsid,
            environment_name
        )

        assert get_split_definition
        assert get_split_definition.json() == split_definitions['objects'][3]
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == get_split_definition.url

    @responses.activate
    def test_partial_update_split_definition_in_environment(self, admin_api):
        json_patch = "[{\"op\": \"remove\", \"path\": \"/rules/0\"}, {\"op\": \"remove\", \"path\": " \
                     "\"/rules/0\"}, {\"op\": \"replace\", \"path\": \"/lastUpdateTime\", \"value\": 1590129125381}]"
        split_name = 'AEXJLFJPMHGOKQOSWWFG'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        responses.add(
            responses.PATCH,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/{environment_name}",
            status=200
        )

        partial_update_split_definition = admin_api.splits.partial_update_split_definition_in_environment(
            split_name,
            wsid,
            environment_name,
            patch_string=json_patch
        )

        assert partial_update_split_definition
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == partial_update_split_definition.url

    @responses.activate
    def test_remove_split_definition_from_environment(self, admin_api):
        split_name = 'AEXJLFJPMHGOKQOSWWFG'
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        responses.add(
            responses.DELETE,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/{environment_name}",
            status=200,
            json=True
        )

        remove_split_definition = admin_api.splits.remove_split_definition_from_environment(
            split_name,
            wsid,
            environment_name
        )

        assert remove_split_definition
        assert remove_split_definition.json() is True
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == remove_split_definition.url

    @responses.activate
    def test_list_split_definitions_in_environment(self, admin_api, split_definitions):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        environment_name = 'Prod'
        limit = 50
        offset = 0
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/environments/{environment_name}"
            f"?limit={limit}&offset={offset}",
            json=split_definitions,
            status=200
        )

        for split_definitions_chunk in admin_api.splits.list_split_definitions_in_environment(wsid, environment_name):
            assert split_definitions_chunk
            assert split_definitions == split_definitions_chunk.json()
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == split_definitions_chunk.url

    @responses.activate
    def test_list_splits(self, admin_api, splits):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        limit = 50
        offset = 0
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}?limit={limit}&offset={offset}",
            json=splits,
            status=200
        )

        for splits_list in admin_api.splits.list_splits(wsid):
            assert splits_list
            assert splits_list.json() == splits
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == splits_list.url

    @responses.activate
    def test_update_split_description(self, admin_api):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        split_name = "split1"
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/updateDescription",
            json={'data': 'new description'},
            status=200
        )

        update_split_description = admin_api.splits.update_split_description(split_name, wsid, 'new description')

        assert update_split_description
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == update_split_description.url

    @responses.activate
    def test_full_update_split_definition_in_environment(self, admin_api, split_definitions):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        split_name = "a"
        environment_name = 'Prod'
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/{environment_name}",
            json=split_definitions['objects'][3],
            status=200
        )

        full_update_split_definition = admin_api.splits.full_update_split_definition_in_environment(
            split_name,
            wsid,
            environment_name,
            split_definitions['objects'][3]
        )

        assert full_update_split_definition
        assert full_update_split_definition.json() == split_definitions['objects'][3]
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == full_update_split_definition.url

    @responses.activate
    def test_kill_split_in_environment(self, admin_api):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        split_name = "a"
        environment_name = 'Prod'
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/"
            f"{environment_name}/kill",
            status=200
        )

        kill_split_in_environment = admin_api.splits.kill_split_in_environment(
            split_name,
            wsid,
            environment_name
        )

        assert kill_split_in_environment
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == kill_split_in_environment.url

    @responses.activate
    def test_restore_split_in_environment(self, admin_api):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        split_name = "a"
        environment_name = 'Prod'
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/splits/ws/{wsid}/{split_name}/environments/"
            f"{environment_name}/restore",
            status=200
        )

        restore_split_in_environment = admin_api.splits.restore_split_in_environment(
            split_name,
            wsid,
            environment_name
        )

        assert restore_split_in_environment
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == restore_split_in_environment.url
