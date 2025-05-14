from flask import app, jsonify
from service.models import Product
from flask import request
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5000"


@when('I visit the "{page}"')
def step_impl(context, page):
    context.browser.get(BASE_URL)

@when('I set the "{field}" to "{value}"')
def step_impl(context, field, value):
    context.browser.find_element(By.ID, field).clear()
    context.browser.find_element(By.ID, field).send_keys(value)

@when('I press the "{button}" button')
def step_impl(context, button):
    context.browser.find_element(By.ID, button.lower()).click()

@then('I should see "{text}"')
def step_impl(context, text):
    assert text in context.browser.page_source