import responses


class TestWorkspacesRequests:
    @responses.activate
    def test_get_workspaces(self, admin_api, workspaces):
        limit = 50
        offset = 0
        responses.add(
            responses.GET,
            f"https://api.split.io/internal/api/v2/workspaces?limit={limit}&offset={offset}",
            json=workspaces,
            status=200
        )

        for workspace_list in admin_api.workspaces.get_workspaces():
            assert workspace_list
            assert workspace_list.json() == workspaces
            assert len(responses.calls) == 1
            assert responses.calls[0].request.url == workspace_list.url
