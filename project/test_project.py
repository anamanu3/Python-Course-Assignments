from project import (
    read_workouts, save_workouts, add_workout, weekly_km,
    pace_min_per_km, best_5k, week_dates,
    read_pbs, save_pbs, add_pb,
    read_goals, save_goals,
)



def test_add_and_roundtrip_workouts(tmp_path):
    path = tmp_path / "workouts.csv"
    rows = []
    rows = add_workout(rows, "2025-05-15", "run", 5, 27.5, "", "easy")
    rows = add_workout(rows, "2025-05-16", "lift", 0, 0, "legs", "squats")
    save_workouts(str(path), rows)
    loaded = read_workouts(str(path))
    assert len(loaded) == 2
    assert loaded[0]["type"] == "run"
    assert loaded[0]["distance_km"] == 5.0
    assert loaded[1]["type"] == "lift"
    assert loaded[1]["lift_day"] == "legs"

def test_weekly_km_sum():
    rows = []
    rows = add_workout(rows, "2025-05-12", "run", 5, 28, "", "")
    rows = add_workout(rows, "2025-05-13", "run", 3, 18, "", "")
    rows = add_workout(rows, "2025-05-18", "run", 2, 12, "", "")  # inside same week
    rows = add_workout(rows, "2025-05-19", "run", 10, 60, "", "") # next week
    total = weekly_km(rows, "2025-05-12")
    assert total == 10.0  # 5 + 3 + 2

def test_pace_min_per_km_ok():
    pace = pace_min_per_km(5, 27.5)
    assert pace == 5.5

def test_pace_min_per_km_raises():
    raised = False
    try:
        pace_min_per_km(0, 20)
    except ValueError:
        raised = True
    assert raised

def test_best_5k_ok():
    rows = []
    rows = add_workout(rows, "2025-05-12", "run", 5.0, 28.0, "", "")
    rows = add_workout(rows, "2025-05-13", "run", 5.0, 26.5, "", "")
    rows = add_workout(rows, "2025-05-14", "run", 4.0, 20.0, "", "")
    best = best_5k(rows)
    assert best == 26.5

def test_best_5k_none():
    rows = []
    rows = add_workout(rows, "2025-05-12", "run", 4.0, 20.0, "", "")
    assert best_5k(rows) is None

def test_week_dates_simple():
    days = week_dates("2025-05-12")
    assert len(days) == 7
    assert days[0] == "2025-05-12"
    assert days[-1] == "2025-05-18"



def test_pbs_roundtrip(tmp_path):
    path = tmp_path / "pbs.csv"
    rows = []
    rows = add_pb(rows, "2025-05-15", "5k", "26:40")
    rows = add_pb(rows, "2025-05-20", "deadlift", "205 lb")
    save_pbs(str(path), rows)
    loaded = read_pbs(str(path))
    assert len(loaded) == 2
    assert loaded[0]["workout"] == "5k"
    assert loaded[1]["notes"] == "205 lb"



def test_goals_roundtrip(tmp_path):
    path = tmp_path / "goals.csv"
    g = {"calories": 2200, "protein_g": 130, "carbs_g": 230, "fat_g": 70}
    save_goals(str(path), g)
    loaded = read_goals(str(path))
    assert loaded == g

def test_read_goals_missing(tmp_path):
    path = tmp_path / "nope.csv"
    loaded = read_goals(str(path))
    assert loaded is None
