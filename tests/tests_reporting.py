
from __future__ import absolute_import
from .fixtures import reporting_returns
from ae_preflight import profile


import glob
import sys
import os


if sys.version_info[:2] >= (2, 7):
    from unittest import TestCase
else:
    from unittest2 import TestCase


try:
    from unittest import mock
except ImportError:
    import mock


class TestReporting(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        files = glob.glob('results.txt')
        for item in files:
            os.remove(item)

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_ubuntu(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('ubuntu')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'check_sysctl'
                                        ) as sysctl:
                                            sysctl.return_value = (
                                                reporting_returns.sysctl()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_dir_paths'
                                            ) as check_dir:
                                                check_dir.return_value = (
                                                    reporting_returns.check_dirs()  # noqa
                                                )
                                                profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/ubuntu_pass.txt', 'r') as ubuntu:
            expected = ubuntu.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_suse(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('suse')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'suse_infinity_check'
                                        ) as infinity:
                                            infinity.return_value = (
                                                reporting_returns.infinity()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_sysctl'
                                            ) as sysctl:
                                                sysctl.return_value = (
                                                    reporting_returns.sysctl()
                                                )
                                                with mock.patch(
                                                    'ae_preflight.profile.'
                                                    'check_dir_paths'
                                                ) as check_dir:
                                                    check_dir.return_value = (
                                                        reporting_returns.check_dirs()  # noqa
                                                    )
                                                    profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/suse_pass.txt', 'r') as suse:
            expected = suse.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_rhel(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('rhel')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.selinux'
                                        ) as selinux:
                                            selinux.return_value = (
                                                reporting_returns.selinux()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_sysctl'
                                            ) as sysctl:
                                                sysctl.return_value = (
                                                    reporting_returns.sysctl()
                                                )
                                                with mock.patch(
                                                    'ae_preflight.profile.'
                                                    'check_dir_paths'
                                                ) as check_dir:
                                                    check_dir.return_value = (
                                                        reporting_returns.check_dirs()  # noqa
                                                    )
                                                    profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/centos_pass.txt', 'r') as centos:
            expected = centos.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_fail_suse(self, mock_args):
        test_pass = False
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('suse')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability(
                    test_pass
                )
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu(test_pass)
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts(
                            test_pass
                        )
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf(test_pass)
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports(test_pass)
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents(test_pass)
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules(
                                                test_pass
                                            )
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'suse_infinity_check'
                                        ) as infinity:
                                            infinity.return_value = (
                                                reporting_returns.infinity(
                                                    test_pass
                                                )
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_sysctl'
                                            ) as sysctl:
                                                sysctl.return_value = (
                                                    reporting_returns.sysctl(
                                                        test_pass
                                                    )
                                                )
                                                with mock.patch(
                                                    'ae_preflight.profile.'
                                                    'check_dir_paths'
                                                ) as check_dir:
                                                    check_dir.return_value = (
                                                        reporting_returns.check_dirs(test_pass)  # noqa
                                                    )
                                                    profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/suse_fail.txt', 'r') as suse:
            expected = suse.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_fail_rhel(self, mock_args):
        test_pass = False
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('rhel')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability(
                    test_pass
                )
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu(test_pass)
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts(
                            test_pass
                        )
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf(test_pass)
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports(test_pass)
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents(test_pass)
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules(
                                                test_pass
                                            )
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.selinux'
                                        ) as selinux:
                                            selinux.return_value = (
                                                reporting_returns.selinux(
                                                    test_pass
                                                )
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_sysctl'
                                            ) as sysctl:
                                                sysctl.return_value = (
                                                    reporting_returns.sysctl(
                                                        test_pass
                                                    )
                                                )
                                                with mock.patch(
                                                    'ae_preflight.profile.'
                                                    'check_dir_paths'
                                                ) as check_dir:
                                                    check_dir.return_value = (
                                                        reporting_returns.check_dirs(test_pass)  # noqa
                                                    )
                                                    profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/centos_fail.txt', 'r') as centos:
            expected = centos.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_ubuntu_trigger_warn_on_fs(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('ubuntu')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts(
                            test_pass=False
                        )
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'check_sysctl'
                                        ) as sysctl:
                                            sysctl.return_value = (
                                                reporting_returns.sysctl()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_dir_paths'
                                            ) as check_dir:
                                                check_dir.return_value = (
                                                    reporting_returns.check_dirs()  # noqa
                                                )
                                                profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/fs_warn.txt', 'r') as ubuntu:
            expected = ubuntu.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_ubuntu_trigger_warn_resolve(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('ubuntu')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf_warn()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'check_sysctl'
                                        ) as sysctl:
                                            sysctl.return_value = (
                                                reporting_returns.sysctl()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_dir_paths'
                                            ) as check_dir:
                                                check_dir.return_value = (
                                                    reporting_returns.check_dirs()  # noqa
                                                )
                                                profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/resolv_warn.txt', 'r') as ubuntu:
            expected = ubuntu.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_ubuntu_trigger_warn_on_interface(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('ubuntu')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports(test_pass=False)
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents()
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'check_sysctl'
                                        ) as sysctl:
                                            sysctl.return_value = (
                                                reporting_returns.sysctl()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_dir_paths'
                                            ) as check_dir:
                                                check_dir.return_value = (
                                                    reporting_returns.check_dirs()  # noqa
                                                )
                                                profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/ports_warn.txt', 'r') as ubuntu:
            expected = ubuntu.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )

    @mock.patch('ae_preflight.profile.argparse')
    def test_reporting_ubuntu_trigger_warn_on_agents(self, mock_args):
        with mock.patch('ae_preflight.profile.get_os_info') as os:
            os.return_value = reporting_returns.os_return('ubuntu')
            with mock.patch(
                'ae_preflight.profile.check_system_type'
            ) as system:
                system.return_value = reporting_returns.system_compatability()
                with mock.patch(
                    'ae_preflight.profile.system_requirements'
                ) as req:
                    req.return_value = reporting_returns.memory_cpu()
                    with mock.patch(
                        'ae_preflight.profile.mounts_check'
                    ) as mount:
                        mount.return_value = reporting_returns.mounts()
                        with mock.patch(
                            'ae_preflight.profile.inspect_resolv_conf'
                        ) as resolv:
                            resolv.return_value = (
                                reporting_returns.resolv_conf()
                            )
                            with mock.patch(
                                'ae_preflight.profile.check_open_ports'
                            ) as port:
                                port.return_value = (
                                    reporting_returns.ports()
                                )
                                with mock.patch(
                                    'ae_preflight.profile.check_for_agents'
                                ) as agent:
                                    agent.return_value = (
                                        reporting_returns.agents(
                                            test_pass=False
                                        )
                                    )
                                    with mock.patch(
                                        'ae_preflight.profile.check_modules'
                                    ) as module:
                                        module.return_value = (
                                            reporting_returns.modules()
                                        )
                                        with mock.patch(
                                            'ae_preflight.profile.'
                                            'check_sysctl'
                                        ) as sysctl:
                                            sysctl.return_value = (
                                                reporting_returns.sysctl()
                                            )
                                            with mock.patch(
                                                'ae_preflight.profile.'
                                                'check_dir_paths'
                                            ) as check_dir:
                                                check_dir.return_value = (
                                                    reporting_returns.check_dirs()  # noqa
                                                )
                                                profile.main()

        results_file = glob.glob('results.txt')
        self.assertEqual(
            len(results_file),
            1,
            'Did not find results file'
        )
        expected = []
        with open('tests/fixtures/agents_warn.txt', 'r') as ubuntu:
            expected = ubuntu.readlines()

        differences = []
        with open('results.txt', 'r') as results:
            for line in results:
                if line not in expected:
                    differences.append(line)

        self.assertEquals(
            differences,
            [],
            'Differences were found in the results from what is expected'
        )
