def set_age(age):
    if age < 0:
        raise ValueError("Age must be positive")
    return age


try:
    set_age(-5)
except ValueError as e:
    print("Log:", e)
    raise
