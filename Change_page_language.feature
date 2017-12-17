Feature: Language change
As logged user I want to change page language

Scenario: Change page language
Given user is logged in
When I enter settings
And I enter display tab
And I change language to german
Then page is available in german
