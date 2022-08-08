import sys
from unittest import TestCase, main, skip, skipIf, skipUnless, expectedFailure
from github_grabber import GithubApi
from json import JSONDecodeError


def skipUnlessHasattr(obj, attr):
    if hasattr(obj, attr):
        return lambda func: func
    else:
        return skip("{!r} doesn't have {!r}".format(obj, attr))


class TestAPI(TestCase):
    @skipUnlessHasattr(GithubApi(), 'PI_TOKEN')
    def test_api_token(self):
        github = GithubApi()
        self.assertEqual(github.API_TOKEN, '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')

    @skip("Skip test because of regression")
    def test_github_user(self):
        github = GithubApi()
        if not github.ok:
            self.skipTest("External resource is not available")
        self.assertIsInstance(github.USER, str)

    @skipUnless(sys.platform == 'linux', "Linux platform required")
    def test_url_invalid(self):
        github = GithubApi()
        github.query_url = "https://noapi.github.com/repos/Invalid/Link"
        with self.assertRaises(JSONDecodeError):
            github.get_json()

    @skipIf(len([True for k in GithubApi.__dict__ if k.startswith('USER')]) == 1, "Second user not found!")
    def test_second_user(self):
        github = GithubApi()
        self.assertIsInstance(github.USER2, 'dell')

    @skipUnlessHasattr(GithubApi, 'USER2')
    def test_url_valid(self):
        github = GithubApi()
        github.USER = 'dell'
        self.assertIsInstance(github.get_json(), dict)

    @expectedFailure
    def test_second_url_invalid(self):
        github = GithubApi()
        github.query_url = "https://noapi.github.com/repos/"
        self.assertEqual(github.ok, True)


if __name__ == "__main__":
    main()
