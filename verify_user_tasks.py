import urllib.request
import json
import sys

# Try 8005 or 8006. Previous runs suggest 8005 is active.
BASE_URL = "http://localhost:8005"

def test_admin_user_tasks():
    user_id = 2 
    url = f"{BASE_URL}/admin/users/{user_id}/tasks"
    print(f"Fetching tasks form: {url}")
    
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                print(f"Success! Found {len(data)} tasks.")
                for task in data:
                    print(f"- [ID: {task['id']}] {task['title']}")
            else:
                print(f"Failed. Status: {response.status}")
    except Exception as e:
        print(f"Error fetching tasks: {e}")

if __name__ == "__main__":
    test_admin_user_tasks()
