import os

import responses


class TestSegmentsRequests:
    @responses.activate
    def test_create_segment(self, admin_api, segments):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        traffic_type_id_or_name = '624a3ca1-b777-22e9-b012-0a5ed410077b'
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/segments/ws/{wsid}/trafficTypes/{traffic_type_id_or_name}",
            status=200,
            json=segments['segment_create']['without_unknown']
        )

        create_segment = admin_api.segments.create_segment(
            wsid,
            traffic_type_id_or_name,
            segments['segment_create']['without_unknown']
        )

        assert create_segment
        assert create_segment.json() == segments['segment_create']['without_unknown']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == create_segment.url

    @responses.activate
    def test_delete_segment(self, admin_api):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        segment_name = 'test_segment'
        responses.add(
            responses.DELETE,
            f"https://api.split.io/internal/api/v2/segments/ws/{wsid}/{segment_name}",
            status=200,
            json='true'
        )

        delete_segment = admin_api.segments.delete_segment(wsid, segment_name)

        assert delete_segment
        assert delete_segment.json() == 'true'
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == delete_segment.url

    @responses.activate
    def test_enable_segment_in_environment(self, admin_api, segments):
        environment_id = segments['segment_in_environment']['environment']['id']
        segment_name = segments['segment_in_environment']['name']
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}",
            status=200,
            json=segments['segment_in_environment']
        )

        enable_segment_in_environment = admin_api.segments.enable_segment_in_environment(
            environment_id,
            segment_name
        )

        assert enable_segment_in_environment
        assert enable_segment_in_environment.json() == segments['segment_in_environment']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == enable_segment_in_environment.url

    @responses.activate
    def test_deactivate_segment_in_environment(self, admin_api, segments):
        environment_id = segments['segment_in_environment']['environment']['id']
        segment_name = segments['segment_in_environment']['name']
        responses.add(
            responses.DELETE,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}",
            status=200,
            json=segments['segment_in_environment']
        )

        deactivate_segment_in_environment = admin_api.segments.deactivate_segment_in_environment(
            environment_id,
            segment_name
        )

        assert deactivate_segment_in_environment
        assert deactivate_segment_in_environment.json() == segments['segment_in_environment']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == deactivate_segment_in_environment.url

    @responses.activate
    def test_list_segments(self, admin_api, segments):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        limit = 50
        offset = 0
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/segments/ws/{wsid}?limit={limit}&offset={offset}",
            json=segments['list_segments_workspace'],
            status=200
        )

        for segments_chunk in admin_api.segments.list_segments(wsid):
            assert segments_chunk
            assert segments['list_segments_workspace'] == segments_chunk.json()
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == segments_chunk.url

    @responses.activate
    def test_list_segments_in_environment(self, admin_api, segments):
        environment_id = segments['list_segments_environment']['objects'][0]['environment']['id']
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        limit = 50
        offset = 0
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/segments/ws/{wsid}/environments/{environment_id}"
            f"?limit={limit}&offset={offset}",
            json=segments['list_segments_environment'],
            status=200
        )

        for segments_chunk in admin_api.segments.list_segments_in_environment(wsid, environment_id):
            assert segments_chunk
            assert segments['list_segments_environment'] == segments_chunk.json()
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == segments_chunk.url

    @responses.activate
    def test_update_segment_keys_in_environment_via_csv(self, admin_api, segments):
        environment_id = segments['create_segment_keys_resp']['environment']
        segment_name = segments['create_segment_keys_resp']['name']
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}/upload?replace=False",
            json=segments['create_segment_keys_resp'],
            status=200
        )

        csv_file_path = os.path.join(os.path.dirname(__file__), 'test_data')
        csv_file_name = 'segment_keys.csv'

        update_segment_keys_in_environment_via_csv = admin_api.segments.update_segment_keys_in_environment_via_csv(
            environment_id,
            segment_name,
            csv_file_path,
            csv_file_name
        )

        assert update_segment_keys_in_environment_via_csv
        assert update_segment_keys_in_environment_via_csv.json() == segments['create_segment_keys_resp']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == update_segment_keys_in_environment_via_csv.url

    @responses.activate
    def test_update_segment_keys_in_environment_via_json(self, admin_api, segments):
        environment_id = segments['create_segment_keys_resp']['environment']
        segment_name = segments['create_segment_keys_resp']['name']
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}/uploadKeys?replace=False",
            json=segments['create_segment_keys_resp'],
            status=200
        )

        update_segment_keys_in_environment_via_json = admin_api.segments.update_segment_keys_in_environment_via_json(
            environment_id,
            segment_name,
            segments['create_segment_keys']
        )

        assert update_segment_keys_in_environment_via_json
        assert update_segment_keys_in_environment_via_json.json() == segments['create_segment_keys_resp']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == update_segment_keys_in_environment_via_json.url

    @responses.activate
    def test_get_segment_keys_in_environment(self, admin_api, segments):
        environment_id = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        segment_name = 'test_segment'
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}/keys",
            json=segments['segment_keys_environment'],
            status=200
        )

        get_segment_keys_in_environment = admin_api.segments.get_segment_keys_in_environment(
            environment_id,
            segment_name,
        )

        assert get_segment_keys_in_environment
        assert get_segment_keys_in_environment.json() == segments['segment_keys_environment']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == get_segment_keys_in_environment.url

    @responses.activate
    def test_remove_segment_keys_from_environment(self, admin_api, segments):
        environment_id = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        segment_name = 'test_segment'
        responses.add(
            responses.PUT,
            f"https://api.split.io/internal/api/v2/segments/{environment_id}/{segment_name}/removeKeys",
            json=segments['remove_segment_keys'],
            status=200
        )

        remove_segment_keys_from_environment = admin_api.segments.remove_segment_keys_from_environment(
            environment_id,
            segment_name,
            segments['segment_keys_environment']
        )

        assert remove_segment_keys_from_environment
        assert remove_segment_keys_from_environment.json() == segments['remove_segment_keys']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == remove_segment_keys_from_environment.url
