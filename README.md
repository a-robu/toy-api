# What is This?

An experiment in rendering JSON responses with Jinja.

# Should I use this?

No, I won't and neither should you.

# What does it do?

It shows some JSON responses.

# Setup

Setup by installing the dependencies. Was tested and worked with Python 3.8.2.

```bash
python -m venv env
. env/bin/activate
pip install -r requirements.txt
```

# Running

Run the following commands.

```bash
. env/bin/activate
env FLASK_APP=app.py flask run
```

Now open http://127.0.0.1:5000/ in your browser.

# Example URLs

There is no front-end, only these URLs with these responses.

## [Plain landing page](http://127.0.0.1:5000/api/page/landing)

```json
{
  "fields": [
    {
      "label": "Your name, as given at birth.", 
      "type": "input-text-line"
    }, 
    {
      "label": "Write a complete essay on the motions of heavenly bodies.", 
      "type": "input-text-block"
    }, 
    {
      "label": "Are you currently on vacation?", 
      "name": "is_on_vacation", 
      "type": "input-boolean"
    }, 
    {
      "choices": {
        "evasive": "I'm here to talk business, not animals.", 
        "yes": "Yes, I do.", 
        "yes-but": "Yes, but how does that change anything?"
      }, 
      "label": "Do you have a pet?", 
      "type": "input-option"
    }
  ], 
  "heading": "Welcome to Cat & Bear", 
  "next-page": "personal-details"
}
```

## [Landing page with alternative feature](http://127.0.0.1:5000/api/page/landing?allow_no=1)

**+ additional dropdown option**

```json
{
  "fields": [
    {
      "label": "Your name, as given at birth.", 
      "type": "input-text-line"
    }, 
    {
      "label": "Write a complete essay on the motions of heavenly bodies.", 
      "type": "input-text-block"
    }, 
    {
      "label": "Are you currently on vacation?", 
      "name": "is_on_vacation", 
      "type": "input-boolean"
    }, 
    {
      "choices": {
        "evasive": "I'm here to talk business, not animals.", 
        "no": "No, I know of no such animals.", 
        "yes": "Yes, I do.", 
        "yes-but": "Yes, but how does that change anything?"
      }, 
      "label": "Do you have a pet?", 
      "type": "input-option"
    }
  ], 
  "heading": "Welcome to Cat & Bear", 
  "next-page": "personal-details"
}
```

## [A dependant page](http://127.0.0.1:5000/api/page/personal-details)

```json
{
  "fields": [
    {
      "choices": {
        "yes": "Yes, I do.", 
        "yes-of-course": "Of course I like pets!"
      }, 
      "label": "Do you like pets?", 
      "type": "input-option"
    }
  ], 
  "heading": "Personal Details", 
  "next-page": "confirmation"
}
```

## [A dependant page (with additional question shown)](http://127.0.0.1:5000/api/page/personal-details?is_on_vacation=1)

**+additional question displayed**

```json
{
  "fields": [
    {
      "input-constraints": {
        "integer": true, 
        "min-value": 0
      }, 
      "label": "How many years have you been on medication for?", 
      "type": "input-number"
    }, 
    {
      "choices": {
        "yes": "Yes, I do.", 
        "yes-of-course": "Of course I like pets!"
      }, 
      "label": "Do you like pets?", 
      "type": "input-option"
    }
  ], 
  "heading": "Personal Details", 
  "next-page": "confirmation"
}
```

# Pros / Cons

So what are the limitations and what is good about this?

## Pros

- By placing the whole response (essentially) in the Jinja template, it's easy to see what the actual response will be. And we can see the conditional checks there also.
- It's easy to add feature flags, A/B choices or conditional questions. Just put them in the template.

## Cons

- It's a weird/ad-hoc idea.
- It's not appropriate to edit the response manually if each field has many properties. In that case, it's more appropriate to generate the field properties in code.

# Limitations

- Error responses are not taken into consideration here.
- There is no mechnaism to provide API versioning.
