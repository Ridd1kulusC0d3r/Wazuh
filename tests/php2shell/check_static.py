"""Validate snapshot integrity and structure, never Wazuh runtime semantics.

Run from repository root: python tests/php2shell/check_static.py
Requires PyYAML. Does not execute SCA commands or send network requests.
"""
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET
import yaml

root = Path(__file__).resolve().parents[2]
vendor = root / 'vendor/php2shell'
manifest = json.loads((vendor / 'manifest.json').read_text())
for entry in manifest['files']:
    content = (vendor / entry['path']).read_bytes()
    digest = hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()
    assert digest == entry['git_blob_sha'], f"Snapshot changed: {entry['path']}"

rules = ET.parse(vendor / 'rules/php2shell_rules.xml').getroot()
ids = [node.attrib['id'] for node in rules.findall('rule')]
assert len(ids) == len(set(ids)) == 6
assert set(ids) == {'100100', '100101', '100110', '100120', '100130', '100131'}
decoders = ET.fromstring('<root>' + (vendor / 'decoders/php2shell_decoders.xml').read_text() + '</root>')
assert len(decoders.findall('decoder')) == 3
sca = yaml.safe_load((vendor / 'sca/php2shell_cve_2026_109618_109619.yml').read_text())
assert {check['id'] for check in sca['checks']} == set(range(109600, 109605))
fixtures = json.loads((root / 'tests/php2shell/fixtures.json').read_text())
assert len({case['id'] for case in fixtures}) == len(fixtures) == 5
for case in fixtures:
    assert case['log'].startswith('php2shell ip=')
    assert set(case.get('expected_rules', [])).issubset(ids)
print('PASS: upstream blob hashes; 6 rules; 3 decoders; 5 SCA checks; 5 fixtures.')
print('NOT TESTED: Wazuh matching, frequency, SCA execution, ingestion or alert delivery.')
