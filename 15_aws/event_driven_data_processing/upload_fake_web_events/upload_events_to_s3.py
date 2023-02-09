from fake_web_events import Simulation


if __name__ == "__main__":
    simulation = Simulation(user_pool_size=10, sessions_per_day=1000)
    events = simulation.run(duration_seconds=60)

    for event in events:
        print(event)
