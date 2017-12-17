Feature: Post in Draft
As login user I want to post new entry as a draft

Scenario: Post new entry as a draft
Given user is logged in
When I click post new entry
And I fill all fields
And click Draft button
Then new entry post is saved as a draft

