Feature: Close old sessions
As logged user I want to close old activities

Scenario: Close old sessions.
Given user is logged in
When I enter settings
And I enter history tab
Then Old session is closed
