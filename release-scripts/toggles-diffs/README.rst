README
#######

A folder that holds scripts to generate the diffs in toggles and settings between arbitrary releases.

* ``default-diff.py``: Generates a report of what defaults have changed for existing flags, formatted for RST.
  See file header for usage details.

* ``settings-flags-diff.py``: Generates the new and removed featuretoggles & settings for this release, compared to the last release,
  formatted for RST. New featuretoggles & settings will also list their default values. See file header for usage details.

* ``sumac-xml``: The ``_build/xml`` directory from the edx-platform docs build for the Sumac release.

* ``teak-xml``: The ``_build/xml`` directory from the edx-platform docs build for the Sumac release.

For the xml directories, the needed files are in the ``releasename-xml/references`` directory.
