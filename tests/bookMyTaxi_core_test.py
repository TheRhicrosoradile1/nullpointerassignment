# tests/bookMyTaxi_core_test.py

from typer.testing import CliRunner

from nullpointer_assignment import __app_name__, __version__, myTaxiCli

runner = CliRunner()

def test_version():
    result = runner.invoke(myTaxiCli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout