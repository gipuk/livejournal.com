Feature: Publish post error
As logged user I want to post new post

Scenario: Cannot publish new post
Given user is logged in
When I click post new entry
And I fill all fields
And click Publish button
Then there is an error message