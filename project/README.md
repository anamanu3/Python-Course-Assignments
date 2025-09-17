Workout Log (Runs, Lifts, PBs, and Goals)

Video Demo: (https://youtu.be/-HyoNlSeoPk)
Author: Ana Manu
CS50P Final Project
2025-09-16






What this is:
A command-line tracker for workouts where you can add a
run (distance + time) or a lift (day/type + notes)
and see your weekly workouts laid out by date.
You are able to record and view PBs (personal bests),
set and view calorie and macro goals and delete or alter saved information.

Everything is stored in small CSV files in the same folder.
No internet, no accounts, no external libraries.



How to run:
python project.py

You’ll see a menu:

Workout Log
1) add workout
2) weekly workouts
3) PBs
4) calorie and macro goals
5) delete
6) quit

Use the numbers to pick what you want to do



Files in this project:
project.py — the main program (inputs, prints, CSV reads/writes)
workouts.csv — created after first save. This holds runs and lifts data
pbs.csv — created after first PB. This holds personal bests data
goals.csv — created after first goal save. This csv file holds data on calories/macros goals
requirements.txt — empty (standard library only)



How the data is stored:
workouts.csv
date,type,distance_km,duration_min,lift_day,notes
2025-05-15,run,5.0,27.5,,easy 5k
2025-05-16,lift,0.0,0.0,legs,10 pull-ups x3 sets

Runs use type=run, with distance_km and duration_min
Lifts use type=lift, with lift_day (like chest/back/legs/etc)
Notes are free text

pbs.csv
date,workout,notes
2025-05-15,5k,26:40 official
2025-05-20,deadlift,205 lb single

goals.csv
calories,protein_g,carbs_g,fat_g
2200,130,230,70

What each menu item does
1) add workout - lets you add data to your workout log
You choose run or lift
if run, you enter distance in km (numbers only, like 5 or 7.5) and duration (minutes or mm:ss)
if lift, you enter lift day (chest/back/legs/etc).
There is also a (useful) option to add optional notes about the workout!
(all data here saved to workouts.csv - upon first save, file created)


2) weekly workouts - lets you see your logged workouts
To use, enter a week start date (YYYY-MM-DD). This will print a simple
table with 7 rows (one per day) and it shows the type and details of
the workout (for runs: distance + time; for lifts: lift day). This
table also displays the notes about the wokrout, if added. Finally,
this option also prints the total nbumber of kms ran for that week.



3) PBs
This section allows for the choices of adding a PB ("add PB"), which
asks for the date of the PB, the workout name, and any notes like weight or reps.
You may also decide to display all your PBs by selecting "see all PBs". This
option prints a table of all workouts you are tracking PBs on. And lastly,
there is an option to bring you back to the main menu ("back").

4) calorie and macro goals
This section both allows you to choose to see your current macro/calorie goals
or allows you to update them.

5) delete
This section allows you to perminantly erase a wokrout or PB you've previously
added. It asks for if you want to delete a workout or a PB. For workouts, it
asks for you to enter the date and type (run/lift). If there are multiple
workouts on one date, it asks you which you want to delete by numbered list
and input choice. For deleting PBs, the program asks you to enter the workout
name you want deleted. Changes are, then saved.


Resetting:
To start fresh, delete workouts.csv, pbs.csv, and/or goals.csv.


Notes:
- CSV files use so data can be changed by hand.
- Tables are printed with fixed column widths for readability
