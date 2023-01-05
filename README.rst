     
################################
Build/Test/Release Working Group
################################

This repo is the home of the BTR Working Group, hosting:

- `Projects <https://github.com/openedx/build-test-release-wg/projects>`_

Discussion happens in the `BTR category at discuss.openedx.org`__.

__ https://discuss.openedx.org/c/working-groups/build-test-release/30

Synchronous meeting takes place bi-weekly (see `Working Groups Calendar`__)

__ https://calendar.google.com/calendar/u/0?cid=Y192ODZzaHJuZWdzaHNxZ3A0Zmoyazk0dTdiY0Bncm91cC5jYWxlbmRhci5nb29nbGUuY29t

Meeting notes and recordings are available in `BTR Meeting Minutes`__ in Confluence and

__ https://openedx.atlassian.net/wiki/spaces/COMM/pages/3185508485/BTR+Meeting+Minutes

More details about the working group are at the `BTR page in the wiki`__.

__ https://openedx.atlassian.net/wiki/spaces/COMM/pages/1022099494/Build+-+Test+-+Release+Working+Group

================================
Role definitions and assignments
================================

*Current release: Nutmeg*

The following roles, with corresponding expectations and assignments, are
defined for the current release cycle.

The following applies to all roles:

* Communication between assignees that is pertinent to their roles must be done
  publicly so it can be linked to, preferrably via:
* The `Build-Test-Release category`__ in the forum.

__ https://discuss.openedx.org/c/working-groups/build-test-release/30

* Github issues or PRs.
* The `group's Slack channel`__.

__ https://openedx.slack.com/archives/C01AGTSB1LL

* If communication is done via video or audio, it must be recorded and posted
  to one of the above.

Group Chair
===========

*Current assignee: @BbrSofiane*

The group chair is responsible for coordinating efforts that culminate in
getting a new release out and maintaining the current one.  In particular, the
Group Chair will:

* Manage the current release cycle in general, including making sure that
  proper deadlines are established and adhered to.
* Facilitate the assignment of roles and tasks.
* Coordinate the group's communication efforts, including running periodic
  meetings such as the Biweekly Meetup, and summarizing recent happenings in
  the Biweekly Update.
* Try and help solve problems as they come up, bringing them to the attention
  of the right group members.

Release Manager
===============

*Current assignees: @mtyaka*

The Release Manager is responsible for the actual cutting of a release, which,
in essence, includes following the steps in the `Process to Create an Open edX Release
<https://openedx.atlassian.net/wiki/spaces/COMM/pages/19662426/Process+to+Create+an+Open+edX+Release>`_.

In addition, the Release Manager will:

* Create public test or release candidate branches as required by the release process.
* Notify the Release Testing Coordinator whenever additional testing is needed
  in response to the above.
* Tag releases, major and minor, at the appropriate time.

Release Testing Coordinator
===========================

*Current assignee: @DeanJayMathew*

The Release Testing Coordinator is responsible for making sure release
candidates are tested _before_ a tag is made.  The coordinator does not
necessarily have to run tests themselves, but they will:

* Coordinate testing in general, in particular in the days leading to a timed
  release, including the bimonthly minor ones.
* Keep tabs on whatever CI is available, making sure it is running correctly.
* Advocate for better testing tools and environments, when necessary.
* Coordinate the reaction to test failures, such as bringing them to the
  attention of the rest of the group by opening tickets or commenting in the forum.

Release Documentation Expert
============================

*Current assignee: @pdpinch*

The Release Documentation Expert is tasked with building the Release Notes
document prior to a major release.  It involves:

* On a best-effort basis, track down relevant information, including but not
  limited to:
  * Reviewing commits and pull requests across Open edX repositories.
  * Collecting a summary of new features from the edX Product organization.
* Writing a draft document and posting it for community review as a PR to
  [edx-documentation](https://github.com/openedx/edx-documentation/tree/master/en_us/open_edx_release_notes/source)
  with sufficient lead time prior to a release.
* Adjusting it as per the former review, and finally releasing a final version
  concomittantly with the major release itself.

.. _Bug_Triager:

Bug Triager
===========

*Current assignee: @jfavellar90 & @NeOneSoft*

The group's Bug Triager is, in a nutshell, responsible for proper use of
the group's `issue board
<https://github.com/openedx/build-test-release-wg/projects/1>`_.  In
particular, they will:

* Review incoming issues and ensure they have been processed accordingly (to be
  specified separately).
* Assist in making sure any known release bugs are tracked with individual
  issues.  For example, if a known bug is not currently tracked, they will
  create an issue for it with relevant information.
* Bring the group's attention to any issues that warrant immediate action.
* Help ping assignees when milestone deadlines are approaching.


Community Liaison
=================

*Current assignee: @DennisBates*

The Build-Test-Release Community Liaison(s) will:

* Assist the Group Chair in communicating the group's progress in the forum.
* Take minutes of the BTR Biweekly Meetup and share them in the forum.
* Periodically reply to community communication in the Build-Test-Release
  category.
* Be on the lookout for any forum posts (not only on the
  Build-Test-Release working group category) that credibly report
  release-breaking issues, and communicate the issues to the Bug_Triager_.


===========================
Historical role assignments
===========================

Maple
======


* Group Chair: @BbrSofiane
* Release Manager: @regisb
* Release Testing Coordinator: @jfavellar90
* Release Documentation Expert: @pdpinch
* Bug Triager: @arbrandes
* Community Liaison: @DennisBates

Lilac
=====


* Group Chair: @arbrandes
* Release Manager: @nedbat & @arbrandes
* Release Testing Coordinator: @jfavellar90
* Release Documentation Expert: @pdpinch
* Bug Triager: @BbrSofiane
* Community Liaison: @arbrandes

Koa
===

Group Chair: @regisb
Release Manager: @nedbat

Juniper
=======

Group Chair: @regisb
Release Manager: @nedbat
