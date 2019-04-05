import json

from dephell.commands import PackageSearchCommand
from dephell.config import Config


def test_package_downloads_command(capsys):
    config = Config()
    config.attach({
        'level': 'WARNING',
        'silent': True,
    })

    command = PackageSearchCommand(argv=['textdistance'], config=config)
    result = command()

    assert result is True
    captured = capsys.readouterr()
    output = json.loads(captured.out)
    assert len(output) == 1
    assert output[0]['name'] == 'textdistance'
    assert output[0]['url'] == 'https://pypi.org/project/textdistance/'
