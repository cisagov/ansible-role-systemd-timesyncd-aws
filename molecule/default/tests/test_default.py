"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_config(host):
    """Verify that systemd-timesyncd is correctly configured."""
    command = "systemd-analyze cat-config systemd/timesyncd.conf"
    cmd = host.run(command)
    assert cmd.rc == 0, f"Command {command} did not exit with status 0."
    assert (
        "NTP=169.254.169.123" in cmd.stdout
    ), f"Output of command {command} did not contain the expected content."
