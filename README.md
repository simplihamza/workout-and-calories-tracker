# Workout Tracker

A command-line script that logs workouts to a Google Sheet. You describe
what you did in plain English, the script uses the Nutritionix natural-language exercise API to estimate duration and calories burned,
and the result is appended to a Google Sheet via the Sheety API.

## Features

- Accepts a free-text description of an activity (e.g. "ran 5km, played
  basketball for 30 minutes") from terminal input.
- Sends the description, along with your gender, weight, height, and age,
  to the Nutritionix natural-language exercise endpoint to estimate
  calories burned and duration for each exercise mentioned.
- Appends the result to a Google Sheet (via Sheety), recording the date,
  time, duration, and calories.
- Loads API keys and personal stats from a `.env` file instead of
  hardcoding them in the script.

## How to Run

1. Clone the repo.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in:
   - `APP_ID`, `API_KEY`: your Nutritionix (100 Days of Python proxy) app
     ID and API key
   - `GENDER`, `WEIGHT_KG`, `HEIGHT_CM`, `AGE`: your personal stats, used
     to estimate calories burned
   - `EXERCISE_ENDPOINT`: the Nutritionix natural-language exercise
     endpoint URL
   - `SHEETY_ENDPOINT`: your Sheety project's endpoint URL for the sheet
4. Set up a Google Sheet and a Sheety project for it (with columns:
   Exercise, Date, Time, Duration, Calories), then set `SHEETY_ENDPOINT`
   in `.env` to that project's endpoint.
5. Run the script and enter the activity when prompted:
   ```
   python main.py
   ```

## Known Issues / Limitations

- No error handling around API responses (e.g. failed requests, missing
  fields, invalid input).

## What I Learned

- Chaining two external APIs together: parsing free-text exercise input
  with Nutritionix, then using its output to build the payload for a
  second POST to Sheety.
- A `for` loop body isn't just whatever's indented near it: I had the
  `requests.post()` call sitting one indent level outside the loop that
  built the payload, so only the last exercise from a multi-exercise
  query ever got logged instead of all of them.
- Reusing a variable name (`exercise`) for both the loop variable and an
  earlier value silently shadows the original; renaming the input
  variable to `exercise_question` fixed it.
- Sheety expects the POST body nested under the sheet/tab name (e.g.
  `{"workout": {...}}`), not a flat dict of column names.
- Keeping config in `.env` instead of hardcoding it, including things
  like API endpoint URLs, not just keys, makes the script portable
  across different Sheety projects/sheets.
