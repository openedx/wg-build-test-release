================
Release timeline
================

-------
Status
-------

Draft

-------
Context
-------

The technical release process is currently documented in `a Confluence page
<https://openedx.atlassian.net/wiki/spaces/COMM/pages/19662426/Process+to+Create+an+Open+edX+Release>`__;
this is not an attempt to replace or duplicate it.  Rather, the BTR group needs
to document the timeframe of each release, such as:

* When the ``master`` branch should be split into ``open-release/zebrawood.master``.
* When release candidates come out.
* What is the deadline for testing.
* What is the deadline for the release notes to be put up for review.
* etc

The changes to the current process were initially proposed `in the discussion forum
<https://discuss.openedx.org/t/a-modest-proposal-for-lilac-and-beyond/4070>`__

---------
Decisions
---------

#. Releases will be made twice a year, once on June 9th, and the other on
   December 9th.

#. The release timeline will proceed as follows, where "zebrawood" is to be
   replaced with the upcoming release's actual name:

   +---------------------------+------------------------------------------------+
   | Time prior to release day | Event                                          |
   +===========================+================================================+
   | 8 weeks                   | ``open-release/zebrawood.master`` branched off |
   |                           | Release note development starts                |
   +---------------------------+------------------------------------------------+
   | 6 weeks                   | Development milestone 1                        |
   +---------------------------+------------------------------------------------+
   | 4 weeks                   | Development milestone 2                        |
   |                           | Release notes are put up for review            |
   +---------------------------+------------------------------------------------+
   | 2 weeks                   | Development milestone 3                        |
   +---------------------------+------------------------------------------------+
   | 0 days                    | ``open-release/zebrawood.1`` is tagged         |
   +---------------------------+------------------------------------------------+

#. The above timeline will be posted to the forum as a wiki post, with specific
   dates, as soon as development on the release begins (much like how `Ubuntu
   does it <https://discourse.ubuntu.com/t/hirsute-hippo-release-schedule/18539>`__).

------------
Consequences
------------

This will hopefully result in:

* More time for testing, and thus a better-quality release
* Release notes produced in time for release
