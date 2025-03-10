========================
Base Search Mail Content
========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:a94362371dead252623eb54d05bc7f31372ba915df8519b6a0b62ab709b3d2d1
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fsocial-lightgray.png?logo=github
    :target: https://github.com/OCA/social/tree/17.0/base_search_mail_content
    :alt: OCA/social
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/social-17-0/social-17-0-base_search_mail_content
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/social&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds the capability to find on any object (e.g. project
issues or helpdesk ticket) based on the conversation threads associated
to them.

This will be useful in models that make intense use of messages, like
project issues or helpdesk tickets.

A project issue or helpdesk ticket can contain tens of mails or notes
associated, based on the feedback that the person responsible for the
ticket maintains, including conversations with the person that raised
the issue.

A user may often want to find issues or tickets, based on the past
conversations that were recorded, as much as he or she needs to search
in their mail for past conversations.

This module will add dynamically a field 'message_content' to the search
view of any model that inherits from the mail.thread.

The current search capabilities include searching into the subject,
body, email from, reply to and record name.

**Table of contents**

.. contents::
   :local:

Installation
============

This module creates the GIN (trigram) indexes for these fields of
mail.message: subject, body, record_name, email_from, reply_to.

Usage
=====

Go to any model that contains a chatter (e.g. Contacts, ...). Search for
content in field 'Message Content'.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/social/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/social/issues/new?body=module:%20base_search_mail_content%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* ForgeFlow
* SerpentCS
* Tecnativa

Contributors
------------

-  Jordi Ballester Alomar <jordi.ballester@forgeflow.com>
-  Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>
-  Lois Rilo Antelo <lois.rilo@forgeflow.com>
-  Aaron Henriquez <ahenriquez@forgeflow.com>
-  `Tecnativa <https://www.tecnativa.com>`__:

   -  Vicent Cubells
   -  Ernesto Tejeda

-  Nguyen Minh Chien <chien@trobz.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/social <https://github.com/OCA/social/tree/17.0/base_search_mail_content>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
