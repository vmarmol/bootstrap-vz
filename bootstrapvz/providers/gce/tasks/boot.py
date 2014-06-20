from bootstrapvz.base import Task
from bootstrapvz.common import phases
from bootstrapvz.common.tasks import boot
import os.path


class ConfigureGrub(Task):
	description = 'Change grub configuration to allow for ttyS0 output and enable the memory cgroup'
	phase = phases.system_modification
	successors = [boot.InstallGrub]

	@classmethod
	def run(cls, info):
		from bootstrapvz.common.tools import sed_i
		grub_config = os.path.join(info.root, 'etc/default/grub')
		sed_i(grub_config, r'^(GRUB_CMDLINE_LINUX*=".*)"\s*$', r'\1console=ttyS0,38400n8 cgroup_enable=memory"')
		sed_i(grub_config, r'^.*(GRUB_TIMEOUT=).*$', r'GRUB_TIMEOUT=0')
