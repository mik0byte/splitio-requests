import responses


class TestTrafficTypesRequests:
    @responses.activate
    def test_get_traffic_types(self, admin_api, traffic_types):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/trafficTypes/ws/{wsid}",
            status=200,
            json=traffic_types['without_unknown']
        )

        get_traffic_types = admin_api.traffic_types.get_traffic_types(wsid)

        assert get_traffic_types
        assert get_traffic_types.json() == traffic_types['without_unknown']
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == get_traffic_types.url
