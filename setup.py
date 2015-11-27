from setuptools import setup

setup (
	name='ditfile-automator',
	version='0.0',
	install_requires=[
		'click'
	],
	entry_points='''
		[console_scripts]
		dfa=project.cli:cli
	''',
)
