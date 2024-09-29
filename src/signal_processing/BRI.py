from live_advance import LiveAdvance

CLIENT_SECRET = 'zNmQlj2tRXg43B9oH1mjSY1mSDdggqJIEVUYNQRvjlqbRZYjNJwDrNxEwIpXiB73F5450Xy41vJj0NtCRjV7TwxKd3VsKckmPRFlzhTlsnqcFafCjY6msd3n9QtvhORU'
CLIENT_ID = '7vPRhxTutkNjsKhZ9xn6YW6z6JJbXhYSh3NRx1YG'

def main():
    workflow = LiveAdvance(app_client_id=CLIENT_ID, app_client_secret=CLIENT_SECRET)
    workflow.start("guilherme")

if __name__ == "__main__":
    main()