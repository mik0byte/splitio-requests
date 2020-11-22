import responses


class TestTagsRequests:
    @responses.activate
    def test_associate_tags(self, admin_api, tags):
        wsid = '624a3ca1-b777-22e9-b012-0a5ed410077c'
        object_name = 'split1'
        object_type = 'Split'
        tags_payload = ["tag2", "tag3", "tag4", "tag5", "tag6", "tag7", "tag8", "tag9", "tag10"]
        responses.add(
            responses.POST,
            f"https://api.split.io/internal/api/v2/tags/ws/{wsid}/object/{object_name}/objecttype/{object_type}",
            status=200,
            json=tags
        )

        associate_tags = admin_api.tags.associate_tags(wsid, object_name, object_type, tags_payload)

        assert associate_tags
        assert associate_tags.json() == tags
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url == associate_tags.url
