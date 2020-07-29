# What is This?

An experiment in rendering JSON responses with Jinja.

# Should I use this?

I won't and neither should you.

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

There is no front-end, only these URLs with there responses.

| Description                           | URL                                               |
| ------------------------------------- |-------------------------------------------------- |
| Plain landing page                    |             |
| Landing page with alternative feature | http://127.0.0.1:5000/api/page/landing?allow_no=1 |
| Conditional response (with extra field)  | http://127.0.0.1:5000/api/page/personal-details |
| Conditional response (without extra field)  | http://127.0.0.1:5000/api/page/personal-details?is_on_vacation=1 |

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
