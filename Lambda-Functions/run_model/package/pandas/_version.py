
# This file was generated by 'versioneer.py' (0.15) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

from warnings import catch_warnings
with catch_warnings(record=True):
    import json
import sys

version_json = '''
{
 "dirty": false,
 "error": null,
 "full-revisionid": "62a87bf4a2af02a8d3bc271ad26e5994292b8e6a",
 "version": "0.25.3"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
